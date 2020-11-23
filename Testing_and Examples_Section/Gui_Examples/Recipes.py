import tkinter as tk
from tkinter import ttk
import csv
from ttkthemes import ThemedStyle #Runs just fine but causes import errors during testing.



class Recipe_Editor(tk.Frame):
    def __init__(self, master):                
        tk.Frame.__init__(self, master)
        self.master = master
#Frame that hold TreeView
        self.data_display = tk.Frame(self)
        self.data_display.pack(side="top")
        self.TableMargin = tk.Frame(self.data_display)
        self.TableMargin.pack(side="right")         
        self.scrollbarx = ttk.Scrollbar(self.TableMargin, orient="horizontal")
        self.scrollbary = ttk.Scrollbar(self.TableMargin, orient="vertical")
        self.tree = ttk.Treeview(self.TableMargin, columns=("Cartridge","Caliber","Bullet_Type", "Charge","Powder_Type","Charge_Volume","Case",
                                            "Case_Length","COAL","Primer"), selectmode="extended", 
                                            yscrollcommand=self.scrollbary.set, 
                                            xscrollcommand=self.scrollbarx.set)
        
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side="right", fill="y")
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side="bottom", fill="x")
        self.tree.heading('Cartridge', text="Cartridge", anchor="w")
        self.tree.heading('Caliber', text="Caliber", anchor="w")
        self.tree.heading('Bullet_Type', text="Bullet Type", anchor="w")
        self.tree.heading('Charge', text="Charge", anchor="w")
        self.tree.heading('Powder_Type', text="Powder Type", anchor="w")
        self.tree.heading('Charge_Volume', text="Charge Vol.", anchor="w")
        self.tree.heading('Case', text="Case", anchor="w")
        self.tree.heading('Case_Length', text="Case Len.", anchor="w")
        self.tree.heading('COAL', text="COAL", anchor="w")
        self.tree.heading('Primer', text="Primer", anchor="w")
        self.tree.column('#0', stretch="no", minwidth=0, width=0) #not used
        self.tree.column('#1', stretch="no", minwidth=0, width=75)
        self.tree.column('#2', stretch="no", minwidth=0, width=75)
        self.tree.column('#3', stretch="no", minwidth=0, width=75)
        self.tree.column('#4', stretch="no", minwidth=0, width=75)
        self.tree.column('#5', stretch="no", minwidth=0, width=75)
        self.tree.column('#6', stretch="no", minwidth=0, width=75)
        self.tree.column('#7', stretch="no", minwidth=0, width=75)
        self.tree.column('#8', stretch="no", minwidth=0, width=75)
        self.tree.column('#9', stretch="no", minwidth=0, width=75)
        self.tree.column('#10', stretch="no", minwidth=0, width=75)
    #Imports data into TreeView at start:
        with open('3_3_Cartridge_Recipe.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader: #This way gets all the data and matches it to row.
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
                self.tree.insert("", "end", values=(cart, cal, bul, bt, chg, pt, cv, case, cl, coal, primer))
        self.tree.pack()

#Frame to hold the Data Entry into file and tree view.
        self.data_input_frame = ttk.Labelframe(self, text="Add New Recipe")
    #Labels
        self.cartridge_label = tk.Label(self.data_input_frame, text="Cartridge")
        self.cartridge_label.grid(column=0, row=0)
        self.cal_label = tk.Label(self.data_input_frame, text="Caliber")
        self.cal_label.grid(column=1, row=0)
        self.bt_label = tk.Label(self.data_input_frame, text="Bullet Type")
        self.bt_label.grid(column=2, row=0)
        self.chg_label = tk.Label(self.data_input_frame, text="Charge")
        self.chg_label.grid(column=3, row=0)
        self.pt_label = tk.Label(self.data_input_frame, text="Powder")
        self.pt_label.grid(column=4, row=0)
        self.cv_label = tk.Label(self.data_input_frame, text="Charge Vol.")
        self.cv_label.grid(column=5, row=0)
        self.case_label = tk.Label(self.data_input_frame, text="Case")
        self.case_label.grid(column=6, row=0)
        self.cl_label = tk.Label(self.data_input_frame, text="Case Length")
        self.cl_label.grid(column=7, row=0)
        self.coal_label = tk.Label(self.data_input_frame, text="COAL")
        self.coal_label.grid(column=8, row=0)
        self.primer_label = tk.Label(self.data_input_frame, text="Primer")
        self.primer_label.grid(column=9, row=0)
        
        #Entry feilds       
        self.cartridge_entry = ttk.Entry(self.data_input_frame, width=20)
        self.cartridge_entry.grid(column=0, row=1)
        self.cal_entry = ttk.Entry(self.data_input_frame, width=10)
        self.cal_entry.grid(column=1, row=1)
        self.bt_entry = ttk.Entry(self.data_input_frame, width=10)
        self.bt_entry.grid(column=2, row=1)
        self.chg_entry = ttk.Entry(self.data_input_frame, width=10)
        self.chg_entry.grid(column=3, row=1)
        self.pt_entry = ttk.Entry(self.data_input_frame, width=10)
        self.pt_entry.grid(column=4, row=1)
        self.cv_entry = ttk.Entry(self.data_input_frame, width=10)
        self.cv_entry.grid(column=5, row=1)
        self.case_entry = ttk.Entry(self.data_input_frame, width=10)
        self.case_entry.grid(column=6, row=1)
        self.cl_entry = ttk.Entry(self.data_input_frame, width=10)
        self.cl_entry.grid(column=7, row=1)
        self.coal_entry = ttk.Entry(self.data_input_frame, width=10)
        self.coal_entry.grid(column=8, row=1)
        self.primer_entry = ttk.Entry(self.data_input_frame, width=10)
        self.primer_entry.grid(column=9, row=1)
        self.save_data_bt = ttk.Button(self.data_input_frame, text ="Save", width=10, command= self.Write_Data_To_File)
        self.save_data_bt.grid(column=0, row = 3)
        self.data_input_frame.pack(side="bottom")
        
        #Frame to hold delete button. Wanted and Edit button but that is proving to difficult to figure out
        self.button_frame = tk.Frame(self.data_display)
        self.button_frame.pack(side="right")
        self.dellet_data_bt = ttk.Button(self.button_frame, text = "Delete", width=10, command= self.Remove_Item)
        self.dellet_data_bt.pack()

    def Write_Data_To_File(self): #Writes entry fields into tree and into CSV file.
        ba = self.cartridge_entry.get()
        bb = self.cal_entry.get()
        bc = self.bt_entry.get()
        bd = self.chg_entry.get()
        be = self.pt_entry.get()
        bf = self.cv_entry.get()
        bg = self.case_entry.get()
        bh = self.cl_entry.get()
        bi = self.coal_entry.get()
        bj = self.primer_entry.get()
        with open('3_3_Cartridge_Recipe.csv', 'a', newline='') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([ba, bb, bc, bd, be, bf, bg, bh, bi, bj]) #Adds to file. Only writes the new line.
            self.row = self.tree.insert("","end",values=(ba, bb,bc,bd,be, bf, bg, bh, bi, bj)) #Updates the tree
    
    def Remove_Item(self): #Removes row from tree. Then overwrites CSV file with new tree.
        def Update_Recipe_File(self):#To over write CSV with new Treeview
            with open('3_3_Cartridge_Recipe.csv', 'w', newline='') as f:
                w=csv.writer(f, quoting=csv.QUOTE_ALL)
                w.writerow(['cartridge', 'caliber', 'bullet',
                               'bullet_type', 'charge', 'powder_type',
                               'charge_volume', 'case', 'case_Length',
                               'coal', 'primer']) #Rewrite our dictionary headings.
                for row_id in self.tree.get_children():
                    row = self.tree.item(row_id)['values']
                    w.writerow(row)

        self.selected_items = self.tree.selection()
        for selected_item in self.selected_items:        
            self.tree.delete(selected_item)#Removes selected item from tree
        Update_Recipe_File(self) #Then we over write the old CSV with the new tree.
    
    
if __name__ == "__main__":

    root = tk.Tk()
    style = ThemedStyle() #Commented out for testing. Works fun during normal running. Causes errors for test runs.
    style.set_theme("breeze") #Commented out for testing. Works fun during normal running. Causes errors for test runs.
    Recipe_Editor(root).pack()
    root.mainloop()