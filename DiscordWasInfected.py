from tkinter import Entry, Button, Text, Label, Tk, END, RAISED 
import os
import time
import re
import hashlib

bg_color = '#23272a'

##########################################
#                FUNCTIONS               #
##########################################
def isInfected():
    title_label = Label(root, text="Your Discord is infected !\nPlease check your file : \n" + path_index_discord, bg=bg_color, fg='red')
    title_label.place(relx = 0.5, rely = 0.5, anchor = 'center') 


##########################################
#                Design                  #
##########################################


root = Tk()
root.title("DWI - Discord Was Infected")
root.geometry("800x400")
root.configure(bg=bg_color)


# Create title label
title_label = Label(root, text="DWI - Discord Was Infected", bg=bg_color, fg='white')
title_label.place(relx = 0.5, rely = 0.4, anchor = 'center') 
# title_label.pack(anchor='n')


##########################################
#                SCRIPTS                 #
##########################################
version = []

regex = re.compile('^[0-9.]+.[0-9.]+.[0-9]')
path = str(os.path.expandvars(r"%APPDATA%\discord"))
list_dir = os.listdir(path)
for diretorie in list_dir:
    a = regex.findall(diretorie)
    if a:
       version = a

# Get Discord Path
path_discord = os.path.expandvars(r'%APPDATA%\discord\\' + version[0] + '\modules\discord_desktop_core')
if not os.path.exists(path_discord):
    path_discord = ""
    print('Your version of discord is not recognized\nDo not hesitate to take a tour on the GitHub: \nhttps://github.com/Celestarien/discordwasinfected')
    time.sleep(10)

# Add the file to scan
path_index_discord = str(path_discord) + "\index.js"

# Original Hash
original_hash = "5fc5801cdb0fbf4aad69bb9e6f7b8957f664e872"
# Check actual hash
hasher = hashlib.sha1()
with open(path_index_discord, 'rb') as afile:
    buf = afile.read()
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read()
actual_hash = hasher.hexdigest()

if original_hash == actual_hash:
    title_label = Label(root, text="Your Discord is safe ! Have fun !", bg=bg_color, fg='#2b1')
    title_label.place(relx = 0.5, rely = 0.5, anchor = 'center') 
else:
    isInfected()

##########################################
#                CREDITS                 #
##########################################
title_label = Label(root, text="Github : https://github.com/Celestarien/discordwasinfected", bg=bg_color, fg='white')
title_label.place(relx = 0.5, rely = 0.6, anchor = 'center') 
title_label = Label(root, text="Dev by ♥ from Celestarien & Alexander3312.", bg=bg_color, fg='white')
title_label.place(relx = 0.5, rely = 0.7, anchor = 'center')



root.mainloop()
