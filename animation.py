import tkinter as tk
from tkinter import *
import os
root = tk.Tk()
root.title("PROJECT ON RECOMMENDED SYSTEM")
root.configure(bg='sky blue')
#canvas = canvas(root, bg = "blue", height=100, width=100) 
#canvas.grid(row=0,column=2)

#C = tkinter.Canvas(root, bg="blue", height=250, width=300)

canvas = tk.Canvas(root)
#canvasColor = "yellow"
#canvas = Canvas(width=600, height=600, bg='white')
canvas.pack()

canvas_text = canvas.create_text(10, 10, text='', anchor=tk.CENTER,fill='blue')
#canvas_text = C.create_text(10, 10, text='', anchor=tk.NW)

test_string =      "WELCOME TO HIGHER STUDIES RECOMMENDATION SYSTEM"
#Time delay between chars, in milliseconds
delta = 100 
delay = 10
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta

root.mainloop()