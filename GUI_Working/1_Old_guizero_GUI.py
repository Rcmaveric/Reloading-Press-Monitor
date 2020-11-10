#!/usr/bin/python3
from guizero import App, Text, PushButton, TextBox, Box, Picture, Window, MenuBar, Picture
from tkinter.ttk import Progressbar
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#Menu Bar Functions
def cam1_function():
    print("Cam1")

def cam2_function():
    print("Cam2")

def cal_function():
    print("Cal")

#Maint App windows and Camera windows
app = App(title="Ammo Computer", width=1035, height=280)
Cam1 = Window(app, title="Cam1", height=350, width=500) 
Cam2 = Window(app, title="Cam2", height=350, width=500)

### Camera feed
#Windows uses relative path while Linux needs exact path
cam_feed1 = Picture(Cam1, image="/home/pi/Documents/Reloading-Press-Monitor-main/GUI_Working/primer.jpg")
cam_feed2 = Picture(Cam2, image="/home/pi/Documents/Reloading-Press-Monitor-main/GUI_Working/primer.png")
#cam_feed1 = Picture(Cam1, image="GUI/primer.jpg")
#cam_feed2 = Picture(Cam2, image="GUI/primer.png")

# Tkinter based widgets can be themed
ttk.Style().theme_use('clam')

#Menu Bar
menubar = MenuBar(app,
                  toplevel=["Cams", "Cal"],
                  options=[
                      [ ["Cams option 1", cam1_function], ["Cams option 2", cam2_function] ],
                      [ ["Cal option 1", cal_function], ["Cal option 2", cal_function] ]
                  ])

#Layout will Be grid[row, col]
#Top
Welcome_box = Box(app, align="top")
message = Text(Welcome_box, text="Welcome Rcmaveric, Lets make ammo!")

# Counter, Logo, Powder Level aligning Box
Count_PWDLV_Box = Box(app, border=False, width="fill", align="top", layout="grid")

# Round Counter box
Counter_box = Box(Count_PWDLV_Box, layout="grid", grid=[0,0], width="fill")
count_label = Text(Counter_box, text="Rounds", grid=[0,0], align="left")
Round_Counted = Box(Counter_box,border=True,grid=[0,1], align="left")
counted_Rounds = Text(Round_Counted, text="100")
Primer_Label = Text(Counter_box,text="Primers",grid=[1,0], align="left")
Primer_Counter = Box(Counter_box,border=True,grid=[1,1], align="left")
Primers_Counted = Text(Primer_Counter, text="50")
Primer_reset_button = PushButton(Counter_box,text="Primer",grid=[2,1], align="left")
Case_reset_button = PushButton(Counter_box,text="Case",grid=[3,1], align="left")
pause_button = PushButton(Counter_box,text="Pause",grid=[4,1], align="left")

#Logo
logo = Picture(Count_PWDLV_Box, image="/home/pi/Documents/Reloading-Press-Monitor-main/GUI_Working/logo2.png",height=100, width=450, grid=[1,0])

# add a progress bar to the box
Powder_Level_Info = Box(Count_PWDLV_Box, border=False, grid=[2,0],height="fill", width="fill")
PWD_Level_Label = Text(Powder_Level_Info, text="Powder Level!", width="fill", align="top")
Pow_Level_Progress = Box(Powder_Level_Info, border=True, width="fill")
Powder_Level = Text(Powder_Level_Info, text="95%", width="fill", align="bottom")
pb = Progressbar(Pow_Level_Progress.tk)
Pow_Level_Progress.add_tk_widget(pb)
pb.start()

#Caps BOX
Caps_box = Box(app,border=False, height="fill", width="fill")
Caps_box_box = Box(Caps_box, border=False, width="fill", align="top")
Caps_Box_title = Text(Caps_box_box, text="Cuations and Advisorys")
Caps_box_Calls = Box(Caps_box, border=False, width="fill", align="bottom", height="fill")

####Alerts
Low_Primer_Warning = Box(Caps_box_Calls , border=True, width="fill", height="fill", align="left")
Low_Primer_Label =  Text(Low_Primer_Warning,bg=(255,0,0), text="Low Primer!", width="fill", height="fill") 
Binding_Warning = Box(Caps_box_Calls , border=True,height="fill", width="fill", align="left")
Binding_Label = Text(Binding_Warning, bg=(255,0,0), text="Binding!", width="fill", height="fill")
Low_Powder_Warning = Box(Caps_box_Calls , border=True, height="fill", width="fill", align="left")
Low_Powder_Label = Text(Low_Powder_Warning, bg=(255,0,0), text="Low Powder!", width="fill", height="fill")
Low_Case_Warning = Box(Caps_box_Calls , border=True, height="fill", width="fill", align="left")
Low_Case_Label = Text(Low_Case_Warning, bg=(255,0,0), text="Low Case!", width="fill", height="fill")
Low_Bullet_Warning = Box(Caps_box_Calls , border=True, height="fill", width="fill", align="left")
Low_Bullet_Label = Text(Low_Bullet_Warning, bg=(255,0,0), text="Low Bullets", width="fill", height="fill")
#Bottom
Form_Box = Box(app, border=False, align="bottom", layout="grid")
####Form Labels
Date_Label = Text(Form_Box, text="Date", grid=[0,0])
Caliber_Label = Text(Form_Box, text="Caliber", grid=[1,0])
BulletMFG_Label = Text(Form_Box, text="Bul MFG", grid=[2,0])
Buller_Type_Label = Text(Form_Box, text="Bul Type", grid=[3,0])
Powder_CHg_Label = Text(Form_Box, text="Pwd CH", grid=[4,0])
Powder_Type_Label = Text(Form_Box, text="Pwd", grid=[5,0])
Powder_Volume_Label = Text(Form_Box, text="Wwd Vol", grid=[6,0])
Case_TypeLabel = Text(Form_Box, text="Case", grid=[7,0])
Case_Legth_Label = Text(Form_Box, text="Length", grid=[8,0])
COAL_BoxLabel = Text(Form_Box, text="COAL", grid=[9,0])
Primer_Label = Text(Form_Box, text="Primer", grid=[10,0])
Rounds_Loaded_Label = Text(Form_Box, text="Rounds", grid=[11,0])
########Form Input Boxes
Date_Box = TextBox(Form_Box, text="27 Oct 20", grid=[0,1])
Caliber_Box = TextBox(Form_Box, text="270 Win", grid=[1,1])
BulletMFG_Box = TextBox(Form_Box, text="Cast", grid=[2,1])
Buller_Type_Box = TextBox(Form_Box, text="Lee PC RNFP", grid=[3,1])
Powder_CHg_Box = TextBox(Form_Box, text="17.4 G", grid=[4,1])
Powder_Type_Box = TextBox(Form_Box, text="4198", grid=[5,1])
Powder_Volume_Box = TextBox(Form_Box, text="4 CC", grid=[6,1])
Case_Type = TextBox(Form_Box, text="RP", grid=[7,1])
Case_Legth_Box = TextBox(Form_Box, text="2.53 IN", grid=[8,1])
COAL_Box = TextBox(Form_Box, text="3.3 IN", grid=[9,1])
Primer_Box = TextBox(Form_Box, text="WLR", grid=[10,1])
Rounds_Loaded_Box = TextBox(Form_Box, text="200", grid=[11,1])
############Buttons
Clear_Form = PushButton(Form_Box,text="Clear", grid=[0,2])
Export_Form = PushButton(Form_Box,text="Export", grid=[1,2])

app.display()