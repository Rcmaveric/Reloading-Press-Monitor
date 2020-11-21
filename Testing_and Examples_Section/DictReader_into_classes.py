import tkinter as tk
import sys
from tkinter import ttk
#from ttkthemes import ThemedStyle #Causes error during testing but works during normal run
import csv
import datetime
import ast
import pprint


#Note to self: the way this works is the csv is turned into a class. The class name is the list ID which is Recipe[n],
#where N is the number of the recipe line with 0 being the first line. After that the heading can be use as a dot atribut,
#IE Recipe[0].cartridge will give you the cartridge name of recipe 0.
with open('3_3_Cartridge_Recipe.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    class Recipe:
        def __init__(self, **fields):
            self.__dict__.update(**fields)

        def __repr__(self):  # Added to make printing instances show their contents.
            fields = ','.join(('{}={!r}'.format(fieldname, getattr(self, fieldname))
                                   for fieldname in fieldnames))
            return('{}({})'.format(self.__class__.__name__, fields))

    Loads = [Recipe(**row) for row in reader]
    print (Loads)
    
    def Recipe_Update():
        Loads.clear()
        with open('3_3_Cartridge_Recipe.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames

            class Recipe:
                def __init__(self, **fields):
                    self.__dict__.update(**fields)

                def __repr__(self):  # Added to make printing instances show their contents.
                    fields = ','.join(('{}={!r}'.format(fieldname, getattr(self, fieldname))
                                        for fieldname in fieldnames))
                    return('{}({})'.format(self.__class__.__name__, fields))

            new = ([Recipe(**row) for row in reader])
            Loads.extend(new)
           


class Recipe_Editor(tk.Frame):
    def __init__(self, master, window, window_title):                
        self.master = master
        self.window = window
        self.window.title(window_title)
    #Frame that hold TreeView
        self.data_display = tk.Frame(window)
        self.data_display.pack(side="top")
        self.TableMargin = tk.Frame(self.data_display)
        self.TableMargin.pack(side="right")         
        self.scrollbarx = ttk.Scrollbar(self.TableMargin, orient="horizontal")
        self.scrollbary = ttk.Scrollbar(self.TableMargin, orient="vertical")
        self.tree = ttk.Treeview(self.TableMargin, columns=("Cartridge","Caliber", "Bullet", "Bullet_Type", "Charge","Powder_Type","Charge_Volume","Case",
                                            "Case_Length","COAL","Primer"), selectmode="extended", 
                                            yscrollcommand=self.scrollbary.set, 
                                            xscrollcommand=self.scrollbarx.set)
        
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side="right", fill="y")
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side="bottom", fill="x")
        self.tree.heading('Cartridge', text="Cartridge", anchor="w")
        self.tree.heading('Caliber', text="Caliber", anchor="w")
        self.tree.heading('Bullet', text="Bullet", anchor="w")
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

    #Frame to hold the Data Entry form.
        self.data_input_frame = ttk.Labelframe(window, text="Add New Recipe")
     #Labels
        self.cartridge_label = tk.Label(self.data_input_frame, text="Cartridge")
        self.cartridge_label.grid(column=0, row=0)
        self.cal_label = tk.Label(self.data_input_frame, text="Caliber")
        self.cal_label.grid(column=1, row=0)
        self.bul_label = tk.Label(self.data_input_frame, text="Bullet")
        self.bul_label.grid(column=2, row=0)
        self.bt_label = tk.Label(self.data_input_frame, text="Bullet Type")
        self.bt_label.grid(column=3, row=0)
        self.chg_label = tk.Label(self.data_input_frame, text="Charge")
        self.chg_label.grid(column=4, row=0)
        self.pt_label = tk.Label(self.data_input_frame, text="Powder")
        self.pt_label.grid(column=5, row=0)
        self.cv_label = tk.Label(self.data_input_frame, text="Charge Vol.")
        self.cv_label.grid(column=6, row=0)
        self.case_label = tk.Label(self.data_input_frame, text="Case")
        self.case_label.grid(column=7, row=0)
        self.cl_label = tk.Label(self.data_input_frame, text="Case Length")
        self.cl_label.grid(column=8, row=0)
        self.coal_label = tk.Label(self.data_input_frame, text="COAL")
        self.coal_label.grid(column=9, row=0)
        self.primer_label = tk.Label(self.data_input_frame, text="Primer")
        self.primer_label.grid(column=10, row=0)
        
     #Entry feilds       
        self.cartridge_entry = ttk.Entry(self.data_input_frame, width=20)
        self.cartridge_entry.grid(column=0, row=1)
        self.cal_entry = ttk.Entry(self.data_input_frame, width=10)
        self.cal_entry.grid(column=1, row=1)
        self.bul_entry = ttk.Entry(self.data_input_frame, width=10)
        self.bul_entry.grid(column=2, row=1)
        self.bt_entry = ttk.Entry(self.data_input_frame, width=10)
        self.bt_entry.grid(column=3, row=1)
        self.chg_entry = ttk.Entry(self.data_input_frame, width=10)
        self.chg_entry.grid(column=4, row=1)
        self.pt_entry = ttk.Entry(self.data_input_frame, width=10)
        self.pt_entry.grid(column=5, row=1)
        self.cv_entry = ttk.Entry(self.data_input_frame, width=10)
        self.cv_entry.grid(column=6, row=1)
        self.case_entry = ttk.Entry(self.data_input_frame, width=10)
        self.case_entry.grid(column=7, row=1)
        self.cl_entry = ttk.Entry(self.data_input_frame, width=10)
        self.cl_entry.grid(column=8, row=1)
        self.coal_entry = ttk.Entry(self.data_input_frame, width=10)
        self.coal_entry.grid(column=9, row=1)
        self.primer_entry = ttk.Entry(self.data_input_frame, width=10)
        self.primer_entry.grid(column=10, row=1)
        self.save_data_bt = ttk.Button(self.data_input_frame, text ="Save", width=10, command= self.Write_Data_To_File)
        self.save_data_bt.grid(column=0, row = 3)
        self.data_input_frame.pack(side="bottom")
        
    #Frame to hold delete button. Wanted and Edit button but that is proving to difficult to figure out
        self.button_frame = tk.Frame(self.data_display)
        self.button_frame.pack(side="right")
        self.dellet_data_bt = ttk.Button(self.button_frame, text = "Delete", width=10, command= self.Remove_Item)
        self.dellet_data_bt.pack()

   #Functions, Methods and Commands

    def Write_Data_To_File(self): #Writes entry fields into tree and into CSV file.
        ba = self.cartridge_entry.get()
        bb = self.cal_entry.get()
        bz = self.bul_entry.get()
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
            w.writerow([ba, bb, bz, bc, bd, be, bf, bg, bh, bi, bj]) #Adds to file. Only writes the new line.
            self.row = self.tree.insert("","end",values=(ba, bb, bz, bc,bd,be, bf, bg, bh, bi, bj)) #Updates the tree
        
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


class FormBox(ttk.LabelFrame):
    def __init__(self, master):        
        ttk.LabelFrame.__init__(self, master, text="Reloading Log")
        self.master = master
        self.formz_frame = tk.Frame(self)
    #Form Labels
        date_label = ttk.Label(self.formz_frame, text="Date")
        date_label.grid(column=0, row=0)
        caliber_label = ttk.Label(self.formz_frame, text="Caliber")
        caliber_label.grid(column=1, row=0)
        bullet_MFG_label = ttk.Label(self.formz_frame, text="Bul MFG")
        bullet_MFG_label.grid(column=2, row=0)
        bullet_type_label = ttk.Label(self.formz_frame, text="Bul Type")
        bullet_type_label.grid(column=3, row=0)
        powder_CHG_label = ttk.Label(self.formz_frame, text="Pwd CH")
        powder_CHG_label.grid(column=4, row=0)
        powder_type_label = ttk.Label(self.formz_frame, text="Pwd")
        powder_type_label.grid(column=5, row=0)
        powder_vol_label = ttk.Label(self.formz_frame, text="Pwd Vol")
        powder_vol_label.grid(column=6, row=0)
        case_type_label = ttk.Label(self.formz_frame, text="Case")
        case_type_label.grid(column=7, row=0)
        case_length_label = ttk.Label(self.formz_frame, text="Length")
        case_length_label.grid(column=8, row=0)
        COAL_label = ttk.Label(self.formz_frame, text="COAL")
        COAL_label.grid(column=9, row=0)
        primer_label = ttk.Label(self.formz_frame, text="Primer")
        primer_label.grid(column=10, row=0)
        rounds_loaded_label = ttk.Label(self.formz_frame, text="Rounds")
        rounds_loaded_label.grid(column=11, row=0)
    #Form Input Boxes
        #Sets default current date
        to_day = datetime.datetime.now() # Retreve current date.
        self.date_box = ttk.Entry(self.formz_frame,width=10)
        self.date_box.grid(column=0, row=1)
        self.date_box.insert(0, to_day.strftime("%d%b%Y")) # Sets todays date as default entry
        self.caliber_box = ttk.Entry(self.formz_frame)
        self.caliber_box.grid(column=1, row=1)
        self.bullet_MFG_box = ttk.Entry(self.formz_frame, width=10)
        self.bullet_MFG_box.grid(column=2, row=1)
        self.bullet_type_box = ttk.Entry(self.formz_frame, width=10)
        self.bullet_type_box.grid(column=3, row=1)
        self.powder_CHG_box = ttk.Entry(self.formz_frame, width=6)
        self.powder_CHG_box.grid(column=4, row=1)
        self.powder_type_box = ttk.Entry(self.formz_frame,width=10)
        self.powder_type_box.grid(column=5, row=1)
        self.powder_volume_Box = ttk.Entry(self.formz_frame,width=6)
        self.powder_volume_Box.grid(column=6, row=1)
        self.case_type = ttk.Entry(self.formz_frame,width=10)
        self.case_type.grid(column=7, row=1)
        self.case_length_Box = ttk.Entry(self.formz_frame,width=5)
        self.case_length_Box.grid(column=8, row=1)
        self.COAL_box = ttk.Entry(self.formz_frame,width=10)
        self.COAL_box.grid(column=9, row=1)
        self.primer_box = ttk.Entry(self.formz_frame,width=7)
        self.primer_box.grid(column=10, row=1)
        self.rounds_loaded_Box = ttk.Entry(self.formz_frame,width=6)
        self.rounds_loaded_Box.grid(column=11, row=1)
        self.formz_frame.grid(column=0, row=0)   
    
        self.button_frame = tk.Frame(self)
        self.clear_btn = ttk.Button(self.button_frame, text="Clear", command=lambda: self.Editor())
        self.clear_btn.grid(column=0, row=0)
        self.export_btn = ttk.Button(self.button_frame, text="Export", command=lambda:self.Combo_Update())
        self.export_btn.grid(column=3, row=0)

        self.combo_frame = tk.Frame(self.button_frame)
        self.load_select_label = tk.Label(self.combo_frame, text="Pet Loads")
        self.load_select_label.grid(row=0, column=0)
        self.load_select = ttk.Combobox(self.combo_frame, width=25, value = Loads)
        self.load_select.bind("<<ComboboxSelected>>", self.Combo_Entry)
        self.load_select.grid(column=1, row=0)
        self.combo_frame.grid(column=2, row=0)

        self.button_frame.grid(column=0, row=2, )
   
    def Combo_Update(self):
        self.load_select['value'] = Loads
    def Combo_Entry(self, eventObject):
        self.Clear_Load_data()
        #This Code magically turns our string back into a Dictionary
        raw_string_recipe = self.load_select.get()#get data string
        new_data_string=raw_string_recipe[7:]#removes recipe from string
        #Now we clean the string
        #strip quoatation
        qq = new_data_string.replace("'","")        
        # first remove the () from it
        s = qq.replace("(", " ")
        finalstring = s.replace(")"," ")
        
        list = finalstring.split(",")
        self.dictionary={}
        for i in list:
            keyvalue = i.split("=")
            m= keyvalue[0].strip('\'')
            m = m.replace("\"", "")
            self.dictionary[m] = keyvalue[1].strip('"\'')
        
        self.caliber_box.insert(0, self.dictionary["caliber"])
        self.bullet_MFG_box.insert(0, self.dictionary["bullet"])
        self.bullet_type_box.insert(0, self.dictionary["bullet_type"])
        self.powder_CHG_box.insert(0, self.dictionary["charge"])
        self.powder_type_box.insert(0, self.dictionary["powder_type"])
        self.powder_volume_Box.insert(0, self.dictionary["charge_volume"])
        self.case_type.insert(0, self.dictionary["case"])
        self.case_length_Box.insert(0, self.dictionary["case_Length"])
        self.COAL_box.insert(0, self.dictionary["coal"])
        self.primer_box.insert(0, self.dictionary["primer"])


    def Clear_Load_data(self):
        self.caliber_box.delete(0, tk.END)
        self.bullet_MFG_box.delete(0, tk.END)
        self.bullet_type_box.delete(0, tk.END)
        self.powder_CHG_box.delete(0, tk.END)
        self.powder_type_box.delete(0, tk.END)
        self.powder_volume_Box.delete(0, tk.END)
        self.case_type.delete(0, tk.END)
        self.case_length_Box.delete(0, tk.END)
        self.COAL_box.delete(0, tk.END)
        self.primer_box.delete(0, tk.END)
        self.rounds_loaded_Box.delete(0, tk.END)
    def Editor(self):
        self.new_window = tk.Toplevel(self)
        self.editor_of_recipes = Recipe_Editor(self, window=self.new_window, window_title="Editor")
     
#Main Aplication Window to call in the classes
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AMMMO Computer")

      
#First Frame: I like my computer to great me. Makes me feel needed.
        self.first_frame = tk.Frame(self)
        welcome = tk.Label(self.first_frame, text="Welcome Rcmaveric, lets make some ammo!")
        welcome.pack(fill="both")
        self.button = tk.Button(self.first_frame, command = lambda: Recipe_Update(), text="Editor")
        self.button.pack()
        self.first_frame.grid(column=0, row= 0)
#Fourth Frame
        self.fourth_frame = tk.Frame(self)
        self.forms = FormBox(self.fourth_frame)
        self.forms.pack()
        self.fourth_frame.grid(column=0, row=2)
    
    def Pet_Loads_Log(self):
        self.recipes_window = tk.Toplevel(self)
        self.recipe_editor = Recipe_Editor(self.recipes_window, window=self.recipes_window, window_title="Load Editor")
        self.recipe_window.wm_protocol("WM_DELETE_WINDOW", lambda: self.Update_Close())

    def Update_Close(self):
        Recipe_Update()
        self.forms.Combo_Update()
        self.destroy

    
        
#Commands

if __name__ == "__main__":
    app=App()
    #style = ThemedStyle()
    #style.set_theme("breeze")
    app.mainloop()