from tkinter import *
from tkinter.messagebox import *
from joblib import load
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
import os
import pandas as pd
from tkinter import messagebox

#import numpy as np
#from tkinter import *
#import tkinter as tk
#from tkinter import ttk



import tkinter as tk
from tkinter import ttk


def get_values():
    """Returns the values of the txtboxes"""
    return [
        int(num1.get()),
        int(num2.get()),
        int(num3.get()),
        float(num4.get()),
        float(num5.get()),
        float(num6.get())
    ]

def get_values11():
    """Returns the values of the txtboxes"""
    return [
        int(num1.get()),
        int(num2.get()),
        int(num3.get()) 
     
    ]

def make_prediction():
    '''Runs the model.jbl and get result'''
    if not os.path.exists("model.jbl"):
        print("model.jbl not found. Please run Train.ipynb")
        return
    x_values = get_values()
    x1_values = [x_values[0],x_values[1],x_values[5]]
    model = load("model2.jbl")
    scaler=load("scaler2.jbl")
    input_data=[x_values]
    input_data=scaler.transform(input_data)
    admit=model.predict_proba(input_data)[0][1]
    prediction = "{0:.2f}%".format(admit*100)
    show_txtbx.delete(0, 'end')
    show_txtbx.insert(0, prediction)

def linear_predictions():
    '''Runs the model.jbl and get result'''
    if not os.path.exists("regression.jbl"):
        print("regression.jbl not found. Please run Train.ipynb")
        return
    x_values = get_values()
    x1_values = [x_values[0],x_values[1],x_values[5]]
    model = load("regression.jbl")
#     scaler=load("scaler.jbl")
    input_data=[x_values]
#     input_data=scaler.transform(input_data)
    admit=model.predict(input_data)[0]
    prediction = "{0:.2f}%".format(admit*100)
    show_txtbx.delete(0, 'end')
    show_txtbx.insert(0, prediction)
    
def knn_prediction():
    '''Runs the model.jbl and get result'''
    if not os.path.exists("model3.jbl"):
        print("model.jbl not found. Please run Train.ipynb")
        return
    x_values = get_values()
    x1_values = [x_values[0],x_values[1],x_values[5]]
    model = load("model3.jbl")
   #scaler=load("scaler3.jbl")
    input_data=[x_values]
    # i n_data=scaler.transform(input_data)
    admit=model.predict_proba(input_data)[0][1]
    prediction = "{0:.2f}%".format(admit*100)
    show_txtbx.delete(0, 'end')
    show_txtbx.insert(0, prediction)

def naive_prediction():
    '''Runs the naive.jbl and get result'''
    if not os.path.exists("naive.jbl"):
        print(".jbl not found. Please run Train.ipynb")
        return
    x_values = get_values11()
    
    x1_values = [x_values[0],x_values[1],x_values[2]]
    model = load("naive.jbl")
   #scaler=load("scaler3.jbl")
    input_data=[x_values]
    # i n_data=scaler.transform(input_data)
    admit=model.predict_proba(input_data)[0][1]
    prediction = "{0:.2f}%".format(admit*100)
    show_txtbx.delete(0, 'end')
    show_txtbx.insert(0, prediction)  
  
    
def display2():
    #root.geometry("400x300")
    os.system('python table.py')
    
    #b1.grid(columns=0, row=0)
    #b1.pack()
    #b1.displa
    

main = Tk()
main.geometry("700x700")
main.title('Proj on recommendation system')
#main.configure(background='sky blue')


# Add university rating
Label(main, text="Enter GRE SCORE:").grid(row=0)
Label(main, text="Enter TOEFL score:").grid(row=1) 
Label(main, text="Enter University rating:").grid(row=2)
Label(main, text="Enter SOP:").grid(row=3)
Label(main, text="Enter LOR:").grid(row=4)
Label(main, text="Enter CGPA:").grid(row=5)
Label(main, text="Admission Chance: ").grid(row=6)


num1 = Entry(main)
num2 = Entry(main)
num3 = Entry(main)
num4 = Entry(main)
num5 = Entry(main)
num6 = Entry(main)

show_txtbx = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
num3.grid(row=2, column=1)
num4.grid(row=3, column=1)
num5.grid(row=4, column=1)
num6.grid(row=5, column=1)

show_txtbx.grid(row=6, column=1)

#new code

def correct(inp):
    if inp.isdigit():      
        return True
    elif inp is "":
        messagebox.showinfo(" invalid entry")
        print("enter no")
        return False
    else:
        messagebox.showinfo(" invalid entry")
        
        return False
reg=main.register(correct)
num1.config(validate="key",validatecommand=(reg,'%P'))    
num2.config(validate="key",validatecommand=(reg,'%P'))    
num3.config(validate="key",validatecommand=(reg,'%P'))    
num4.config(validate="key",validatecommand=(reg,'%P'))    
num5.config(validate="key",validatecommand=(reg,'%P'))    



def open_graph_gre():
    os.system('svm_gre.png')
def open_graph_toefl():
    os.system('svm_toefl.png')
def open_graph_lor():
    os.system('svm_lor.png')
def open_graph_cgpa():
    os.system('svm_cgpa.png')
def open_knn_graph():
    os.system('knn_rate.png')
def open_graph_SOP():
    os.system('svm_SOP.png')
    
def clear():
    num1.delete(0,END)
    num2.delete(0,END)
    num3.delete(0,END)
    num4.delete(0,END)
    num5.delete(0,END)
    num6.delete(0,END)


    
def first():
    
    main.destroy()
    
    os.system('python content2.py')

def method2():
    
    main.destroy()
    
    os.system('python gui1.py')

def open_accuracy():
    
    main.destroy()
    
    os.system('python accuracy.py')
    os.system('bar.png')
    
def open_graph():
    
    main.destroy()
    
    os.system('python graph.py')


    
#Button(main, text="ALGORITHMS", command=clear).grid(row=11, column=2, sticky=W, pady=4,padx=3)    
Button(main, text="Quit", command=main.destroy).grid(row=8, column=0, sticky=W, pady=4,padx=3)
Button(main, text="Clear", command=clear).grid(row=8, column=6, sticky=W, pady=4,padx=3)


Button(main, text="SVM", command=make_prediction).grid(row=8, column=1, sticky=W, pady=4,padx=3)
#Button(main, text="SVM_GRE_Graph", command=open_graph_gre).grid(row=9, column=2, sticky=W, pady=4,padx=3)
#Button(main, text="SVM_Toefl_Graph", command=open_graph_toefl).grid(row=9, column=1, sticky=W, pady=4,padx=3)
#Button(main, text="SVM_CGPA_Graph", command=open_graph_toefl).grid(row=10, column=1, sticky=W, pady=4,padx=3)
#Button(main, text="SVM_LOR_Graph", command=open_graph_toefl).grid(row=10, column=2, sticky=W, pady=4,padx=3)
#Button(main, text="SVM_SOP_Graph", command=open_graph_SOP).grid(row=11, column=1, sticky=W, pady=4,padx=3)

Button(main, text="Linear regression",command=linear_predictions).grid(row=8, column=3, sticky=W, pady=4,padx=3)
#Button(main, text="KMeans",command=open_graph_kmeans).grid(row=8, column=5, sticky=W, pady=4,padx=3)

Button(main, text="Graph",command=open_graph).grid(row=9, column=6, sticky=W, pady=4,padx=3)

#Button(main, text="knn_error_rate_graph",command=open_knn_graph).grid(row=10, column=6, sticky=W, pady=4,padx=4)
Button(main, text="COMPARE ACCURACY",command=open_accuracy).grid(row=20, column=6, sticky=W, pady=4,padx=4)

Button(main, text="KNN",command=knn_prediction).grid(row=8, column=2, sticky=W, pady=4,padx=3)
#Button(main, text="Naive Bayes",command=naive_prediction).grid(row=12, column=6, sticky=W, pady=4,padx=3)
Button(main, text="BACK",command=method2).grid(row=19, column=6, sticky=W, pady=4,padx=3)
Button(main, text="PREDICTION OF UNIVERSITY",command=first).grid(row=13, column=6, sticky=W, pady=4,padx=4)

#Button(main, text="graph",command=main.destroy).grid(row=8, column=6, sticky=W, pady=4,padx=3)


mainloop()