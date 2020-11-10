import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("class basic window")
        self.config(background="LightBlue4")
        self.lower_tabs = ["Week 1", "Week 2"]
        self.lower_tabs_dict = {}
        self.buttons_dict = {}
        self.create_lower_tabs()
        self.week1 = Week(self)
        self.week1.pack()

    def create_lower_tabs(self):
        style1 = ttk.Style()
        style1.configure("down.TNotebook", tabposition="sw")
        self.tab_control_lower = ttk.Notebook(self, width=1100, height=550, padding=0, style="down.TNotebook")
        for name in self.lower_tabs:
            self.lower_tabs_dict[name] = tk.Frame(self.tab_control_lower, bg='old lace')
            self.tab_control_lower.add(self.lower_tabs_dict[name], text=name)
        self.tab_control_lower.pack(fill=tk.BOTH, expand=1)


class Week(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        tk.Button(self.parent.lower_tabs_dict["Week 1"], text="test button", bg="salmon",).pack()
        tk.Button(self.parent.lower_tabs_dict["Week 2"], text="this page 2 button", bg="salmon").pack()


if __name__ == '__main__':
    Application().mainloop()