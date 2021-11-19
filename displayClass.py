import multiprocessing, time
from shifterClass import Shifter #from shifter.py import Shifter class. Extended by compositon
import random



class LED8x8(multiprocessing.Process):
 
  pattern = [ #used for smiley
    0b00111100, 
    0b01000010, 
    0b10100101, 
    0b10000001, 
    0b10100101, 
    0b10011001, 
    0b01000010, 
    0b00111100 ]

  row = [ #used for version1 (V1)
    0b10000000,
    0b01000000,
    0b00100000,
    0b00010000,
    0b00001000,
    0b00000100,
    0b00000010,
    0b00000001
  ]


#Notes from TA: if i use multiprocessing.array then. initiating 8 arrays. each time you run it updates your 8 arrays based on whatever x and y youre using. Next array will come by changing row[]. 
  pattern = multiprocessing.Array('i',8) 
  #define 8 patterns. multiprocessing will update and use these.
  pattern[0] = 0b00000000
  pattern[1] = 0b00000000
  pattern[2] = 0b00000000
  pattern[3] = 0b00000000
  pattern[4] = 0b00000000
  pattern[5] = 0b00000000
  pattern[6] = 0b00000000
  pattern[7] = 0b00000000

 


  #'sequentially sends 8 pairs of bytes to a Shifter object'

  def __init__(self,data,latch,clock):  
    multiprocessing.Process.__init__(self, name=LED8x8) #in order to get a separate process to launch as soon as LED8x8 class is instantiated
    self.shifter=Shifter(data,latch,clock)


  '''def firefly(self,numRow,numCol): #will light up a single value given the x,y coord. From v1
      self.shifter.shiftByte(~LED8x8.row[numRow-1]) #load col values
      self.shifter.shiftByte(LED8x8.row[numCol-1]) #load row values
      self.shifter.latch() #send to output
      time.sleep(0.10)''' #from V1
  def firefly(self, pattern):
    for num in range(8):
      self.shifter.shiftByte(~LED8x8.pattern[num]) #load col values
      self.shifter.shiftByte(1<<num) #load row values
      self.shifter.latch() #send to output
      time.sleep(0.0010)

    
    
  def setPattern(self, num): #used for smiley
    self.shifter.shiftByte(~LED8x8.pattern[num] & 0b11111111)  #load the col values
    self.shifter.shiftByte( 1 << num )    #load the row values 0b00000001, then 0b00000010, etc...
    self.shifter.latch()

