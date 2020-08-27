import sys
import os
import pandas as pd

import tkinter as tk
from tkinter.messagebox import *

from tkinter import *
from tkinter import ttk
        
from PIL import ImageTk, Image

main = Tk()
#main.geometry("300x400")
#main.title('Recommendation of the universities')
main.configure(background='sky blue')

Label(main, text="THIS IS CORELATION BASED RECOMMENDATION").grid(row=0)
main.invisible="true"

scores = tk.Tk() 
label = tk.Label(scores, text="Top 20 University Listings", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns

cols1 = ('Serial_No.', 'GREScore', 'University_Rating')
listBox = ttk.Treeview(scores, columns=cols1, show='headings')



#new code
def show1():
    
   # main.destroy()
    
    #data = pd.read_csv('Admission_Predict_Ver1.1.csv', encoding = 'latin-1')
    
    data = pd.read_csv('Admission_Predict_new.csv', encoding = 'latin-1')
    rating=pd.DataFrame(data.groupby('GREScore')['University_Rating'].mean())
    ratings_pivot = pd.pivot_table(data=data, values='TOEFLScore', index='GREScore', columns='University_Rating')    
    correlation_matrix = ratings_pivot.corr(method='pearson')    
         
    abc=correlation_matrix.head(10) 
    tempList=data[['Serial_No.','GREScore','University_Rating']].head(20)
    #print(tempList[['Serial No.', 'GRE Score', 'TOEFL Score']])
    tempList.sort_values(by='University_Rating')
    #print(tempList)

    for Serialno, UniversityRating, Uname in tempList.values:
        listBox.insert("", "end", values=(Serialno, UniversityRating, Uname))
        #print(tempList.columns.values).head(10)

#scores = tk.Tk() 
#label = tk.Label(scores, text="Top 20 University Listings", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
#cols = ('SerialNo.', 'GRE Score', 'Uname')
#listBox = ttk.Treeview(scores, columns=cols, show='headings')
# set column headings
for col in cols1:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(scores, text="Show University Name", width=20, command=show1).grid(row=4, column=0)

closeButton = tk.Button(scores, text="Close", width=15, command=scores.destroy).grid(row=4, column=1)
scores.mainloop()
main.destroy()
mainloop()
