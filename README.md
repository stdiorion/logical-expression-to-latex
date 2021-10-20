# Logical Expression to LaTeX

Turning plain-text logical expressions into LaTeX-styled expressions.

Available in both CLI and GUI.

## Dependencies

- Python 3.6 or later

## Usage (from command line)

```sh
$ python converter.py your-expression
```

### Examples

`not P` ->  <img style="background: white" src="https://render.githubusercontent.com/render/math?math={\overline{P}}">

```sh
$ python converter.py not P
\overline{P}
```

`not not P` -> <img style="background: white" src="https://render.githubusercontent.com/render/math?math={P}">

```sh
$ python converter.py not not P
P
```

`P or Q` -> <img style="background: white" src="https://render.githubusercontent.com/render/math?math={P %2B Q}">

```sh
$ python converter.py P or Q
P + Q
```

`(A xnor ~B) xnor (C xnor D)` -> <img style="background: white" src="https://render.githubusercontent.com/render/math?math={( A \ xnor\ \overline{B} ) \ xnor\ ( C \ xnor\ D )}">

```sh
$ python converter.py "(A xnor ~B) xnor (C xnor D)"
( A \ xnor\ \overline{B} ) \ xnor\ ( C \ xnor\ D )
```

`not (A or B) = (not A and not B)` -> <img style="background: white" src="https://render.githubusercontent.com/render/math?math={(\overline{ A %2B B }) = ( \overline{A} \cdot \overline{B} )}">

```sh
$ python converter.py "not (A or B) = (not A and not B)"
(\overline{ A + B }) = ( \overline{A} \cdot \overline{B} )
```
`not {A or B} = not A and not B` -> <img style="background: white" src="https://render.githubusercontent.com/render/math?math={\overline{ A %2B B } = \overline{A} \cdot \overline{B}}">

```
$ python converter.py "not {A or B} = not A and not B"
\overline{ A + B } = \overline{A} \cdot \overline{B}
```

## Usage (GUI app)

```sh
$ python converter_gui.py
```

![image](https://user-images.githubusercontent.com/75237455/138011733-9f40f851-6d5d-4fc4-bbc4-8174a6fcdf2f.png)
