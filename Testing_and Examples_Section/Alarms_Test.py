import gpiozero as gp
import tkinter as tk
import time
from tkinter import ttk


S4 = gp.Button(24) #Binding Sensor
Ldr3 = gp.LightSensor(19) #Case Feeder 
Buzzer = gp.PWMOutputDevice(18, frequency=6000)
Relay2 = gp.OutputDevice(6, initial_value=False, active_high=True)

class Alarm (tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text="Cautions")
        self.master = master
        
    #Alerts
      #Binding
        binding_warning = ttk.LabelFrame(self, text="Binding")
        binding_warning.pack(side = "left") 
        binding_label = tk.Button(binding_warning, text="Good", background="green", height=2, width=5)
        binding_label.pack(fill = "both")

      #Low Cases
        low_case_warning = ttk.LabelFrame(self, text="Bullets")
        low_case_warning.pack(side = "left")
        self.low_case_label = tk.Button(low_case_warning, command = self.Low_Cases_Reset,
                                        text="Good", background="green", 
                                        height=2, width=5)
        self.low_case_label.pack(fill = "both")
        Relay2.source = Ldr3
        

    def Low_Cases(self): #Doesnt work.
        while True:
            pulsetime = 0
            Ldr3.wait_for_light()
            time.sleep(0.1)
            while Ldr3.light_detected == True:
                time.sleep(0.2)
                pulsetime += 1
                print (pulsetime)
                if pulsetime >= 15:
                    Buzzer.pulse()
                    self.low_case_label.configure(bg="red", text = "Alert")
        
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
    