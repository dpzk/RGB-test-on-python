# import tkinter
from tkinter import *
from time import sleep
from os import path
from sys import exit

# build window on tkinter
tk = Tk()
tk.wm_attributes('-fullscreen', True)
tk.resizable(False, False)
tk.title('')
icon = PhotoImage(width = 16, height = 16)
icon.blank()
tk.call('wm', 'iconphoto', tk._w, icon)
tk.update()
canvas = Canvas(tk, width = tk.winfo_width(), height = tk.winfo_height(), bd = 0, highlightthickness = 0, cursor = 'none')
canvas.pack()
background = canvas.create_rectangle(0, 0, tk.winfo_width(), tk.winfo_height(), fill = '#FF0000', outline = '')

# define refresh function
def load(R, G, B):
    try:
        canvas.itemconfig(background, fill = '#%02X%02X%02X' % (R, G, B))
        tk.update_idletasks()
        tk.update()
        sleep(0.01)
    except:
        exit(0)

# main loop
while True:
    R = 255
    G = 0
    B = 0
    for G in range(1, 256, 1):
        load(R, G, B)
    for R in range(254, -1, -1):
        load(R, G, B)
    for B in range(1, 256, 1):
        load(R, G, B)
    for G in range(254, -1, -1):
        load(R, G, B)
    for R in range(1, 256, 1):
        load(R, G, B)
    for B in range(254, -1, -1):
        load(R, G, B)
