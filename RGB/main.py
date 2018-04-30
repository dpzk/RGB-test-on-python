from tkinter import *

tk = Tk()
tk.wm_attributes('-fullscreen', True)
tk.resizable(False, False)
tk.update()
canvas = Canvas(tk, width = tk.winfo_width(), height = tk.winfo_height(), bd = 0, highlightthickness = 0)
canvas.pack()
background = canvas.create_rectangle(0, 0, tk.winfo_width(), tk.winfo_height(), fill = '#FF0000', outline = '')
def load(R, G, B):
    canvas.itemconfig(background, fill = '#%02X%02X%02X' % (R, G, B))
    tk.update_idletasks()
    tk.update()

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
