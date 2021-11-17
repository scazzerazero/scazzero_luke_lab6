
import time
from smilley import LED8x8
import RPi.GPIO as GPIO #for cleanup()

dataPin, latchPin, clockPin = 23, 24, 25 #input data, send data, load data

theLED8x8= LED8x8(dataPin, latchPin, clockPin)

row = [0,1,2,3,4,5,6,7]
# Simple demonstration of the LED8x8 class.
# to define the GPIO pins, since LED8x8 is
# pin-agnostic).

while True:
  try:
    for n in range(8):
      theLED8x8.setPattern(n)
      time.sleep(0.01)
  except KeyboardInterrupt:
    print("\nExiting!")
    GPIO.cleanup()
    break



