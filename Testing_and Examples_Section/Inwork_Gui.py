'''
Author:     Rcmaveric
Date:       07 Nov 2020
Licensing:  Do what you but you can't sell it. It stays open source with source codes available.
            Due to licensings of packages used.
IRL Name:   Ryan Conner
Email:      rcmaveric112@gmail.com
            I barely know what I am doing and Google and stack exchange will help you more than me. LMAO most of this code
            is copy pasted and lucky extropilated guesses. Yes, i faked it till i made. XD

Note:       Reason for all the comments: I am learning and reminders help. Also for others to learn.
            Most importantly, I use VSC and it allows nesting by comments. I can colapse the lines between
            comments to make the navigation of code easier. 

Contributors: The various 
'''
import tkinter as tk
import sys
from tkinter import ttk
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk
from ttkthemes import ThemedStyle
import csv
import datetime
import cv2

#Created a Load data class
class Current_Load_Data():
    def __init__(self, date, caliber, bullet_mfg, bullet_type, pwd_charge, powder_type, powder_volume,
                 case_type, case_length, coal, primer, round_count):
        self.date = date
        self.caliber = caliber 
        self.bullet_mfg = bullet_mfg
        self.bullet_type = bullet_type
        self.pwd_charge = pwd_charge
        self.powder_type = powder_type 
        self.powder_volume = powder_volume 
        self.case_type = case_type
        self.case_length = case_length
        self.coal = coal 
        self.primer = primer
        self.round_count = round_count

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

    #Frame to hold the Data Entry form.
        self.data_input_frame = ttk.Labelframe(window, text="Add New Recipe")
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

   #Functions, Methods and Commands

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

#when calling the cams. The new window will be a assigned to a Top Level Widget. You assigne the camera input during the
#Construction.
class Cam(tk.Frame):
    def __init__(self, master, window, window_title, video_source=0):
        self.master = master
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
 
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
 
            
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        
class MenuBar(tk.Menu):
    def __init__(self, master, add_remove):
        tk.Menu.__init__(self, master)
        self.add_remove = add_remove
        fileMenu = tk.Menu(self, tearoff=False)
        editMenu = tk.Menu(self, tearoff=False)
        loadsMenu = tk.Menu(self, tearoff=True)
        helpMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Copy", underline=0, command=None)
        fileMenu.add_command(label="Save", underline=0, command=None)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)
        self.add_cascade(label="Edit",underline=0, menu=editMenu)
        editMenu.add_command(label="Logo", underline=0, command=None)
        editMenu.add_command(label="Directories", underline=0, command=None)
        editMenu.add_command(label="Theme", underline=0, command=None)
        self.add_cascade(label="Loads", underline=0, menu=loadsMenu)
        loadsMenu.add_command(label="Add/Remove", underline=0, command=add_remove)
        loadsMenu.add_command(label="9MM HP38", underline=0, command=None)
        loadsMenu.add_command(label="9MM BD", underline=0, command=None)
        loadsMenu.add_command(label="357M 2400", underline=0, command=None)
        loadsMenu.add_command(label="6.5MM Gr BB", underline=0, command=None)
        self.add_cascade(label="Help", underline=0, menu=helpMenu)
        helpMenu.add_command(label="User Manual", underline=0, command=None)
        helpMenu.add_command(label="About", underline=0, command=None)

    def quit(self):
        sys.exit(0)

class FormBox(ttk.LabelFrame):
    def __init__(self, master):        
        ttk.LabelFrame.__init__(self, master, text="Reloading Log")
        self.master = master
    #Form Labels]
        date_label = ttk.Label(self, text="Date")
        date_label.grid(column=0, row=0)
        caliber_label = ttk.Label(self, text="Caliber")
        caliber_label.grid(column=1, row=0)
        bullet_MFG_label = ttk.Label(self, text="Bul MFG")
        bullet_MFG_label.grid(column=2, row=0)
        bullet_type_label = ttk.Label(self, text="Bul Type")
        bullet_type_label.grid(column=3, row=0)
        powder_CHG_label = ttk.Label(self, text="Pwd CH")
        powder_CHG_label.grid(column=4, row=0)
        powder_type_label = ttk.Label(self, text="Pwd")
        powder_type_label.grid(column=5, row=0)
        powder_vol_label = ttk.Label(self, text="Pwd Vol")
        powder_vol_label.grid(column=6, row=0)
        case_type_label = ttk.Label(self, text="Case")
        case_type_label.grid(column=7, row=0)
        case_length_label = ttk.Label(self, text="Length")
        case_length_label.grid(column=8, row=0)
        COAL_label = ttk.Label(self, text="COAL")
        COAL_label.grid(column=9, row=0)
        primer_label = ttk.Label(self, text="Primer")
        primer_label.grid(column=10, row=0)
        rounds_loaded_label = ttk.Label(self, text="Rounds")
        rounds_loaded_label.grid(column=11, row=0)
    #Form Input Boxes
        #Sets default current date
        to_day = datetime.datetime.now() # Retreve current date.
        self.date_box = ttk.Entry(self,width=10)
        self.date_box.grid(column=0, row=1)
        self.date_box.insert(0, to_day.strftime("%d%b%Y")) # Sets todays date as default entry
        self.caliber_box = ttk.Entry(self)
        self.caliber_box.grid(column=1, row=1)
        self.bullet_MFG_box = ttk.Entry(self, width=10)
        self.bullet_MFG_box.grid(column=2, row=1)
        self.bullet_type_box = ttk.Entry(self, width=10)
        self.bullet_type_box.grid(column=3, row=1)
        self.powder_CHG_box = ttk.Entry(self, width=6)
        self.powder_CHG_box.grid(column=4, row=1)
        self.powder_type_box = ttk.Entry(self,width=10)
        self.powder_type_box.grid(column=5, row=1)
        self.powder_volume_Box = ttk.Entry(self,width=6)
        self.powder_volume_Box.grid(column=6, row=1)
        self.case_type = ttk.Entry(self,width=10)
        self.case_type.grid(column=7, row=1)
        self.case_length_Box = ttk.Entry(self,width=5)
        self.case_length_Box.grid(column=8, row=1)
        self.COAL_box = ttk.Entry(self,width=10)
        self.COAL_box.grid(column=9, row=1)
        self.primer_box = ttk.Entry(self,width=7)
        self.primer_box.grid(column=10, row=1)
        self.rounds_loaded_Box = ttk.Entry(self,width=6)
        self.rounds_loaded_Box.grid(column=11, row=1)

    #Add our data to a class to retrieve latter.
    def Load_Data_Fetcher(self):
        date = self.date_box.get() 
        caliber = self.caliber_box.get()  
        bullet_mfg = self.bullet_MFG_box.get() 
        bullet_type = self.bullet_type_box.get()
        pwd_charge = self.powder_CHG_box.get()
        powder_type = self.powder_type_box.get() 
        powder_volume = self.powder_volume_Box.get() 
        case_type = self.case_type.get()
        case_length = self.case_length_Box.get()
        coal = self.COAL_box.get() 
        primer = self.primer_box.get()
        round_count = self.rounds_loaded_Box.get()
        return Current_Load_Data(date, caliber, bullet_mfg, bullet_type, pwd_charge, powder_type,
                                powder_volume, case_type, case_length, coal, primer, round_count)

    def Clear_Load_data(self):
        self.date_box.delete(0, tk.END)
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

class Counters(tk.LabelFrame):
    def __init__(self, master,):
        tk.LabelFrame.__init__(self, master, text="Counts")
        self.master = master
        round_counted = tk.LabelFrame(self, text="Rounds")
        counted_rounds = tk.Label(round_counted, text="100", background="white")
        counted_rounds.pack(fill="both")
        round_counted.grid(column=0, row=0)
        primer_counter = tk.LabelFrame(self, text="Primer")
        primers_counted = tk.Label(primer_counter, text="50", background="white")
        primers_counted.pack(fill="both")
        primer_counter.grid(column=1, row=0)
        primer_reset_button = ttk.Button(self,text="Primer")
        primer_reset_button.grid(column=1, row=1)
        case_reset_button = ttk.Button(self,text="Case")
        case_reset_button.grid(column=0, row=1)
       
class Logo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        #Path to logo depends on OS. Windows needs Relative path while Linux requres exact.
        #image = Image.open("/home/pi/Documents/Reloading-Press-Monitor-main/Testing_and Examples_Section/logo2.png")
        image = Image.open("GUI_Working/logo2.png")
        #Resize loaded image.
        image = image.resize((337, 75), Image.ANTIALIAS) ## The (450, 100) is (width, height) 
        render = ImageTk.PhotoImage(image)
        img = tk.Label(self, image=render)
        img.image = render #may seam silly... but this is so that the photo stays stored in memory, if not Python may trash it
        img.pack()

class Powder(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text="Powder Level")
        powder_level = tk.Label(self, text="50%")
        powder_level.pack(side ="bottom")
        bar = ttk.Progressbar(self, length=200)
        bar['value'] = 50
        bar.pack(side ="top")

class Cam_Control(tk.Frame):
    def __init__(self, master, cam1, cam2):
        tk.Frame.__init__(self, master)
        self.master = master
        self.cam1 = cam1
        self.cam2 = cam2
        cam1_btn = ttk.Button(self, text="Cam 1", command=self.cam1)
        cam1_btn.pack(side="left", padx=4, pady=4)
        cam2_btn = ttk.Button(self, text="Cam 2", command=self.cam2)
        cam2_btn.pack(side="left", padx=4, pady=4)

class Alarm (tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text="Cautions")
        self.master = master
        #These will display in the order written and aligned to the left.
    #Alerts
      #Low Primers
        low_primer_warning = ttk.LabelFrame(self, text="Primers")
        low_primer_warning.pack(side = "left")
        low_primer_label =  tk.Button(low_primer_warning, text="Alert", background="red", height=2, width=5, command= None)
        low_primer_label.pack(fill = "both") 
      #Binding
        binding_warning = ttk.LabelFrame(self, text="Binding")
        binding_warning.pack(side = "left") 
        binding_label = tk.Button(binding_warning, text="Alert", background="red", height=2, width=5)
        binding_label.pack(fill = "both")
      #Low Powder
        low_powder_warning = ttk.LabelFrame(self, text="Powder")
        low_powder_warning.pack(side = "left")
        low_powder_label = tk.Button(low_powder_warning, text="Alert", background="red", height=2, width=5)
        low_powder_label.pack(fill = "both")
      #Low Cases
        low_case_warning = ttk.LabelFrame(self, text="Case")
        low_case_warning.pack(side = "left")
        low_case_label = tk.Button(low_case_warning, text="Alert", background="red", height=2, width=5)
        low_case_label.pack(fill = "both")
      #Low Bullets
        low_bullet_warning = ttk.LabelFrame(self,text="Bullets")
        low_bullet_warning.pack(side = "left")
        low_bullet_label = tk.Button(low_bullet_warning, text="Alert", background="red", height=2, width=5)
        low_bullet_label.pack(fill = "both")

class Form_Control(tk.Frame):    
    def __init__(self, master, export, clear):
        tk.Frame.__init__(self, master)
        self.master = master
        self.export = export
        self.clear = clear
        self.clear_btn = ttk.Button(self, text="Clear", command=self.clear)
        self.clear_btn.pack(side="right", padx=4, pady=4)
        self.export_btn = ttk.Button(self, text="Export", command=self.export)
        self.export_btn.pack(side="right",padx=4, pady=4)
    
#Main Aplication Window to call in the classes
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AMMMO Computer")
        self.menubar = MenuBar(self, add_remove=self.Pet_Loads_Log)
        self.config(menu=self.menubar)
        
#Layout Notes to self:
        #App Frames for organization of layout so you can see where I am going with the layout.
        #Sub frames will be created before thier widget contents. pictures are worth 1000 words.
        #              /---------------------------------------/
        # First Frame  /        Welcome Message                /
        # Middle Cont. / /-----------------------------------/ /
        # Second Frame / /Counter    /  Logo   /  Powder Lvl / /
        #              / /----------//--------/-/------------/ /
        # Third Frame  / /Cam Button/ Cautions / Form Buttons/ /
        #              / /---------/----------/--------------/ /
        # Fourth Fram  / / / / / / /Form/ / / /  / / / /  /  / /
        #              /---------------------------------------/     
         
#First Frame: I like my computer to great me. Makes me feel needed.
        self.first_frame = tk.Frame(self)
        welcome = tk.Label(self.first_frame, text="Welcome Rcmaveric, lets make some ammo!")
        welcome.pack(fill="both")
        self.first_frame.grid(column=0, row= 0)
#Middle Container:
        self.middle_frame = tk.Frame(self)
  #Second Frame:  
    #Counter        
        self.counter_box = Counters(self.middle_frame)
        self.counter_box.grid(column=0, row=0)        
    #Logo
        self.picture = Logo(self.middle_frame)
        self.picture.grid(column=1, row=0)  
    #Powder Level
        level = Powder(self.middle_frame)
        level.grid(column=3, row=0)  
  #Third Frame
        self.cammy = Cam_Control(self.middle_frame, cam1=self.Cam1_Toggle, cam2=self.Cam2_Toggle)
        self.cammy.grid(column=0, row=1)  
        self.calls = Alarm(self.middle_frame)
        self.calls.grid(column=1, row=1)  
        self.formy = Form_Control(self.middle_frame, clear= lambda: self.forms.Clear_Load_data(), export= self.Write_To_File)
        self.formy.grid(column=3, row=1)  
        self.middle_frame.grid(column=0, row=3)
#Fourth Frame
        self.fourth_frame = tk.Frame(self)
        self.forms = FormBox(self.fourth_frame)
        self.forms.pack()
        self.fourth_frame.grid(column=0, row=4)
        
#Commands

    def Cam1_Toggle(self):
        self.camera1_window = tk.Toplevel(self)
        self.camera1 = Cam(self, window=self.camera1_window, window_title="Cam1", video_source=0)

    def Cam2_Toggle(self):
        self.camera2_window = tk.Toplevel(self)
        self.camera2 = Cam(self, window=self.camera2_window, window_title="Cam1", video_source=1)
  
    def Pet_Loads_Log(self):
        self.recipes_window = tk.Toplevel(self)
        self.recipe_editor = Recipe_Editor(self.recipes_window, window=self.recipes_window, window_title="Load Editor")

    def Write_To_File(self):
        load_data = self.forms.Load_Data_Fetcher()
        with open('Reloading_Log.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([load_data.date, load_data.caliber, load_data.bullet_mfg, load_data.bullet_type,
                        load_data.pwd_charge, load_data.powder_type, load_data.powder_volume, 
                        load_data.case_type, load_data.case_length, load_data.coal, load_data.primer, 
                        load_data.round_count])

if __name__ == "__main__":
    app=App()
    style = ThemedStyle()
    style.set_theme("breeze")
    app.mainloop()