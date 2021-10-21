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
