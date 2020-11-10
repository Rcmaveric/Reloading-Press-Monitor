import tkinter as tk


class Test(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent =  parent
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello World!")
        self.label.pack()
        self.quit = tk.Button(self, text= "Quit", command=self.controller.destroy)
        self.quit.pack()