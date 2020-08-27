import tkinter as tk

win=tk.Tk()
win.title('Tk GUI')

cols=['GRE score','University rating','university_name']
data = [ ["322", "3", "Carlie melon university"],
         ["321", "3", "Chicago university"],
         ["321", "3", "RIT university"],
         ["321", "3", "North carolina"],
         ["321", "3", "New york university"],
         ["321", "3", "Chicago univ"] ,
         ["321", "3", "Carlie melon university"],
         ["321", "3", "Chicago university"],
         ["321", "3", "RIT university"],
         ["319", "3", "North carolina"],
         ["319", "3", "New york university"],
         ["319", "3", "Chicago univ"] ]
for y in range(len(data)+1):
    for x in range(len(cols)):
        if y==0:
            e=tk.Entry(font=('Consolas 8 bold'),bg='green',justify='center')
            e.grid(column=x, row=y)
            e.insert(0,cols[x])
        else:
            e=tk.Entry()
            e.grid(column=x, row=y)
            e.insert(0,data[y-1][x])
win.mainloop()