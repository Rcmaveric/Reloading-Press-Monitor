from gpiozero import LightSensor
from signal import pause
from time import sleep
import time

# alter if using a different pin
ldr1 = LightSensor(4)
ldr2 = LightSensor(19)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
ldr3 = LightSensor(26) 

while True:
    sleep(.4)
    print("LDR1 = "+str(ldr1.value))
    sleep(.5)
    print("LDR2 = "+str(ldr2.value))
    sleep(.5)
    print("LDR3 = "+str(ldr3.value))