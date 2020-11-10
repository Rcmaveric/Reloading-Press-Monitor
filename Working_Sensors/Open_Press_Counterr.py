#Things we need
from gpiozero import Button, PWMOutputDevice, Buzzer
from signal import pause
from time import sleep

#Hardware Variable names, always match to schematic
S1 = Button(25)
S2 = Button(8)
S3 = Button(7)
M1 = PWMOutputDevice(16, frequency=400)
M2 = PWMOutputDevice(13, frequency=400)

#soft variables
clicks = 0 #Round Counter
clicks2 = 100 #Primer Counter

#functions    
def number():
    global clicks
    clicks += 1
    print(clicks)

def number2():
    global clicks2
    clicks2 -= 1
    print(clicks2)


#script   
while True:
    if S1.is_pressed:
        sleep(.5)
        #Trigers Motor to alternate pulses
        M1.pulse(n=1)
        sleep(.5)
        M2.pulse(n=1)
        #Triggers Count
        number()
        number2()
    #Resets round Counter to Zero
    elif S2.is_pressed:
        sleep(.5)
        clicks = 0
    elif S3.is_pressed:
        sleep(.5)
        clicks2 = 100    

pause()