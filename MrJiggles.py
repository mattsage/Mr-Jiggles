#https://pyautogui.readthedocs.io/en/latest/index.html
import pyautogui
import time

print("Mr Jiggles")
print("+------------+")
print("|            |")
print("| +---+      |")
print("| |   | +--+ |")
print("| |   | |  | |")
print("| +---+ +--+ |")
print("|            |")
print("| X        X |")
print("| X       XX |")
print("| XX      X  |")
print("|  XXXXXXXX  |")
print("|            |")
print("|            |")
print("+-----X------+")
print("      X")
print("      X")
print("     XX")
print("     X")
print("   +---+")
print("   |   |")
print("   |   |")
print("   +---+")

print("Jiggly Wiggly!")
#confirm(text='', title='', buttons=['OK', 'Cancel'])
#set pyautogui.FAILSAFE
while True: #Infinate Loop
	pyautogui.move(1,0) #move mouse 1pxl
	pyautogui.move(-1,0)
        time.sleep(180)
#	pyautogui.typewrite('Hello world!\n', interval=0.2)  #Enter text
#	pyautogui.PAUSE = 1.0
#	pyautogui.keyDown('f15') #Keyboard Press
#	pyautogui.keyUp('f15') #Keyboard Release
