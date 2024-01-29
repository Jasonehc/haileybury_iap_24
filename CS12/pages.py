from tkinter import * 
from tkinter import messagebox
import pymysql

# 'main body' app
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("800x800+0+0")
        self.title("Personal Registration Form")

        self.page_dict = {}
        self.page_dict['HomePage'] = HomePage(self)
        self.page_dict['LoginPage'] = LoginPage(self)
        self.page_dict['RegisterPage'] = RegisterPage(self)

        self.raise_frame('HomePage')

    def raise_frame(self, page):
        frame = self.page_dict[page]
        frame.tkraise()

# pages
class HomePage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root

        label = Label(self, text = "This is the home Page", fg="black", font="tahoma 20")
        label.place(x=100, y=100)

        button1 = Button(self, text = "Login", command = lambda: root.raise_frame('LoginPage'))
        button1.place(x=100, y=200)

        button2 = Button(self, text = "Register", command = lambda: root.raise_frame('RegisterPage'))
        button2.place(x=100, y=250)

        self.place(x=100, y=200, width=500, height=900)

class LoginPage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root 

        label = Label(self, text = "Login", fg="black", font="tahoma 20")
        label.place(x=100, y=100)

        button1 = Button(self, text = "Home", command = lambda: root.raise_frame('HomePage'))
        button1.place(x=100, y=250)

        self.place(x=100, y=200, width=500, height=900)

class RegisterPage(Frame):
    def __init__(self, root, *args):
        Frame.__init__(self, root, *args)
        self.root = root

        label = Label(self, text = "Register", fg="black", font="tahoma 20")
        label.place(x=100, y=100)

        button1 = Button(self, text = "Home", command = lambda: root.raise_frame('HomePage'))
        button1.place(x=100, y=250)

        self.place(x=100, y=200, width=500, height=900)



