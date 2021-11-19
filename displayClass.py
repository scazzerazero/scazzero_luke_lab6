import multiprocessing, time
from shifterClass import Shifter #from shifter.py import Shifter class. Extended by compositon
import random



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
  row = [
    0b10000000,
    0b01000000,
    0b00100000,
    0b00010000,
    0b00001000,
    0b00000100,
    0b00000010,
    0b00000001
  ]
 
  numRow=6
  numCol=8

  #'sequentially sends 8 pairs of bytes to a Shifter object'

  def __init__(self,data,latch,clock):  
    self.shifter=Shifter(data,latch,clock)
    #in order to get a separate process to launch as soon as LED8x8 class is instantiated

#if i use multiprocessing.array then. initiating 8 arrays. each time you run it updates your 8 arrays based on whatever x and y youre using. Next array will come by changing row[]. 

  def firefly(self):
    # change by adding random number between -1 and 1. IF statement to restrict to boundaries to 8.

    
    '''R=random.randint(-1, 1) # x can be -1, 0, or 1
    #print("R random= "+str(R))
    if 1<= LED8x8.numRow + R <=8: 
      numRow=LED8x8.numRow + R
    else:
      pass
    C=random.randint(-1, 1) # x can be -1, 0, or 1
    #print("C random= "+str(C))
    #print("")
    if 1<= LED8x8.numCol+ C <=8: 
      numCol=LED8x8.numCol + C
    else:
      pass'''

    numCol=LED8x8.numCol +2
    numRow=LED8x8.numRow +1

    self.shifter.shiftByte(~LED8x8.row[numRow-1]) #load col values
    self.shifter.shiftByte(LED8x8.row[numCol-1]) #load row values
    self.shifter.latch() #send to output

    time.sleep(1)

    
    
  def setPattern(self, num):
    #self.shifter.shiftByte(~LED8x8.pattern[num] & 0b11111111)  #load the col values
    self.shifter.shiftByte(~LED8x8.pattern[num] & 0b11111111)  #load the col values
    self.shifter.shiftByte( 1 << num )    #load the row values 0b00000001, then 0b00000010, etc...
    self.shifter.latch()

#to run this LED8x8(dataPin,latchPin,clockPin)