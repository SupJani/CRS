import sys
import os
import pandas as pd

import tkinter as tk
from tkinter.messagebox import *

from tkinter import *
from tkinter import ttk
        
from PIL import ImageTk, Image

main = Tk()
main.geometry("300x400")
main.title('Recommendation of the universities')
#main.configure(background='sky blue')

#Label(main, text="THIS IS CONTENT BASED RECOMMENDATION").grid(row=0)

scores = tk.Tk() 
label = tk.Label(scores, text="Top 20 University Listings", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('SerialNo.', 'GRE Score', 'Uname')
listBox = ttk.Treeview(scores, columns=cols, show='headings')

#newcode

cols1 = ('SerialNo.', 'GRE Score', 'Uname')
listBox = ttk.Treeview(scores, columns=cols, show='headings')

def show():
    
   # main.destroy()
    
    #data = pd.read_csv('Admission_Predict_Ver1.1.csv', encoding = 'latin-1')
    
    
    data = pd.read_csv('Admission_Predict_Ver1.1.csv', encoding = 'latin-1')
    tempList=data[['Serial No.','GRE Score','Uname']].head(20)
    #print(tempList[['Serial No.', 'GRE Score', 'TOEFL Score']])
    tempList.sort_values(by='GRE Score')
    #print(tempList)

    for Serialno, GRE, TOEFL in tempList.values:
        listBox.insert("", "end", values=(Serialno, GRE, TOEFL))
        #print(tempList.columns.values).head(10)

#scores = tk.Tk() 
#label = tk.Label(scores, text="Top 20 University Listings", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
#cols = ('SerialNo.', 'GRE Score', 'Uname')
#listBox = ttk.Treeview(scores, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)




#new code


showScores = tk.Button(scores, text="Show University Name", width=20, command=show).grid(row=4, column=0)

closeButton = tk.Button(scores, text="Close", width=15, command=scores.destroy).grid(row=4, column=1)

def show3():
    #main.destroy()
    
    os.system('python content3.py')
def show4():
    #main.destroy()
    
    os.system('python guialgo.py')
def show5():
    #main.destroy()
    
    os.system('python corelation.py')


Button(main, text=" BASED ON CONTENT",command=show).grid(row=4, column=6, sticky=W, pady=4,padx=4)
Button(main, text=" BASED ON POPULARITY",command=show3).grid(row=5, column=6, sticky=W, pady=4,padx=4)
Button(main, text=" BASED ON CORELATION",command=show5).grid(row=6, column=6, sticky=W, pady=4,padx=4)
Button(main, text=" BACK",command=show4).grid(row=7, column=6, sticky=W, pady=4,padx=4)

#b1=Tk.Button(main, text="POPULARITY BASED METHOD", command=show).grid(row=9, column=4, sticky=W, pady=4,padx=3)

#b1=tk.Button(main, text="CONTENT BASED METHOD", command=show).grid(row=9, column=4, sticky=W, pady=4,padx=3)

#b1=tk.Button(main, text="CORELATION BASED METHOD", command=show).grid(row=9, column=4, sticky=W, pady=4,padx=3)


#display(b1)
#b1.pack(side= LEFT, expand=True)
#b1.show()


scores.mainloop()
main.destroy()
mainloop()

    
