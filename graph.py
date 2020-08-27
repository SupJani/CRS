from tkinter import *
from tkinter.messagebox import *
from joblib import load
import pandas as pd
import numpy as np

import numpy as np
from tkinter import *
from tkinter.messagebox import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt
main = Tk()
main.geometry("700x700")

def make_prediction():
    data = pd.read_csv('Admission_predict.csv', encoding = 'latin-1')
    canvas=FigureCanvasTkAgg(fig,main)
    canvas.get_tk_widget().pack(side=Tk.TOP,fill=Tk.BOTH,expand=1)
    x=df['GRe Score']
    y=df['Admit']
    x=x.reshape(len(x),1)
    y=y.reshape(len(y),1)
    x_train=x[:-230]
    x_test=y[-230:]
    y_train=x[:-230]
    y_test=y[-230:]
    
    model=lm().fit(x_train,y_train)
    predictions=model.predict(x_test)
    plt.scatter(y_test,predictions)
    plt.xlabel('GRE Score',s=20)
    plt.ylabel('Admit',s=20)
    fig=plt.Figure()
    #fig.plot(range(60), range(60))

    ax=fig.add_subplot(111)
    plt.savefig('abc.jpg')

    fig.canvas.draw_idle()
    fig.subplots_adjust(bottom=0.25)
    ax.plot(x,y)
    
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
def openbar():
    os.system('bar.png')
def open_kmeans():
    
    os.system('kmeans.png')
    
def open_kmeans1():
    
    os.system('elbow.png')
    
def open_knn():
    
    os.system('knn.png')

def open_linear():
    os.system('Linear.png')

    
    
def first():
    
    main.destroy()
    
    os.system('python content2.py')

def method2():
    
    main.destroy()
    
    os.system('python login.py')

def open_accuracy():
    
    main.destroy()
    
    os.system('python accuracy.py')

def open_gui():
    
    main.destroy()
    
    os.system('python guialgo.py')


 
   



Label(main, text="Comparison of the graphs:").grid(row=0)


Button(main, text="Quit", command=main.destroy).grid(row=8, column=0, sticky=W, pady=4,padx=3)
Button(main, text="SVM_GRE_Graph", command=open_graph_gre).grid(row=9, column=2, sticky=W, pady=4,padx=3)
Button(main, text="SVM_Toefl_Graph", command=open_graph_toefl).grid(row=9, column=1, sticky=W, pady=4,padx=3)
Button(main, text="SVM_CGPA_Graph", command=open_graph_cgpa).grid(row=10, column=1, sticky=W, pady=4,padx=3)
Button(main, text="SVM_LOR_Graph", command=open_graph_lor).grid(row=10, column=2, sticky=W, pady=4,padx=3)
Button(main, text="SVM_SOP_Graph", command=open_graph_SOP).grid(row=11, column=1, sticky=W, pady=4,padx=3)
Button(main, text="knn_error_rate_graph",command=open_knn_graph).grid(row=10, column=6, sticky=W, pady=4,padx=4)
Button(main, text="KMeans_Graph", command=open_kmeans).grid(row=12, column=1, sticky=W, pady=4,padx=3)
Button(main, text="KMeans_Elbow", command=open_kmeans1).grid(row=13, column=1, sticky=W, pady=4,padx=3)


Button(main, text="Back", command=open_gui).grid(row=8, column=1, sticky=W, pady=4,padx=3)

Button(main, text="Linear regression graph",command=open_linear).grid(row=8, column=3, sticky=W, pady=4,padx=3)
Button(main, text="KNN graph",command=open_knn).grid(row=8, column=6, sticky=W, pady=4,padx=3)
Button(main, text="Accuracy bar chart",command=openbar).grid(row=14, column=6, sticky=W, pady=4,padx=3)


#Button(main, text="graph",command=main.destroy).grid(row=8, column=6, sticky=W, pady=4,padx=3)


mainloop()