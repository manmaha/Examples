#!/usr/bin/python

import Adafruit_DHT
import time

# Sensor should be set to Adafruit_DHT.DHT11,
sensor = Adafruit_DHT.DHT11


# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 23

while True:

 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 
 
 if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
 else:
  print('Failed to get reading. Try again!')
 time.sleep(10)
