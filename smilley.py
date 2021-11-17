import RPi.GPIO as GPIO #for cleanup()
import time
from shifter import Shifter #from shifter.py import Shifter class

 
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
row_I = [0b10000000,0b01000000,0b00100000,0b00010000,0b00001000,0b00000100,0b00000010,0b00000001]
class LED8x8():
  'sequentially sends 8 pairs of bytes to a Shifter object'

  def __init__(self,data,latch,clock):  
    self.shifter=Shifter(data,latch,clock)
    
  def display(self, pattern):
    while True:
      try:
        for idx in range(8):
          self.Shifter.shiftByte(pattern[idx]) #shiftByte acceprts a byte
          self.Shifter.shiftByte(row_I[idx])
          time.sleep(0.01)
      except KeyboardInterrupt:
        print("\nExiting!")
        GPIO.cleanup()
        break

#to run this LED8x8(dataPin,latchPin,clockPin)