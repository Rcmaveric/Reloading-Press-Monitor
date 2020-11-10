from gpiozero import LightSensor, PWMOutputDevice, LED
from signal import pause
from time import sleep
import time

# alter if using a different pin
ldr = LightSensor(4)  
# For Passive buzzers, little buzzer best at 2500HZ, Larger 3000hz
#buzzer = PWMOutputDevice(23, frequency=2500)
buzzer = PWMOutputDevice(18, frequency=3000)
led2 = LED(24)

startTime = time.time()

while True:
    if ldr.value > .8:
        endTime = time.time()
        #LDR.value has to be above .8 for 3 seconds to sound alarm. This prevents false alarms during primer feading.
        if (endTime - startTime > 3):
            sleep(.2)
            buzzer.pulse(n=1)
            print("Low Primers")
            led2.on() #visual que to help debug.
    else:
        sleep(.2)
        led2.off()
        buzzer.off()