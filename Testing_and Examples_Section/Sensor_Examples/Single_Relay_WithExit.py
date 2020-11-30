from gpiozero import LightSensor, OutputDevice
from time import sleep
import time
import os

# alter if using a different pin
ldr1 = LightSensor(4)
#ldr2 = LightSensor(19)

#If you relays operate backwards swap the active_high state (default is True).
relay1 = OutputDevice(6, initial_value=False, active_high=True)
#relay2 = OutputDevice(12, initial_value=False, active_high=False)

while True:
    try:
        sleep(.2)
        if ldr1.value > .5:
            relay1.on()
        else:
            relay1.off()
    except KeyboardInterrupt:
        print('Goodbye!')
        break
