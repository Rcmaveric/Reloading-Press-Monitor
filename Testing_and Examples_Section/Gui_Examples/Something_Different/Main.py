import tkinter as tk
import Test


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Wtf, Test.Test):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Wtf")

    def show_frame(self, page_name):
        """ Show a frame for the given page name. """
        frame = self.frames[page_name]
        frame.tkraise()


class Wtf(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent =  parent
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.test = Test.Test(self.parent, self.controller)
        self.btn = tk.Button(self, text="Call",
                             command=lambda: self.controller.show_frame("Test"))
        self.btn.pack()


if __name__ == "__main__":

    app = App()
    app.mainloop()