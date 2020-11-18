import tkinter as tk
import sys
from tkinter import ttk
#from ttkthemes import ThemedStyle #Causes error during testing but works during normal run
import csv
import datetime
import ast


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

    Recipe = [Recipe(**row) for row in reader]
    print(Recipe)



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
        self.clear_btn = ttk.Button(self.button_frame, text="Clear", command=self.Clear_Load_data)
        self.clear_btn.grid(column=0, row=0)
        self.export_btn = ttk.Button(self.button_frame, text="Export", command=print(Recipe))
        self.export_btn.grid(column=3, row=0)

        self.combo_frame = tk.Frame(self.button_frame)
        self.load_select_label = tk.Label(self.combo_frame, text="Pet Loads")
        self.load_select_label.grid(row=0, column=0)
        self.load_select = ttk.Combobox(self.combo_frame, width=25, value = Recipe)
        self.load_select.bind("<<ComboboxSelected>>", self.Combo_Entry)
        self.load_select.grid(column=1, row=0)
        self.combo_frame.grid(column=2, row=0)

        self.button_frame.grid(column=0, row=2, )
   
    
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
        
      
#Main Aplication Window to call in the classes
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AMMMO Computer")

      
#First Frame: I like my computer to great me. Makes me feel needed.
        self.first_frame = tk.Frame(self)
        welcome = tk.Label(self.first_frame, text="Welcome Rcmaveric, lets make some ammo!")
        welcome.pack(fill="both")
        self.first_frame.grid(column=0, row= 0)
#Fourth Frame
        self.fourth_frame = tk.Frame(self)
        self.forms = FormBox(self.fourth_frame)
        self.forms.pack()
        self.fourth_frame.grid(column=0, row=2)
        
#Commands

if __name__ == "__main__":
    app=App()
    #style = ThemedStyle()
    #style.set_theme("breeze")
    app.mainloop()