import gpiozero as gp
import tkinter as tk
import time
from tkinter import ttk


S4 = gp.Button(24) #Binding Sensor
Ldr3 = gp.LightSensor(19) #Case Feeder 
Buzzer = gp.PWMOutputDevice(18, frequency=6000)
Relay2 = gp.OutputDevice(6, initial_value=False, active_high=True)

Relay2.source = Ldr3

while True:
    pulsetime = 0
    Ldr3.wait_for_light()
    time.sleep(0.1)
    while Ldr3.light_detected == True:
        time.sleep(0.2)
        pulsetime += 1
        print (pulsetime)
        if pulsetime >= 15:
            Buzzer.pulse(n=1)
        if Ldr3.light_detected == False:
            Buzzer.off()
       