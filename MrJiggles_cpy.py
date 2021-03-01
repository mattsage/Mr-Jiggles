import time
import board
from digitalio import DigitalInOut, Direction, Pull
import time
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
btn = DigitalInOut(board.GP14)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN
i=0
on=False
def onRelease():

  bState=btn.value
  released=False
  if (bState):
    bState = btn.value
    while bState:
      bState = btn.value
      
return True;

while True:

  if onRelease():
    on=not on
  if on:
    mouse.move(5,5)
    time.sleep(0.1)
    mouse.move(-5,-5)
    time.sleep(0.1)
  time.sleep(0.1)
