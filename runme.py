
import time
from smilley import LED8x8
import RPi.GPIO as GPIO #for cleanup()

dataPin, latchPin, clockPin = 23, 24, 25 #input data, send data, load data

theLED8x8= LED8x8(dataPin, latchPin, clockPin)

row = [
  0b10000000,
  0b01000000,
  0b00100000,
  0b00010000,
  0b00001000,
  0b00000100,
  0b00000010,
  0b00000001 ]
# Simple demonstration of the LED8x8 class.
# to define the GPIO pins, since LED8x8 is
# pin-agnostic).

while True:
  try:
    for n in range(len(row)):
      theLED8x8.setPattern(row(n))
      time.sleep(0.4)
  except KeyboardInterrupt:
    print("\nExiting!")
    GPIO.cleanup()
    break



