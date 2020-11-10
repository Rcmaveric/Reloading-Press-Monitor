from tkinter import * 
import csv


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()
    def output(self):
        firstName=Label(self,text='First Name:')
        firstName.grid(row=1,column=0, padx=5, pady=3)
        self.e = Entry(self, width=10)
        self.e.grid(row=1,column=1, padx=5, pady=3)
        lastName=Label(self,text='Last Name:')
        lastName.grid(row=1,column=2, padx=5, pady=3)
        self.e1 = Entry(self, width=10)
        self.e1.grid(row=1,column=3, padx=5, pady=3)
        self.b = Button(self, text='Submit',command=self.writeToFile)
        self.b.grid(row=1,column=4, padx=5, pady=3)
    def writeToFile(self):
        with open('WorkOrderLog.csv', 'a') as f:
            w=csv.writer(f, delimiter=',')
            w.writerow([self.e.get()])
            w.writerow([self.e1.get()])


if __name__ == "__main__":
     root=Tk()
     root.title('Auto Logger')
     root.geometry('500x200')
     app=App(master=root)
     app.mainloop()
     root.mainloop()