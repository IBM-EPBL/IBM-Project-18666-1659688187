#module for interfacing with the rasberrypi pico
from machine import Pin

#module for using sleep function(delay)
from time import sleep

#creating a new object "led" of class Pin

#red_led attributes
#pin number - 17; pin function - output
red_led = Pin(17, Pin.OUT)

#yellow_led attributes
#pin number - 18; pin function - output
yellow_led = Pin(18, Pin.OUT)

#green_led attributes
#pin number - 19; pin function - output
green_led = Pin(19, Pin.OUT)

#while function used as void loop to execute the function reaptedly
while True:

  #stop signal - red glows
  print("Stop - red glows for 4 seconds")
  red_led.value(1)
  yellow_led.value(0)
  green_led.value(0)
  sleep(4)

  #Alert signal - yellow glows
  print("Alert - yellow glows for 1 second")
  red_led.value(0)
  yellow_led.value(1)
  green_led.value(0)
  sleep(1)

  #Go signal - green glows
  print("Go - Green glows for 3 seconds")
  red_led.value(0)
  yellow_led.value(0)
  green_led.value(1)
  sleep(3)
