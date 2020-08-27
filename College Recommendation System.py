import tkinter
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
flash_delay = 500  # msec between colour change
flash_colours = ('black', 'blue') # Two colours to swap between
def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    root.after(flash_delay, flashColour, object, 1 - colour_index)
root = tkinter.Tk()
root.title("College Recommendation System")
root.geometry('700x400')
my_label = Label(root, text = 'WELCOME TO HIGHER STUDIES RECOMMENDED SYSTEM!',
                      foreground = flash_colours[0],font=("Helvetica", 18))
my_label.place(x=70, y=90)
my_label.place(relx=1.0, rely=2.0, anchor='sw')
my_label.pack()
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('abc2.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)
def display1():
    #root.geometry("400x300")
   
    root.destroy() 
    os.system('python login.py')
    
    #b1.grid(columns=0, row=0)
    #b1.pack()
    #b1.display()


b1=Button(root, text = 'click me',command=display1)





b1.pack(side=BOTTOM)

#my_button.pack()
b1.place(relx=0.5, rely=0.5, anchor='se')

b2=Button(root, text="Quit", command=root.destroy)

b2.pack(side=RIGHT)

b2.place(relx=0.484, rely=0.7, anchor='se')
my_label.pack()
flashColour(my_label, 0)
root.mainloop()