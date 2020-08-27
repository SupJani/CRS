import sys
import os
import tkinter as tk
from tkinter.messagebox import *

from tkinter import *
from tkinter import *
from PIL import ImageTk, Image

main=Tk()

#Setting it up
img = ImageTk.PhotoImage(Image.open("image.jpg"))

#Displaying it
imglabel = Label(main, image=img).grid(row=6, column=7)        




#window= Tk()
main.geometry("700x700")
main.title('Proj on recommendation system')
#main.configure(background='sky blue')

Label(main, text="HIGHER STUDIES RECOMMENDATION SYSTEM").grid(row=0)





def display1():
    #root.geometry("400x300")
   
    main.destroy() 
    os.system('python guialgo.py')
    
    #b1.grid(columns=0, row=0)
    #b1.pack()
    #b1.display()
    
b1=tk.Button(main, text="CLICK", command=display1).grid(row=9, column=4, sticky=W, pady=4,padx=3)
#display(b1)
#b1.pack(side= LEFT, expand=True)
#b1.show()
mainloop()
