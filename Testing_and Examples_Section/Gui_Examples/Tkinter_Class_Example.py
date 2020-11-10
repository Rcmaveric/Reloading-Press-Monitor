import tkinter as tk

root = tk.Tk()

class MainApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #a child frame of MainApp object
        self.frame1 = tk.Frame(self)

        tk.Label(self.frame1, text="This is MainApp frame1").pack()

        self.frame1.grid(row=0, column=0, sticky="nsew")


        #another child frame of MainApp object
        self.frame2 = SearchFrame(self)

        self.frame2.grid(row=0, column=1, sticky="nsew")




    def create_labels(self, master):
        return tk.Label(master, text="asd")


class SearchFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, text="this is SearchFrame")
        self.label.pack()

        master.label1 = MainApp.create_labels(self, master)

        master.label1.grid()


mainAppObject = MainApp(root)
mainAppObject.pack()

root.mainloop()