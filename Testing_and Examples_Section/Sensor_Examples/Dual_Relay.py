'''
Author: Rcmaveric
IRL Name: Ryan Conner
Date: 06 Nov 202
'''

from gpiozero import LightSensor, OutputDevice
from time import sleep
import time

# alter if using a different pin
ldr1 = LightSensor(4)
ldr2 = LightSensor(19)

#If you relays operate backwards swap the active_high state (default is True).
#Setting initial_value to false ensures relays start closed enstead of current state.
relay1 = OutputDevice(6, initial_value=False, active_high=False)
relay2 = OutputDevice(12, initial_value=False, active_high=False)

#For relays to work correctly you have to tell the computer what to do for each possible condition of LDRs.

# For my reference: LDR1 and Relay1 are for cases.
#                   LDR2 and Relay2 are for cases.  
while True:
    sleep(.2)
    #print("LDR1 = "+str(ldr1.value)) #To view LDR1 output for trouble shooting.
    #print("LDR2 = "+str(ldr2.value)) #To view LDR2 output for trouble shooting.
    #Bullet Feeder
    if ldr1.value > .5 and ldr2.value < .5:
        sleep(.2)
        relay1.on()
        relay2.off()
    #Case Feeder
    if ldr1.value < .5 and ldr2.value > .5:
        sleep(.2)
        relay2.on()
        relay1.off()
    #Feed Cases and Bullets
    if ldr1.value > .5 and ldr2.value > .5:
        sleep(.2)
        relay1.on()
        relay2.on()
    #Otherwise all is off.
    if ldr1.value < .5 and ldr2.value < .5:
        relay1.off()
        relay2.off()
        sleep(.2)
