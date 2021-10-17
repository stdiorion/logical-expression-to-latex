import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from converter import convert

FONT_FAMILY = "Consolas"
FONT_SIZE = 14

AUTO_UPDATE_INTERVAL = 2000

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Logical Expression to LaTeX")
        self.geometry("500x800")
        self.create_widgets()

        self.listener()
    
    def create_widgets(self):
        # source textbox
        self.src_box = ScrolledText(self, relief="flat", padx=10, pady=10, font=(FONT_FAMILY, FONT_SIZE))
        self.src_box.pack(fill=tk.BOTH, expand=True)
        self.src_box.focus_set()

        self.separator = tk.Label(self, text="↓ Convert ↓")
        self.separator.pack()

        # destination textbox
        self.dst_box = ScrolledText(self, relief="flat", padx=10, pady=10, font=(FONT_FAMILY, FONT_SIZE))
        self.dst_box.pack(fill=tk.BOTH, expand=True)
    
    def listener(self):
        raw_text = self.src_box.get(1.0, "end-1c")
        res_text = convert(raw_text)

        self.dst_box.delete(1.0, "end")
        self.dst_box.insert(1.0, res_text)

        # self.clipboard_clear()
        # self.clipboard_append(res_text)
        # self.update()

        self.after(AUTO_UPDATE_INTERVAL, self.listener)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
