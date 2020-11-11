from tkinter import*
from tkinter.ttk import*
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle


'''
def clicked1():
    print"exported"

def clicked2():
    print "cleared"
'''

#Main Window
window = Tk()
window.title("Ammo Computer")
#window.geometry('1035x280')

#Camera Windows
#Cam1 = Toplevel()
#Cam2 = Toplevel()

# ttk based widgets can be themedc
style = ThemedStyle()
style.set_theme("breeze")

# Menu
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)


#####aligning it all with frames. Frames are containers.

#Main Window Frame
top_frame = Frame(window)
top_frame.grid(column=0, row=0)

#Camera Frames
#Cam1 = Toplevel()
#Cam2 = Toplevel()

#Top Frame which is welcome message
welcome = Label(top_frame, text="Welcome Rcmaveric, lets make some ammo!")
welcome.pack(fill = BOTH)


#Middle frame which is Counter, Logo, Powder Level aligning Box
Count_PWDLV_Box = Frame(window) 
Count_PWDLV_Box.grid(column=0, row=1)
###Counter, Logo, Powder Level aligning box sub level frames
# Round Counter box
Counter_box = LabelFrame(Count_PWDLV_Box, text="Counter")  #Main container inside upper level frame.
Counter_box.grid(column=0, row=0, padx=4, pady=10) # We want our counter first from left to right.
Round_Counted = LabelFrame(Counter_box, text="Rounds")
Round_Counted.grid(column=0, row=0)
counted_Rounds = Label(Round_Counted, text="100")
counted_Rounds.pack()
Primer_Counter = LabelFrame(Counter_box, text="Primer")
Primer_Counter.grid(column=1, row=0)
Primers_Counted = Label(Primer_Counter, text="50")
Primers_Counted.pack()
Primer_reset_button = Button(Counter_box,text="Primer")
Primer_reset_button.grid(column=1, row=1)
Case_reset_button = Button(Counter_box,text="Case")
Case_reset_button.grid(column=0, row=1)
pause_button = Button(Counter_box,text="Pause")
pause_button.grid(column=3, row=1)
#Logo
#path = 'C:\Users\rcmav\Dropbox\Reloading-Press-Monitor\GUI_Working\logo2.png' # Linux make sure image path is exact
path = 'GUI_Working\logo2.png' #Windows make sure image path is exact
img = ImageTk.PhotoImage(Image.open(path))
logo = Label(Count_PWDLV_Box, image = img)
logo.grid(column=1, row=0, padx=4, pady=10)

# Powder Level
Powder_Level_Info = LabelFrame(Count_PWDLV_Box, text="Powder Level")
Powder_Level_Info.grid(column=2, row=0, padx=4, pady=10)
Powder_Level = Label(Powder_Level_Info, text="50%")
Powder_Level.pack(side = BOTTOM, fill = Y)
bar = Progressbar(Powder_Level_Info, length=200)
bar['value'] = 50 #This will be the powerder
bar.pack(side = TOP)


#Middle Fram
middle_frame = Frame(window)
middle_frame.grid(column=0, row=3)
#CAPs Box (CAP stands for Cautions and Advisories)
Caps_box_Calls = LabelFrame(middle_frame, text="Cautions")
Caps_box_Calls.grid(column=2, row=0)

####Alerts
#These will display in the order written and aligned to the left.
Low_Primer_Warning = LabelFrame(Caps_box_Calls, text="Primers")
Low_Primer_Warning.pack(side = LEFT)
Low_Primer_Label =  Label(Low_Primer_Warning, text="Alert", background="red")
Low_Primer_Label.pack(fill = BOTH) 

Binding_Warning = LabelFrame(Caps_box_Calls, text="Binding")
Binding_Warning.pack(side = LEFT) 
Binding_Label = Label(Binding_Warning, text="Alert", background="red")
Binding_Label.pack(fill = BOTH)

Low_Powder_Warning = LabelFrame(Caps_box_Calls, text="Powder")
Low_Powder_Warning.pack(side = LEFT)
Low_Powder_Label = Label(Low_Powder_Warning, text="Alert", background="red")
Low_Powder_Label.pack(fill = BOTH)

Low_Case_Warning = LabelFrame(Caps_box_Calls, text="Case")
Low_Case_Warning.pack(side = LEFT)
Low_Case_Label = Label(Low_Case_Warning, text="Alert", background="red")
Low_Case_Label.pack(fill = BOTH)

Low_Bullet_Warning = LabelFrame(Caps_box_Calls,text="Bullets")
Low_Bullet_Warning.pack(side = LEFT)
Low_Bullet_Label = Label(Low_Bullet_Warning, text="Alert", background="red")
Low_Bullet_Label.pack(fill = BOTH)
#Buttons
Camera_Buttons = Frame(middle_frame)
Camera_Buttons.grid(column=0, row=0)
Form_Buttons = Frame(middle_frame)
Form_Buttons.grid(column=3, row=0) 
clear_btn = Button(Form_Buttons, text="Clear", command=None)
clear_btn.pack(side = RIGHT)
export_btn = Button(Form_Buttons, text="Export", command=None)
export_btn.pack(side = RIGHT)
cam1_btn = Button(Camera_Buttons, text="Cam 1", command=None)
cam1_btn.pack(side = LEFT)
cam2_btn = Button(Camera_Buttons, text="Cam 2", command=None)
cam2_btn.pack(side = LEFT)

#Form
Form_Box = LabelFrame(window, text="Reloading Log")
Form_Box.grid(column=0, row=4)
####Form Labels
Date_Label = Label(Form_Box, text="Date")
Date_Label.grid(column=0, row=3)
Caliber_Label = Label(Form_Box, text="Caliber")
Caliber_Label.grid(column=1, row=3)
BulletMFG_Label = Label(Form_Box, text="Bul MFG")
BulletMFG_Label.grid(column=2, row=3)
Buller_Type_Label = Label(Form_Box, text="Bul Type")
Buller_Type_Label.grid(column=3, row=3)
Powder_CHg_Label = Label(Form_Box, text="Pwd CH")
Powder_CHg_Label.grid(column=4, row=3)
Powder_Type_Label = Label(Form_Box, text="Pwd")
Powder_Type_Label.grid(column=5, row=3)
Powder_Volume_Label = Label(Form_Box, text="Pwd Vol")
Powder_Volume_Label.grid(column=6, row=3)
Case_TypeLabel = Label(Form_Box, text="Case")
Case_TypeLabel.grid(column=7, row=3)
Case_Legth_Label = Label(Form_Box, text="Length")
Case_Legth_Label.grid(column=8, row=3)
COAL_Box_Label = Label(Form_Box, text="COAL")
COAL_Box_Label.grid(column=9, row=3)
Primer_Label = Label(Form_Box, text="Primer")
Primer_Label.grid(column=10, row=3)
Rounds_Loaded_Label = Label(Form_Box, text="Rounds")
Rounds_Loaded_Label.grid(column=11, row=3)
########Form Input Boxes
Date_Box = Entry(Form_Box,width=10)
Date_Box.grid(column=0, row=4)
Caliber_Box = Entry(Form_Box,width=7)
Caliber_Box.grid(column=1, row=4)
BulletMFG_Box = Entry(Form_Box,width=10)
BulletMFG_Box.grid(column=2, row=4)
Buller_Type_Box = Entry(Form_Box, width=10)
Buller_Type_Box.grid(column=3, row=4)
Powder_CHg_Box = Entry(Form_Box, width=6)
Powder_CHg_Box.grid(column=4, row=4)
Powder_Type_Box = Entry(Form_Box,width=10)
Powder_Type_Box.grid(column=5, row=4)
Powder_Volume_Box = Entry(Form_Box,width=6)
Powder_Volume_Box.grid(column=6, row=4)
Case_Type = Entry(Form_Box,width=10)
Case_Type.grid(column=7, row=4)
Case_Legth_Box = Entry(Form_Box,width=5)
Case_Legth_Box.grid(column=8, row=4)
COAL_Box = Entry(Form_Box,width=10)
COAL_Box.grid(column=9, row=4)
Primer_Box = Entry(Form_Box,width=7)
Primer_Box.grid(column=10, row=4)
Rounds_Loaded_Box = Entry(Form_Box,width=6)
Rounds_Loaded_Box.grid(column=11, row=4)

window.mainloop()