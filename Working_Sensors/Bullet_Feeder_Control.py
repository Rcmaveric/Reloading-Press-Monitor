from gpiozero import LightSensor, OutputDevice
from time import sleep
import time

# alter if using a different pin
ldr1 = LightSensor(4)
#ldr2 = LightSensor(19)

#If you relays operate backwards swap the active_high state (default is True). For some reason 
#relay 2 for me is backards. NC pshould have continuity when relay de-energized.
relay1 = OutputDevice(6, initial_value=False)
#relay2 = OutputDevice(12, initial_value=False, active_high=False)

#At this time I havent figured out how to make all relays work at once. That is in the works.

while True:
    sleep(.5)
    #print(ldr1.value) To test LDR if having problems
    #print(ldr2.value) 

#Bullet Feeder
    if ldr1.value > .5:
        relay1.on()

#Case Feeder
    #if ldr2.value > .5:
    #   relay2.on()

    else:
        relay1.off()
        #relay2.off()
        sleep(.2)
        