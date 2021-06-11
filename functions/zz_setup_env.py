from integral import *
import msvcrt
import pyautogui

app = " "
packages = []
imports = []
sep = []
val = input("Name of project: ")

f = open("saves/python_imports.txt","r")
contents = f.read()
f.close()

contents = contents.replace("\t","")
#contents = contents.replace(" ","")
all_pkgs = contents.split("\n")
for z in all_pkgs:
	sep.append(z.split(":"))

print("***Install Packages***")
j = 0
print("0. Skip")
for i in sep:
	print(j+1,". ",i[0])
	j+=1

while True:
	char = msvcrt.getch()
	app = char.decode("utf-8") 
	app = app.lower()
	ch = int(app)
	if ch==0: break
	ch = ch-1
	packages.append(sep[ch][1])
	imports.append(sep[ch][2])
	#print(type(ch), ch)

cmd("E:")
instant_write("cd projects_python")
instant_write("mkdir "+val)
instant_write("cd "+val)
instant_write("python -m venv venv")
instant_write("venv\\scripts\\activate")
instant_write("python.exe -m pip install --upgrade pip")

if len(packages)!=0:
	for i in packages:
		instant_write(i)

print("***Press Enter once installation is complete***")
keyboard.wait("enter")
time.sleep(1)
#instant_write("type nul > "+val+".py")
instant_write("copy con "+val+".py")
#time.sleep(2)
for i in imports:
	if i.find("&")!=-1:
		wo = i.split("&")
		for rd in wo:
			instant_write(rd)
	else:
		instant_write(i)

time.sleep(0.2)
press('ctrl+z')
press('enter')

