
import  multiprocessing, time, random

from displayClass import LED8x8
import RPi.GPIO as GPIO #for cleanup()

dataPin, latchPin, clockPin = 23, 24, 25 #input data, send data, load data

theLED8x8= LED8x8(dataPin, latchPin, clockPin) #create object from led8x8 class

#define starting position for LED
numRow=1
numCol=1

theLED8x8.start() #only happens once!
while True:
 
  try:
    #RANDOM WALK:
    '''R=random.randint(-1, 1) # R can be -1, 0, or 1
    if 1<= numRow + R <=8: 
      numRow=numRow + R
    else:
      pass
    C=random.randint(-1, 1) # C can be -1, 0, or 1
    if 1<= numCol+ C <=8: 
      numCol=numCol + C
    else:
      pass''' #from V1
    #RANDOM WALK. not optimized for V2 but still will work:
    R=random.randint(-1, 1) # R can be -1, 0, or 1
    if 1 - 1<= numRow + R <=8 - 1: 
      numRow=numRow + R
    else:
      pass
    C=random.randint(-1, 1) # C can be -1, 0, or 1
    if 1 - 1 <= numCol+ C <= 8 - 1: 
      numCol=numCol + C
    else:
      pass
    
    #for loop to iterate through multiprocessing array
    for i in range(len(theLED8x8.pattern)):
      theLED8x8.pattern[i]=0b00000000

    theLED8x8.pattern[numRow] = 1 << numCol #throw a 1 into the array mix and move it around randomly
    time.sleep(0.1)


    theLED8x8.firefly(theLED8x8.pattern) #finally instantiating the method, being run by multiprocessing
    
    theLED8x8.daemon() ## Force process termination when main code ends
    #   (always 'join' after termination)
    theLED8x8.join()
    
    '''p = multiprocessing.Process(target=theLED8x8.firefly, args=(numRow,numCol,))
    p.daemon = True # Force process termination when main code ends
    p.start()        # Start the process (only once!)
    p.join()''' #from v1

  except KeyboardInterrupt:
    print("\nExiting!")
    p.terminate()    # Terminate the process (no equivalent for threads)
    #   (always 'join' after termination)
    p.join(2)        # Pause the calling process for up to n seconds to let
    #   the process to end, then join even if not ended
    GPIO.cleanup()
    break



