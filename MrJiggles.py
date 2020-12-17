#https://pyautogui.readthedocs.io/en/latest/index.html
import pyautogui
import time
print("#####################")
print("Mr Jiggles")
print("#####################")
print("+------------+")
print("|             |")
print("| +---+       |")
print("| |   |  +--+ |")
print("| |   |  |  | |")
print("| +---+  +--+ |")
print("|             |")
print("| X         X |")
print("| X        XX |")
print("| XX       X  |")
print("|  XXXxXXXXX  |")
print("|             |")
print("|             |")
print("+-----[]------+")
print("      []")
print("      []")
print("      [][]")
print("        []")
print("        []")
print("        []")
print("      +----+")
print("      |    |")
print("      |[][]|")
print("      +----+")

pyautogui.typewrite('Jiggly Wiggly!\n', interval=0.1)  
#confirm(text='', title='', buttons=['OK', 'Cancel'])
#set pyautogui.FAILSAFE
while True: #Infinate Loop
	pyautogui.move(1,0) #move mouse 1pxl
	pyautogui.move(-1,0)
        time.sleep(180)
#	pyautogui.PAUSE = 1.0
#	pyautogui.keyDown('f15') #Keyboard Press
#	pyautogui.keyUp('f15') #Keyboard Release
