from functions.integral import *

def searcher(num,command=""):
	if num == 0:
		if num==0: f = open("functions/saves/commands.txt","r")
		commands = f.read()
		f.close()
		commands = commands.replace("\t","")
		commands = commands.replace(" ","")
		comms_array = commands.split("\n")
		for comms in comms_array:
			parts = comms.split(":")
			if contains(command,parts[1]):
				return(parts[0])
		return "No_comms_found"
	if num == 1:
		f = open("functions/saves/open_type.txt","r")
		contents = f.read()
		f.close()
		contents = contents.replace("\t","")
		contents = contents.replace(" ","")
		all_comms = contents.split("\n")
		return(all_comms)
	if num == 2:
		f = open("functions/saves/specific_apps.txt","r")
		commands = f.read()
		f.close()
		commands = commands.replace("\t","")
		commands = commands.replace(" ","")
		comms_array = commands.split("\n")
		for comms in comms_array:
			parts = comms.split(":")
			if contains(command,parts[1]):
				return(parts[0])
		return "No_comms_found"

def open_app(app_name):
	all_comms = searcher(1)
	for comms in all_comms:
		comms = comms.split(":")
		if contains(app_name,comms[0]):
			if comms[1]=="run": run(comms[2])
			if comms[1]=="start": start(comms[2])
			print("Started ",app_name)

def close_app(app_name=""):
	i = 0
	if app_name=="":
		keyboard.press_and_release('alt+f4')
		time.sleep(0.2)
		return 1
	while contains(active_window(),app_name)!=True:
		print(active_window())
		i += 1
		alttab(i);
		if i>10: return 0
		if contains(active_window(),app_name):
			keyboard.press_and_release('alt+f4')
			time.sleep(0.2)
			return 1

def startup_app():
	#ctfmonster
	run("C:\Windows\system32\ctfmon.exe")
	time.sleep(1)
	#mouse driver ready
	start("pointer");
	#keyboard.press_and_release("tab")
	keyboard.press_and_release("tab");time.sleep(0.2)
	keyboard.press_and_release("space")
	time.sleep(7)
	close_app()
	close_app()
	time.sleep(1)
	print("Initialization Complete")

def start_writing():
	current_app = active_window()

def clone_env():
	cmd("E:")
	instant_write("cd projects_python\\assistant_bot")
	instant_write("venv\\scripts\\activate")
	instant_write("cd functions")

def specific_app(text):
	clone_env()
	name = searcher(2,text)
	if name!="No_comms_found":instant_write("python "+name+".py")




#open_app("blender")
#close_app("notepad")