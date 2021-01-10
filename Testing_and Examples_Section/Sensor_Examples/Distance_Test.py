#!/usr/bin/python3
from gpiozero import DistanceSensor
from signal import pause
from time import sleep
import time

# alter if using a different pin
ultrasonic = DistanceSensor(echo=27, trigger=17)  

while True:
    print(ultrasonic.distance)
    print(ultrasonic.value)
    sleep(1)