import sys
import re
from typing import Dict, Set

DEFAULT_TEXDICT = {
    "and": "\cdot",
    "or": "+",
    "xor": "\oplus",
    "nor": "\ nor\ ",
    "nand": "\ nand\ ",
    "xnor": "\ xnor\ ",
}

DEFAULT_NEGATIONS = {
    "not",
    "~"
}

def convert(raw_text: str, texdict: Dict[str, str] = None, negations: Set[str] = None, align_equal: bool = False):
    if texdict is None:
        texdict = DEFAULT_TEXDICT
    if negations is None:
        negations = DEFAULT_NEGATIONS
    
    res_text = raw_text

    for key, value in texdict.items():
        res_text = res_text.replace(" " + key + " ", " " + value + " ")

    # Split by "(){} \n", *NAGATIONS but not eliminate them
    # Ex. "not (P and ~Q) or (~P and Q)"
    #     -> ['', 'not', ' ', '(', 'P and ~Q', ')', ' or ', '(', '~P and Q', ')', '']
    stringpart = "|".join(p for p in negations if len(p) > 1)
    if stringpart:
        stringpart = "|" + stringpart
    re_pattern = "([\(\)\{\}\ \n" + "".join(p for p in negations if len(p) == 1) + "]" + stringpart + ")"
    res_text_splitted = re.split(re_pattern, res_text)

    # Remove whitespace or empty chunk
    # Ex. ['not', '(', 'P and ', '~', 'Q', ')', ' + ', '(', '~', 'P and Q', ')']
    res_text_splitted = [s for s in res_text_splitted if not set(s) <= {" "}]

    negated = False
    paren_depth = 0
    negated_depths = []
    
    res_line = []
    res_lines = []

    if align_equal:
        res_lines.append("\\begin{aligned}")

    for chunk in res_text_splitted:
        if chunk == "\\n" or chunk == "\n":
            # new line
            if res_line:
                if align_equal:
                    if "=" in res_line:
                        res_line[res_line.index("=")] = "&="
                    # new line in the "aligned" block
                    res_line.append("\\\\")
                res_lines.append(" ".join(res_line))
                res_line = []
        elif negated:
            if chunk == "(":
                # not (something) -> (\overline{ something })
                paren_depth += 1
                negated_depths.append(paren_depth)
                res_line.append("(\overline{")
            elif chunk == "{":
                # not {something} -> \overline{ something }
                paren_depth += 1
                negated_depths.append(paren_depth)
                res_line.append("\overline{")
            elif chunk in negations:
                # not not -> disappear
                pass
            else:
                # not something -> \overline{ something }
                res_line.append("\overline{" + chunk + "}")

            negated = False

        else:
            if chunk == "(" or chunk == "{":
                paren_depth += 1
                res_line.append(chunk)
            elif chunk == ")":
                if negated_depths and negated_depths[-1] == paren_depth:
                    # ")" as the end of negation
                    negated_depths.pop()
                    res_line.append("})")
                else:
                    # just ")"
                    res_line.append(")")
                paren_depth -= 1
            elif chunk == "}":
                if negated_depths and negated_depths[-1] == paren_depth:
                    # "}" as the end of negation
                    negated_depths.pop()
                    res_line.append("}")
                else:
                    # just "}"
                    res_line.append("}")
                paren_depth -= 1
            elif chunk in negations:
                # not -> negates next
                negated = True
            else:
                # everything else
                res_line.append(chunk)

    if align_equal:
        if "=" in res_line:
            res_line[res_line.index("=")] = "&="
    res_lines.append(" ".join(res_line))

    if align_equal:
        res_lines.append("\\end{aligned}")

    return "\n".join(res_lines)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("USAGE:")
        print(f"if you prefer CLI $ python {__file__} text-you-want-to-convert")
        print(f"or you want GUI? $ python {__file__.rsplit('.', 1)[0] + '_gui.' + __file__.rsplit('.', 1)[1]}")
    else:
        print(convert(" ".join(sys.argv[1:])))
