from tkinter import *
from tkinter.ttk import * 
from tkinter.font import Font
import time

class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
 
        self.text = "WELCOME TO RECOMMENDATION SYSTEM"
        #self.text = "For MS"
        self.geometry("700x700")
        self.configure(background='sky blue')
        #self.bold_font = Font(family="Helvetica", size=14, weight="bold")
       # self.text.tag_configure("BOLD", font=self.bold_font)
        self.i = 0
        self.spacing = 0
         
  
        
        for val in range(len(self.text)):
            exec("self.l{0} = Label(text=self.text[{1}])".format(val, val))
 
        self.appear()
        
 
    def appear(self):
        if not self.i >= len(self.text):
            eval("self.l{0}.place(x=self.spacing, y=0)".format(self.i))
            self.i += 1
            self.spacing += 20
        self.after(300, self.appear)
        
 
w = Window()
w.mainloop()