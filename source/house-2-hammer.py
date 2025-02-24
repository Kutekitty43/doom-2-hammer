#Hammer unit to Doom Map unit converter
import tkinter as tk
import math
import time

def unitGetter(type):
    global getterPassed
    getterPassed = False
    global doomUnits
    global hammerUnits
    if type == "doom":
        doomUnits = userUnits.get()
    elif type == "hammer":
        hammerUnits = userUnits.get()
    getterPassed = True

def doom2Hammer (units, complete):
    while getterPassed != True:
        time.sleep(1)
    units = float(units)
    global hammerUnits
    global text1
    global number1
    hammerUnits = 1
    if complete == True:
        complete = False
    hammerUnits = units * 0.86
    hammerUnits = round(hammerUnits)
    complete = True
    text1 = ("Your value of " + str(doomUnits) + " Map Units is equal to:")
    number1 = str(hammerUnits)
    doomLabel3.config(text = text1)
    doomlabel4.config(text = number1)

def hammer2Doom (units, complete):
    while getterPassed != True:
        time.sleep(1)
    if complete == True:
        complete = False
    global doomUnits
    units = int(units)
    doomUnits = units / 0.86
    doomUnits = round(doomUnits)
    complete = True
    text1 = ("Your value of " + str(hammerUnits) + " Map Units is equal to:")
    number1 = str(doomUnits)
    doomLabel3.config(text = text1)
    doomlabel4.config(text = number1)

def return2Start():
    global hammerUnits
    global doomUnits
    main.pack()
    doom2HammerEnd.pack_forget()
    doom2Hammerentry.pack_forget()
    doom2Hammerprocess.pack_forget()
    hammer2Doomend.pack_forget()
    hammer2Doomentry.pack_forget()
    hammer2Doomprocess.pack_forget()
    doomUnits = 0
    hammerUnits = 0

def doomChange(stage):
    if stage == "entry":
        doom2Hammerentry.pack()
        main.pack_forget()
    elif stage == "processing":
        doom2Hammerprocess.pack()
        doom2Hammerentry.pack_forget()
    elif stage == "end":
        doom2HammerEnd.pack()
        doom2Hammerprocess.pack_forget()
def hammerChange(stage):
    if stage == "entry":
        hammer2Doomentry.pack()
        main.pack_forget()
    elif stage == "processing":
        hammer2Doomprocess.pack()
        hammer2Doomentry.pack_forget()
    elif stage == "end":
        hammer2Doomend.pack()
        hammer2Doomprocess.pack_forget()

text1 = "y"
number1 = "2"
doomUnits = 0
hammerUnits = 0
functComplete = False
getterpassed = False
root = tk.Tk()
root.title("Doom Engine/Source Engine map unit converter")
main = tk.Frame(root)
userUnits = tk.StringVar()
doom2Hammerentry = tk.Frame(root)
doom2Hammerprocess = tk.Frame(root)
doom2HammerEnd = tk.Frame(root)
hammer2Doomentry = tk.Frame(root)
hammer2Doomprocess = tk.Frame(root)
hammer2Doomend = tk.Frame(root)
label1 = tk.Label(main, text="Welcome to Kutekitty's Doom Engine/Source Engine map unit converter.")
label2 = tk.Label(main, text="Choose a conversion type to get started.")
button1 = tk.Button(main, text="Doom Map Units to Hammer Units", command= lambda: doomChange("entry"))
button2 = tk.Button(main, text="Hammer Units to Doom Map Units", command= lambda: hammerChange("entry"))


doomLabel1 = tk.Label(doom2Hammerentry, text="Enter the number of Doom Map Units.")
doomUnitEntry = tk.Entry(doom2Hammerentry, textvariable=userUnits)
doomButton1 = tk.Button(doom2Hammerentry, text="Convert!", command= lambda:  [unitGetter("doom"), doom2Hammer(doomUnits, functComplete), doomChange("processing")])

doomLabel2 = tk.Label(doom2Hammerprocess, text="Processing...")
doomButton2 = tk.Button(doom2Hammerprocess, text="Click to see the converted units.", command= lambda: doomChange("end"))



doomLabel3 = tk.Label(doom2HammerEnd, text = "placeholder")
doomlabel4 = tk.Label(doom2HammerEnd, text = "placeholder", font = ("Arial", 50))
doomlabel5 = tk.Label(doom2HammerEnd, text= "Hammer Units.")
doomButton3 = tk.Button(doom2HammerEnd, text= "Return to start", command = return2Start)

hammerLabel1 = tk.Label(hammer2Doomentry, text="Enter the number of Hammer Units.")
hammerUnitEntry = tk.Entry(hammer2Doomentry, textvariable=userUnits)
hammerButton1 = tk.Button(hammer2Doomentry, text="Convert!", command= lambda:  [unitGetter("hammer"), hammer2Doom(hammerUnits, functComplete), hammerChange("processing")])

hammerLabel2 = tk.Label(hammer2Doomprocess, text="Processing...")
hammerButton2 = tk.Button(hammer2Doomprocess, text="Click to see the converted units.", command= lambda: hammerChange("end"))


root.geometry("400x200")
hammerLabel3 = tk.Label(hammer2Doomend, text = "placeholder")
hammerlabel4 = tk.Label(hammer2Doomend, text = "placeholder", font = ("Arial", 50))
hammerlabel5 = tk.Label(hammer2Doomend, text= "Map Units.")
hammerButton3 = tk.Button(hammer2Doomend, text= "Return to start", command = return2Start)
label1.pack( pady = 2)
label2.pack(pady = 5)
doomLabel1.pack()
button1.pack(side= tk.LEFT, pady= 30)
button2.pack(side = tk.RIGHT, pady = 30)
doomUnitEntry.pack()
main.pack()
doomButton1.pack()
doomLabel2.pack()
doomButton2.pack()
doomLabel3.pack()
doomlabel4.pack()
doomlabel5.pack()
doomButton3.pack()
hammerLabel1.pack()
hammerUnitEntry.pack()
hammerButton1.pack()
hammerLabel2.pack()
hammerLabel3.pack()
hammerButton2.pack()
hammerlabel4.pack()
hammerlabel5.pack()
hammerButton3.pack()
root.mainloop()
