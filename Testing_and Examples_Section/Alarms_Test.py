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
        low_bullet_label = tk.Button(low_bullet_warning, text="Good", background="green", height=2,
                                     width=5, command = self.Low_Bullet_Reset)
        low_bullet_label.pack(fill = "both")
        Relay1.source = Ldr2

      #Low Primers
        low_primer_warning = ttk.LabelFrame(self, text="Primers")
        low_primer_warning.pack(side = "left")
        self.low_primer_label =  tk.Button(low_primer_warning, text="Good", background="green",
                                            height=2, width=5, command= self.Low_Primer_Reset)
        self.low_primer_label.pack(fill = "both")
        Ldr1.when_light= self.Low_Primer_Alert

      #Low Cases
        low_case_warning = ttk.LabelFrame(self, text="Bullets")
        low_case_warning.pack(side = "left")
        self.low_case_label = tk.Button(low_case_warning, command = self.Low_Cases_Reset,
                                        text="Good", background="green", 
                                        height=2, width=5)
        self.low_case_label.pack(fill = "both")
        Relay2.source = Ldr3
        self.T1 = threading.Thread(target=self.Low_Cases, daemon=True)
        self.T1.start()

    def Low_Cases(self): #Works But doesnt quit thread when exiting main loop
        while True:
            pulsetime = 0
            Ldr3.wait_for_light()
            time.sleep(0.1)
            while Ldr3.light_detected == True:
                time.sleep(0.2)
                pulsetime += 1
                print ("Case Timer = " + str(pulsetime))
                if pulsetime >= 15:
                    self.low_case_label.configure(bg="red", text = "Alert")
                    Buzzer.pulse(n=1)
                if Ldr3.light_detected == False:
                    pass
    
    def Low_Primer_Alert(self):
        startTime = time.time()
        if Ldr1.light_detected == True:
            endTime = time.time()
            if (endTime - startTime > 3):
                Buzzer.pulse()
                self.low_primer_label.configure(bg="red", text = "Alert")
                print("Low Primers")
        
    def Low_Cases_Reset(self):
        Buzzer.off()
        self.low_case_label.configure(bg="green", text = "Good")
    
    def Low_Primer_Reset(self):
        self.low_primer_label.configure(bg="green", text = "Good")
        Buzzer.off()
        
    def Low_Bullet_Reset(self):
        self.low_bullet_label.configure(bg="green", text = "Good")
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
    