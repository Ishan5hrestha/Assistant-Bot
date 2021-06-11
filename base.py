
from functions.listener import *
from functions.worker import *

print("I am here for you.")
while True:
	while keyboard.is_pressed("up"):
		text = listener()
		print("> ",text)
		if text =="exit": break

		if searcher(0,text)=="start_app": open_app(text)
		if searcher(0,text)=="init_start": startup_app()
		if searcher(0,text)=="close_app": close_app()
		if searcher(0,text)=="specific": 
			print("Project In? ")
			text = listener(howlong=8)
			specific_app(text)
		if text.find("close")!=-1:close_app()
		if text.find("change")!=-1 and text.find("tab")!=-1: alttab()


#print(searcher(0,"open_notepad"))
