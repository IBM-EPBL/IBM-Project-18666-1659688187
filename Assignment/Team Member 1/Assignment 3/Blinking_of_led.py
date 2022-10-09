
#project implementation - https://wokwi.com/projects/345069417333260883


#module for interfacing with the rasberrypi pico
from machine import Pin

#module for using sleep function(delay)
from time import sleep

#creating a new object "led" of class Pin
#led attributes
#pin number - 17; pin function - output
led = Pin(17, Pin.OUT)

#while function used as void loop to execute the function reaptedly
while True:
  led.value(1) # set the pin 17 to high
  sleep(1) #delay for 1 second
  led.value(0) #set the pin 17 to low
  sleep(1) #delay for 1 second
  
