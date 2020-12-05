import gpiozero as gp
import tkinter as tk
import time
from tkinter import ttk
import threading


Ldr3 = gp.LightSensor(26) #Case Feeder
Buzzer = gp.PWMOutputDevice(18, frequency=6000)
Relay2 = gp.OutputDevice(12, initial_value=False, active_high=True)#Cases

class Alarm (tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text="Cautions")
        self.master = master
    #Alerts
      #Low Cases
        low_case_warning = ttk.LabelFrame(self, text="Bullets")
        low_case_warning.pack(side = "left")
        self.low_case_label = tk.Button(low_case_warning, command = self.Low_Cases_Reset,
                                        text="Good", background="green", 
                                        height=2, width=5)
        self.low_case_label.pack(fill = "both")
        Relay2.source = Ldr3
       #Threads
        self.T1 = threading.Thread(target=self.Low_Cases, daemon=True)
        self.T1.start()
                
    def Low_Cases(self): #Currently Works if thread is a daemon.
        while True:
            pulsetime = 15
            Ldr3.wait_for_light()
            time.sleep(0.2)
            while Ldr3.light_detected == True:
                if pulsetime <= -1: #Without this the threads wouldn't idle and release lock
                    pass
                if pulsetime >= 0:
                    time.sleep(0.2)
                    pulsetime -= 1
                    print ("Case Timer = " + str(pulsetime))
                    if pulsetime <= 0:
                        self.low_case_label.configure(bg="red", text = "Alert")
                        Buzzer.pulse()
                    if Ldr3.light_detected == False: 
                        pass
    

    def Low_Cases_Reset(self):
        Buzzer.off()
        self.low_case_label.configure(bg="green", text = "Good")
   
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AMMMO Computer")
        self.calls = Alarm(self)
        self.calls.pack()

if __name__ == "__main__":
    app=App()
    app.mainloop()