from tkinter import W,Label,Entry,mainloop,Button,Tk
from joblib import load
import pandas as pd
# import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt


main = Tk()
main.geometry("500x400+350+250")

def make_prediction():
    data = pd.read_csv('Admission_predict.csv',sep=',')
    # canvas=FigureCanvasTkAgg(fig,main)
    # canvas.get_tk_widget().pack(side=Tk.TOP,fill=Tk.BOTH,expand=1)
    print(data['GRE Score'])
    x=data['GRE Score']
    y=data['Admit ']

    x=x.values.reshape(len(x),1)
    y=y.values.reshape(len(y),1)
    
    x_train=x[:-230]
    x_test=y[-230:]
    y_train=x[:-230]
    y_test=y[-230:]

    model=lm().fit(x_train,y_train)
    predictions=model.predict(x_test)

    # plt.scatter(y_test,predictions)
    plt.scatter(x_test,predictions)

    plt.xlabel('GRE Score')
    plt.ylabel('Admit')
    fig=plt.Figure()
    
    #fig.plot(range(60), range(60))
    ax=fig.add_subplot(111)
    fig.canvas.draw_idle()
    fig.subplots_adjust(bottom=0.25)
    ax.plot(x,y)
    plt.show()
    plt.savefig('abc.png')

# Add university rating
Label(main, text="Comparison of the graphs:").grid(row=0)

Button(main, text="Quit", command=main.destroy).grid(row=8, column=0, sticky=W, pady=4,padx=3)
Button(main, text="SVM graph", command=make_prediction).grid(row=8, column=1, sticky=W, pady=4,padx=3)
Button(main, text="Linear regression graph",command=make_prediction).grid(row=8, column=3, sticky=W, pady=4,padx=3)
Button(main, text="KNN graph",command=main.destroy).grid(row=8, column=6, sticky=W, pady=4,padx=3)
#Button(main, text="graph",command=main.destroy).grid(row=8, column=6, sticky=W, pady=4,padx=3)

mainloop()