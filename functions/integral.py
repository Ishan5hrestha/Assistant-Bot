import keyboard
import pyautogui
import time
from win32gui import GetWindowText, GetForegroundWindow

def press(key):
	keyboard.press_and_release(key)

def write(text):
	keyboard.write(text);time.sleep(0.2)

def instant_write(text):
	keyboard.write(text);time.sleep(0.2)
	keyboard.press_and_release('enter')

def active_window():
	fullname = GetWindowText(GetForegroundWindow())
	fullname = fullname.split("-")
	name = fullname[len(fullname)-1]
	name.replace(" ","")
	return name.lower()

def run(command):
	print("In Run")
	keyboard.press_and_release('cmd + r');time.sleep(0.2)
	while active_window()!="run":continue
	write(command)
	while active_window()!="run":continue
	keyboard.press_and_release('enter')
	time.sleep(0.2)

def start(command):
	print("In Start")
	keyboard.press_and_release('cmd');time.sleep(2)	#2 because start is slow
	while active_window()!="search":continue
	write(command)
	time.sleep(1)	#because start is slow
	while active_window()!="search":continue
	keyboard.press_and_release('enter')
	time.sleep(0.2)

def alttab(num):
	pyautogui.keyDown('alt')
	for i in range(num):
		pyautogui.press('tab')
	pyautogui.keyUp('alt')

def contains(sentence, words):
	found = False
	word_array = words.split(",")
	for word in word_array:
		if word.find("&")!=-1:
			wo = word.split("&")
			for rd in wo:
				if sentence.find(rd)!=-1:
					found=True
				else:
					found=False
					break
			if found == True: return 1;
		else:
			if sentence.find(word)!=-1: return 1
			else: return 0
				

def cmd(command):
	run("cmd")
	write(command)
	keyboard.press_and_release('enter')

#while True:print(active_window())
#run("notepad")
#print(contains("what the hell?","what&how,what&cuz,no&way"))