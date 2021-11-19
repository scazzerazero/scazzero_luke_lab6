
import  multiprocessing, time

from displayClass import LED8x8
import RPi.GPIO as GPIO #for cleanup()

dataPin, latchPin, clockPin = 23, 24, 25 #input data, send data, load data

theLED8x8= LED8x8(dataPin, latchPin, clockPin) #create object from led8x8 class

# Simple demonstration of the LED8x8 class.
# to define the GPIO pins, since LED8x8 is
# pin-agnostic).

while True:
  try:
    p = multiprocessing.Process(target=theLED8x8.firefly)
    p.start()        # Start the process (only once!)



  except Exception as e:
    p.daemon = True # Force process termination when main code ends
    print("\nExiting!")
    print(e)
    p.terminate()    # Terminate the process (no equivalent for threads)
    #   (always 'join' after termination)
    p.join(2)        # Pause the calling process for up to n seconds to let
    #   the process to end, then join even if not ended
    GPIO.cleanup()
    break



