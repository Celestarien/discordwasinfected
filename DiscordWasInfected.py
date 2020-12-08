from tkinter import Entry, Button, Text, Label, Tk, END, RAISED 
import os
import time


##########################################
#                FUNCTIONS               #
##########################################
def isInfected():
    title_label = Label(root, text="Your Discord is infected !\nPlease check your file : \n" + path_discord)
    title_label.pack(anchor='n')


##########################################
#                Design                  #
##########################################


root = Tk()
root.title("DWI - Discord Was Infected")
root.geometry("800x400")
root.configure(bg='#23272a')


# Create title label
title_label = Label(root, text="DWI - Discord Was Infected")
title_label.pack(anchor='n')




##########################################
#                SCRIPTS                 #
##########################################

# We try to find version 0.0.308 and 0.0.307
version_path_308 = str(os.path.expandvars(r'%APPDATA%\discord\0.0.308'))
version_path_307 = str(os.path.expandvars(r'%APPDATA%\discord\0.0.307'))

# Get Discord Path
if os.path.exists(version_path_308):
    path_discord = os.path.expandvars(r'%APPDATA%\discord\0.0.308\modules\discord_desktop_core')
elif os.path.exists(version_path_307):
    path_discord = os.path.expandvars(r'%APPDATA%\discord\0.0.307\modules\discord_desktop_core')
else:
    title_label = Label(root, text="Your version of discord is not recognized\nDo not hesitate to take a tour on the GitHub: \nhttps://github.com/Celestarien/discordwasinfected")
    title_label.pack(anchor='n')

# Add the file to scan
path_discord = str(path_discord) + "\index.js"
# Open the file
discord_file = open(path_discord, "r")

# Read lines from file
Lines = discord_file.readlines()

number_of_lines = len(Lines)

if number_of_lines > 1:
        isInfected()
else:
    for line in Lines:
        if number_of_lines == 1 and line == "module.exports = require('./core.asar');":
            title_label = Label(root, text="Your Discord is safe ! Have fun !")
            title_label.pack(anchor='n')
        else:
            isInfected()

##########################################
#                CREDITS                 #
##########################################
title_label = Label(root, text="Dev by ♥ from Celestarien.")
title_label.pack(anchor='n')



root.mainloop()