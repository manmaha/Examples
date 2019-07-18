import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

red = 14
yellow = 15
green = 18
GPIO.setup(red,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT) 
GPIO.setup(green,GPIO.OUT) 

GPIO.output(red,GPIO.HIGH)
time.sleep(3) 
GPIO.output(red,GPIO.LOW)
GPIO.output(yellow,GPIO.HIGH)
time.sleep(3) 
GPIO.output(yellow,GPIO.LOW)
time.sleep(3) 
GPIO.output(green,GPIO.HIGH)
time.sleep(3) 
GPIO.output(green,GPIO.LOW)