#Flash led

import RPi.GPIO as GPIO
import time

Leds = [2,4,7,19,26,23,8,16,20,21,10,12,27,22,13,9,18,24]
GPIO.setmode(GPIO.BCM) 
GPIO.setup(Leds,GPIO.OUT) 

#set LEDs to flash forever
while True:
 for led in Leds:
  GPIO.output(led,GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(led,GPIO.LOW)
  