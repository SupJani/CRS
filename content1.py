{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os\n",
    "import tkinter as tk\n",
    "from tkinter.messagebox import *\n",
    "\n",
    "from tkinter import *\n",
    "        \n",
    "from PIL import ImageTk, Image\n",
    "\n",
    "main=Tk()\n",
    "\n",
    "#Setting it up\n",
    "img = ImageTk.PhotoImage(Image.open(\"image.jpg\"))\n",
    "\n",
    "#Displaying it\n",
    "imglabel = Label(main, image=img).grid(row=6, column=7)        \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "#window= Tk()\n",
    "main.geometry(\"700x700\")\n",
    "main.title('Proj on recommendation system')\n",
    "main.configure(background='sky blue')\n",
    "\n",
    "Label(main, text=\"HIGHER STUDIES RECOMMENDATION SYSTEM\").grid(row=0)\n",
    "\n",
    "def display1():\n",
    "    #root.geometry(\"400x300\")\n",
    "   \n",
    "    main.destroy() \n",
    "    os.system('python gui.py')\n",
    "    \n",
    "    #b1.grid(columns=0, row=0)\n",
    "    #b1.pack()\n",
    "    #b1.display()\n",
    "    \n",
    "b1=tk.Button(main, text=\"CONTENT BASED METHOD\", command=display1).grid(row=9, column=4, sticky=W, pady=4,padx=3)\n",
    "#display(b1)\n",
    "#b1.pack(side= LEFT, expand=True)\n",
    "#b1.show()\n",
    "mainloop()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
