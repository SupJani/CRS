import tkinter as tk
from tkinter import messagebox

win=tk.Tk()
win.title('COMPARISON OF ACCURACY OF ALGORITHMS')
#var = StringVar()
#label = Message( win, textvariable=var, relief=RAISED )

#var.set("KNN is having high accuracy")
#label.pack()

cols=['ALGORITHM','ACCURACY']
data = [ ["LINEAR REGRESSION", "81-85"],
         ["SVM", "85-90"],
         ["KNN", "91-94"]]
for y in range(len(data)+1):
    for x in range(len(cols)):
        if y==0:
            e=tk.Entry(font=('Consolas 12 bold'),bg='blue',justify='center')
            e.grid(column=x, row=y)
            e.insert(0,cols[x])
        else:
            e=tk.Entry()
            e.grid(column=x, row=y)
            e.insert(0,data[y-1][x])
win.geometry("400x400")


messagebox.showinfo("CONCLUSION", "KNN is having high accuracy")

win.mainloop()