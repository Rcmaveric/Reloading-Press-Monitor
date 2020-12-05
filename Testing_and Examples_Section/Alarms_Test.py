import gpiozero as gp
import tkinter as tk
import time
from tkinter import ttk
import threading


S4 = gp.Button(24) #Binding Sensor
Ldr1 = gp.LightSensor(4) #Low Primer
Ldr2 = gp.LightSensor(19) #Bullet Feeder 
Ldr3 = gp.LightSensor(26) #Case Feeder
Buzzer = gp.PWMOutputDevice(18, frequency=6000)
Relay1 = gp.OutputDevice(6, initial_value=False, active_high=True)#Bullets
Relay2 = gp.OutputDevice(12, initial_value=False, active_high=True)#Cases

class Alarm (tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text="Cautions")
        self.master = master
        
     #Alerts
      #Low Bullets
        low_bullet_warning = ttk.LabelFrame(self,text="Bullets")
        low_bullet_warning.pack(side = "left")
        self.low_bullet_label = tk.Button(low_bullet_warning, text="Good", background="green", height=2,
                                     width=5, command = self.Low_Bullet_Reset)
        self.low_bullet_label.pack(fill = "both")
        Relay1.source = Ldr2
      #Low Primers
        low_primer_warning = ttk.LabelFrame(self, text="Primers")
        low_primer_warning.pack(side = "left")
        self.low_primer_label =  tk.Button(low_primer_warning, text="Good", background="green",
                                            height=2, width=5, command= self.Low_Primer_Reset)
        self.low_primer_label.pack(fill = "both")
      #Low Cases
        low_case_warning = ttk.LabelFrame(self, text="Bullets")
        low_case_warning.pack(side = "left")
        self.low_case_label = tk.Button(low_case_warning, command = self.Low_Cases_Reset,
                                        text="Good", background="green", 
                                        height=2, width=5)
        self.low_case_label.pack(fill = "both")
        Relay2.source = Ldr3
      #Binding
        binding_warning = ttk.LabelFrame(self, text="Binding")
        binding_warning.pack(side = "left") 
        self.binding_label = tk.Button(binding_warning, text="Good", background="green",
                                  height=2, width=5, command=self.Is_Bound_Reset)
        self.binding_label.pack(fill = "both")
      #Low Powder
        low_powder_warning = ttk.LabelFrame(self, text="Powder")
        low_powder_warning.pack(side = "left")
        low_powder_label = tk.Button(low_powder_warning, text="Good",
                                     background="green", height=2, width=5)
        low_powder_label.pack(fill = "both")

     #Threads
        self.T1 = threading.Thread(target=self.Low_Cases, daemon=True)
        self.T1.start()
        self.T2 = threading.Thread(target=self.Low_Primers, daemon=True)
        self.T2.start()
        self.T3 = threading.Thread(target=self.Low_Bullets, daemon=True)
        self.T3.start()
        self.T4 = threading.Thread(target=self.Is_Bound, daemon=True)
        self.T4.start()
    def Low_Cases(self): #Currently Works if thread is a daemon.
        while True:
            pulsetime = 0
            Ldr3.wait_for_light()
            time.sleep(0.2)
            while Ldr3.light_detected == True:
                time.sleep(0.2)
                pulsetime += 1
                print ("Case Timer = " + str(pulsetime))
                if pulsetime >= 15:
                    self.low_case_label.configure(bg="red", text = "Alert")
                    Buzzer.pulse(n=1)
                if Ldr3.light_detected == False: 
                    pass
    
    def Low_Bullets(self): #Currently Works if thread is a daemon.
        while True:
            pulsetime = 0
            Ldr2.wait_for_light()
            time.sleep(0.2)
            while Ldr2.light_detected == True:
                time.sleep(0.2)
                pulsetime += 1
                print ("Bullets Timer = " + str(pulsetime))
                if pulsetime >= 15:
                    self.low_bullet_label.configure(bg="red", text = "Alert")
                    Buzzer.pulse(n=1)
                if Ldr3.light_detected == False: 
                    pass

    def Low_Primers(self): #Currently Works if thread is a daemon.
        while True:
            pulsetime = 0
            Ldr1.wait_for_light()
            time.sleep(0.2)
            while Ldr1.light_detected == True:
                time.sleep(0.2)
                pulsetime += 1
                print ("Primers Timer = " + str(pulsetime))
                if pulsetime >= 3:
                    self.low_primer_label.configure(bg="red", text = "Alert")
                    Buzzer.pulse(n=1)
                if Ldr3.light_detected == False: 
                    pass            
    
    def Is_Bound(self): #Currently Works if thread is a daemon.
        while True:
            pulsetime = 0
            S4.wait_for_press() #Written backwards for testing
            time.sleep(0.2)
            while S4.is_pressed == True: #Written backwards for testing
                time.sleep(0.2)
                pulsetime += 1
                print ("Bind Timer = " + str(pulsetime))
                if pulsetime >= 15:
                    self.binding_label.configure(bg="red", text = "Alert")
                    Buzzer.pulse(n=1)
                if S4.is_pressed == False: #Written backwards for testing
                    pass          
    
    def Low_Powder(self): #No Distance sensor at the moment
       pass        
        
    def Low_Cases_Reset(self):
        Buzzer.off()
        self.low_case_label.configure(bg="green", text = "Good")
    
    def Low_Primer_Reset(self):
        self.low_primer_label.configure(bg="green", text = "Good")
        Buzzer.off()
        
    def Low_Bullet_Reset(self):
        self.low_bullet_label.configure(bg="green", text = "Good")
        Buzzer.off()

    def Is_Bound_Reset(self):
        self.binding_label.configure(bg="green", text = "Good")
        Buzzer.off()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AMMMO Computer")
        self.calls = Alarm(self)
        self.calls.pack()


if __name__ == "__main__":
    app=App()
    app.mainloop()