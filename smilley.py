import time
from shifter import Shifter #from shifter.py import Shifter class. Extended by compositon




class LED8x8():
 
  pattern = [
    0b00111100, 
    0b01000010, 
    0b10100101, 
    0b10000001, 
    0b10100101, 
    0b10011001, 
    0b01000010, 
    0b00111100 ]

  #pattern=(~pattern & 0b11111111)



  '''col = [
    0b01111111,
    0b10111111,
    0b11011111,
    0b11101111,
    0b11110111,
    0b11111011,
    0b11111101,
    0b11111110]'''

  '''col =[
    0b11111110,
    0b11111101,
    0b11111011,
    0b11110111,
    0b11101111,
    0b11011111,
    0b10111111,
    0b01111111]'''
  col =[
    0b10000000,
    0b01000000,
    0b00100000,
    0b00010000,
    0b00001000,
    0b00000100,
    0b00000010,
    0b00000001]
    
  '''col = [
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000]'''
  '''col = [
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111]'''



  #'sequentially sends 8 pairs of bytes to a Shifter object'

  def __init__(self,data,latch,clock):  
    self.shifter=Shifter(data,latch,clock)
    
  def setPattern(self, num):
    self.shifter.shiftByte(~LED8x8.pattern[num] & 0b11111111)  #load the col values
    self.shifter.shiftByte( 1 << num )    #load the row values

    self.shifter.latch()

#to run this LED8x8(dataPin,latchPin,clockPin)