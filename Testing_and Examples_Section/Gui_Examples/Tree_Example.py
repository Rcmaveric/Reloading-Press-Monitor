from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Cartridge","Caliber","Bullet_Type", "Charge","Powder_Type","Charge_Volume","Case",
                                            "Case_Length","COAL","Primer"), height=400, 
                                            selectmode="extended", yscrollcommand=scrollbary.set, 
                                            xscrollcommand=scrollbarx.set)
tree.heading('Cartridge', text="Cartridge", anchor=W)
tree.heading('Caliber', text="Caliber", anchor=W)
tree.heading('Bullet_Type', text="Bullet_Type", anchor=W)
tree.heading('Charge', text="Charge", anchor=W)
tree.heading('Powder_Type', text="Powder_Type", anchor=W)
tree.heading('Charge_Volume', text="Charge_Volume", anchor=W)
tree.heading('Case', text="Case", anchor=W)
tree.heading('Case_Length', text="Case_Length", anchor=W)
tree.heading('COAL', text="COAL", anchor=W)
tree.heading('Primer', text="Primer", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=50)
tree.column('#2', stretch=NO, minwidth=0, width=50)
tree.column('#3', stretch=NO, minwidth=0, width=50)
tree.column('#4', stretch=NO, minwidth=0, width=50)
tree.column('#5', stretch=NO, minwidth=0, width=50)
tree.column('#6', stretch=NO, minwidth=0, width=50)
tree.column('#7', stretch=NO, minwidth=0, width=50)
tree.column('#8', stretch=NO, minwidth=0, width=50)
tree.column('#9', stretch=NO, minwidth=0, width=50)
tree.column('#10', stretch=NO, minwidth=0, width=50)
tree.pack()
with open('3_3_Cartridge_Recipe.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        cart = row['cartridge']
        cal = row['caliber']
        bul = row['bullet']
        bt = row['bullet_type']
        chg = row['charge']
        pt = row['powder_type']
        cv = row['charge_volume']
        case = row['case']
        cl = row['case_Length']
        coal = row['coal']
        primer = row['primer']
        tree.insert("", 0, values=(cart, cal, bul, bt, chg, pt, cv, case, cl, coal, primer))

if __name__ == '__main__':
    root.mainloop()