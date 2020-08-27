import os
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk
root=Tk()
root.geometry("1350x750+0+0")
root.title("Login System")
bg_icon=ImageTk.PhotoImage(file="images/col.jpg")
user_icon=ImageTk.PhotoImage(file="images/email.png")
pass_icon=ImageTk.PhotoImage(file="images/passwd.png")
logo_icon=ImageTk.PhotoImage(file="images/logo.jpg")
per_icon=ImageTk.PhotoImage(file="images/user.png")
contact_icon=ImageTk.PhotoImage(file="images/contact.png")
logo1_icon=ImageTk.PhotoImage(file="images/logo1.jpg")
bg_lbl=Label(root,image=bg_icon).pack()

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    root.after(flash_delay, flashColour, object, 1 - colour_index)

flash_delay = 500  # msec between colour change
flash_colours = ('white', 'red') # Two colours to swap between
title=Label(root,text="College Recommendation System",font=("times new roman",40,"bold"),bg="blue",bd=10,relief=GROOVE,foreground = flash_colours[0])
title.place(x=0,y=0,relwidth=1) 
flashColour(title, 0)
#=======================================VARIABLES=====================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
EMAIL = StringVar()
CONTACT = StringVar()
PASSWORD = StringVar()
CPASSWORD = StringVar()
#=======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_colsystem.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `user` (user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, email TEXT, contact TEXT, password TEXT)")

        
def LoginForm():
    global Login_Frame
    Login_Frame=Frame(root,bg="white")
    Login_Frame.place(x=400,y=150)
    logolbl=Label(Login_Frame,image=logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
    lbluser=Label(Login_Frame,text=" Email",image=user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lbluser.grid(row=1,column=0,padx=20,pady=10)
    txtuser=Entry(Login_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=EMAIL)
    txtuser.grid(row=1,column=1,padx=20)
    lblpass=Label(Login_Frame,text=" Password",image=pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lblpass.grid(row=2,column=0,padx=20,pady=10)
    txtpass=Entry(Login_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=PASSWORD,show='*')
    txtpass.grid(row=2,column=1,padx=20)
    btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg='yellow',fg="red",command=Login)
    btn_log.grid(row=4,columnspan=2,pady=10)
    lbl_login = Label(Login_Frame, text="Don't have an account? Sign Up!",anchor="center",fg="red", font=('times new roman',13,"bold"),bg='white')
    lbl_login.place(x=230,y=377,anchor="center")
    lbl_login.bind('<Button-1>', ToggleToRegister)
def RegisterForm():
    global Register_Frame
    Register_Frame=Frame(root,bg="white")
    Register_Frame.place(x=390,y=90)
    logolbl=Label(Register_Frame,image=logo1_icon,bd=0).grid(row=0,columnspan=2,pady=10)
    lblfirstname=Label(Register_Frame,text=" First Name",image=per_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lblfirstname.grid(row=1,column=0,padx=20,pady=10)
    txtfirstname=Entry(Register_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=FIRSTNAME)
    txtfirstname.grid(row=1,column=1,padx=20)
    lbllastname=Label(Register_Frame,text=" Last Name",image=per_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lbllastname.grid(row=2,column=0,padx=20,pady=10)
    txtlastname=Entry(Register_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=LASTNAME)
    txtlastname.grid(row=2,column=1,padx=20)
    lbluser=Label(Register_Frame,text=" Email",image=user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lbluser.grid(row=3,column=0,padx=20,pady=10)
    txtuser=Entry(Register_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=EMAIL)
    txtuser.grid(row=3,column=1,padx=20)
    lblcontact=Label(Register_Frame,text=" Contact No",image=contact_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lblcontact.grid(row=4,column=0,padx=20,pady=10)
    txtcontact=Entry(Register_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=CONTACT)
    txtcontact.grid(row=4,column=1,padx=20)
    lblpass=Label(Register_Frame,text=" Password",image=pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lblpass.grid(row=5,column=0,padx=20,pady=10)
    txtpass=Entry(Register_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=PASSWORD,show='*')
    txtpass.grid(row=5,column=1,padx=20)
    lblpass=Label(Register_Frame,text=" Confirm Password",image=pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
    lblpass.grid(row=6,column=0,padx=20,pady=10)
    txtpass=Entry(Register_Frame,bd=5,relief=GROOVE,font=("",15),textvariable=CPASSWORD,show='*')
    txtpass.grid(row=6,column=1,padx=20)
    btn_log=Button(Register_Frame,text="Sign Up",width=15,font=("times new roman",14,"bold"),command=Register,bg='yellow',fg="red")
    btn_log.grid(row=8,columnspan=2,pady=10)
    lbl_register = Label(Register_Frame, text="Have an account? Sign In!",anchor="center",fg="red", font=('times new roman',13,"bold"),bg='white')
    lbl_register.place(x=285,y=560,anchor="center")
    lbl_register.bind('<Button-1>', ToggleToLogin)
def ToggleToRegister(event=None):
    Login_Frame.destroy()
    RegisterForm()
def ToggleToLogin(event=None):
    Register_Frame.destroy()
    LoginForm()

def Register():
    Database()
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or EMAIL.get() == "" or CONTACT.get() == "" or PASSWORD.get() == "" or CPASSWORD.get() =="":
        messagebox.showerror("Error","All fields are required!!")
    else:
        cursor.execute("SELECT * FROM `user` WHERE `email` = ?", (EMAIL.get(),))
        if cursor.fetchone() is not None:
            messagebox.showerror("Error","Already registered as an user!!")
        
        elif PASSWORD.get() != CPASSWORD.get():
            messagebox.showerror("Error","Password is not equal to confirmed password!!")
            
        elif cursor.fetchone() is None and PASSWORD.get() == CPASSWORD.get():
            messagebox.showinfo("Successfull",f"Welcome {FIRSTNAME.get()}")
            cursor.execute("INSERT INTO `user` (firstname, lastname, email, contact, password) VALUES(?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(EMAIL.get()), str(CONTACT.get()), str(PASSWORD.get())))
            conn.commit()
            FIRSTNAME.set("")
            LASTNAME.set("")
            EMAIL.set("")
            CONTACT.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close()
    print(CONTACT.get())
def Login():
    Database()
    if EMAIL.get == "" or PASSWORD.get() == "":
        messagebox.showerror("Error","All fields are required!!")
    else:
        cursor.execute("SELECT * FROM `user` WHERE `email` = ? and `password` = ?", (EMAIL.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.destroy()
            os.system('python gui1.py')
        else:
            messagebox.showerror("Error","Invalid email or password!!")



LoginForm()  
if __name__ == '__main__':
    root.mainloop()
