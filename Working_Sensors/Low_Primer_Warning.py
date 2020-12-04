from gpiozero import LightSensor, PWMOutputDevice, LED, OutputDevice
from signal import pause
from time import sleep
import time

# alter if using a different pin
ldr = LightSensor(4)  
buzzer = PWMOutputDevice(18, frequency=6000, active_high=True)



startTime = time.time()

while True:
    if ldr.value > .8:
        endTime = time.time()
        #LDR.value has to be above .8 for 3 seconds to sound alarm. This prevents false alarms during primer feading.
        if (endTime - startTime > 1):
            sleep(.2)
            buzzer.pulse(n=1)
            print("Low Cases")
            #led2.on() #visual que to help debug.
    else:
        sleep(.2)
        #led2.off()
        buzzer.off()
        startTime = time.time()