from tkinter import *
    
import os, sys, subprocess

win=Tk()

b1 = Button(win, text = "PREMIERE", command = lambda: os.startfile(r'(file directory here)'))
b2 = Button(win, text = "STEAM", command = lambda: os.startfile(r'(file directory here)'))
b3 = Button(win, text = "BRAVE", command = lambda: os.popen('start brave.exe'))

b4 = Button(win, text = "AGE OF WAR", command = lambda: os.popen('start brave https://www.crazygames.com/game/age-of-war'))
b5 = Button(win, text = "KRUNKER", command = lambda: os.popen('start brave https://krunker.io/?game=FRA:0k2w8'))
b6 = Button(win, text = "MINECRAFT", command = lambda: os.startfile(r'(file directory here)'))
b7 = Button(win, text = "TERRARIA", command = lambda: os.startfile(r'(file directory here)'))

b8 = Button(win, text = "SHUTDOWN", command = lambda: subprocess.call(["shutdown.exe", "-f", "-s", "-t", "0"]))
b9 = Button(win, text = "SLEEP", command = lambda: subprocess.call(['rundll32.exe', 'powrprof.dll', 'SetSuspendState','0','1','0']))
b10 = Button(win, text = "RESTART", command = lambda: subprocess.call(["shutdown.exe", "-f", "-r", "-t", "0"]))

l = Label(win, text = "Apps")
k = Label(win, text = "Games")
j = Label(win, text = "Computer")

l.grid(row = 0, column = 0, padx = 10, pady = 10)
k.grid(row = 0, column = 1, padx = 10, pady = 10)
j.grid(row = 0, column = 2, padx = 10, pady = 10)

b1.grid(row = 1, column = 0, padx = 10, pady = 10)
b2.grid(row = 2, column = 0, padx = 10, pady = 10)
b3.grid(row = 3, column = 0, padx = 10, pady = 10)

b4.grid(row = 1, column = 1, padx = 10, pady = 10)
b5.grid(row = 2, column = 1, padx = 10, pady = 10)
b6.grid(row = 3, column = 1, padx = 10, pady = 10)
b7.grid(row = 4, column = 1, padx = 10, pady = 10)

b8.grid(row = 1, column = 2, padx = 10, pady = 10)
b9.grid(row = 2, column = 2, padx = 10, pady = 10)
b10.grid(row = 3, column = 2, padx = 10, pady = 10)

mainloop()
