from pyautogui import *
from pynput.keyboard import Key,Controller
import pyautogui
import time
import keyboard
import random
import win32api,win32con
import winsound
import sys

def check():
	if(len(sys.argv)!=3):
		print("USAGE:python fire.py textfile.txt 0(limiter)")
		#print("modes: 0-fire71 1-rbcautofill 2-BMcustom 3-Firecustom")
		quit()
	else:
		return 1


check()

flag=0
if(len(sys.argv)>1):
	flag=int(sys.argv[2])

keyboard=Controller()
# pyautogui.sleep(5)
fname=sys.argv[1]
f=open(fname)
coords=f.readlines()
#print(coords)

coordinates=[]
for coord in coords:
	acoord=int(coord.split()[0])
	bcoord=int(coord.split()[1])
	coordinate=[]
	coordinate.append(acoord)
	coordinate.append(bcoord)
	coordinates.append(coordinate)

# print(coordinates)
# #X:  827 Y:   98 RGB: (113,  99,  84) :left
# #X:  875 Y:   93 RGB: (122,  96,  76) :right
# pyautogui.doubleClick(827,98)
# pyautogui.sleep(5)
def say(c):
	time.sleep(2)
	keyboard.type(c)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)#presses defown
    time.sleep(0.03) #topause the script for 0.01s
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)#releases


def dclickleftcoordbar():
	pyautogui.doubleClick(827,98) #left coordinate
	a=str(coordinate[0])

def dclickrightcoordbar():
	pyautogui.doubleClick(875,93) #right coordinate
	b=str(coordinate[1])

def enterpress():
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	pyautogui.sleep(0.5)

def entercoords(a,b):
	dclickleftcoordbar()
	keyboard.type(a)
	pyautogui.sleep(0.5)
	dclickrightcoordbar()
	keyboard.type(b)
	pyautogui.sleep(0.5)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	pyautogui.sleep(0.5)



def clicksearch():
	click(927,111)
	pyautogui.sleep(0.5)

def launchattack():
	click(1070,590)#attack button
	time.sleep(0.5)
	#X: 1071 Y:  715 RGB: (126, 177,  57)
	click(1071,715) #green button
	pyautogui.sleep(0.5)

def presetchooser():
	click(624,922) #presets triangle button
	pyautogui.sleep(0.5)

def clearwave():
	#X: 1062 Y:  976 RGB: (242, 242, 242)
	click(1062,976) #presets triangle button
	pyautogui.sleep(0.5)

def wave1():
	click(469,898)
	pyautogui.sleep(0.5)

def applytoallwaves():
	click(762,921)
	pyautogui.sleep(0.5)

def wave2():
	click(513,873)
	pyautogui.sleep(0.5)

def applytoonewave():
	click(716,917)
	pyautogui.sleep(0.5)

def nextwave():
	#X:  777 Y:  867 RGB: (255, 255, 255)
	click(777,867)
	pyautogui.sleep(0.5)

def prevwave():
	#X:  703 Y:  866 RGB: (255, 255, 255)
	click(703,866)
	pyautogui.sleep(0.5)

def autofillone():
	#X: 1209 Y:  977 RGB: (169,  46,  27)
	click(1209,977)
	pyautogui.sleep(0.5)

def autofillall():
	#X: 1288 Y:  977 RGB: (197,  87,  69)
	#X: 1283 Y:  973 RGB: (255, 255, 255)
	click(1283,973)
	pyautogui.sleep(0.5)

def confirmcoinattack():
	click(1405,970)
	time.sleep(0.5)

	#coin horses
	#683 Y:  537 RGB: (255, 255, 255)
	click(683,537)
	time.sleep(0.5)


	#final green button
	#X: 1112 Y:  820 RGB: (255, 255, 255)
	click(1112,820)
	pyautogui.sleep(0.5)

def confirmnohorsesattack():
	click(1405,970)
	time.sleep(0.5)

	#coin horses
	#683 Y:  537 RGB: (255, 255, 255)
	# click(683,537)
	# time.sleep(0.5)


	#final green button
	#X: 1112 Y:  820 RGB: (255, 255, 255)
	click(1112,820)
	pyautogui.sleep(0.5)


#presets

def nomads():
	time.sleep(0.5)
	presetchooser()
	
	wave1()
	
	applytoallwaves()

	clearwave()
	
	presetchooser()
	
	wave2()
	
	applytoonewave()
	autofillone()
	
	time.sleep(0.5)

def rbcautofill():
	time.sleep(0.5)
	autofillall()
	time.sleep(0.5)

def bmcustom():
	time.sleep(0.5)
	presetchooser()
	wave1()
	applytoallwaves()
	presetchooser()
	wave2()
	applytoonewave()
	time.sleep(0.5)

def custom1():  # 1 1 1 2
	time.sleep(0.5)
	presetchooser()
	
	wave1()
	
	applytoallwaves()
	prevwave()
	
	presetchooser()
	
	wave2()
	
	applytoonewave()
	applytoonewave()
	time.sleep(0.5)

def custom2(): #1 1 1 1
	time.sleep(0.5)
	applytoallwaves()
	time.sleep(0.5)

def custom3(): #1 0 0 0
	time.sleep(0.5)
	applytoonewave()
	time.sleep(0.5)


def main():
	pyautogui.sleep(5)
	i=0
	for coordinate in coordinates:
		if i<flag:
			i=i+1
			continue
		a=str(coordinate[0])
		b=str(coordinate[1])
	entercoords(a,b)
	#print("sys arg 3 is ",sys.argv[3])
	
	for i in range(20):
		clicksearch()
		launchattack()
		nomads()
		confirmnohorsesattack()
		time.sleep(0.5)

main()