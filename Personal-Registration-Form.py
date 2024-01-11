#Done by Mr.Noureddine Tadjerout 

# step 1:
from tkinter import *
from tkinter import messagebox

#from PIL import Image, ImageTk
import pymysql

# (X) Set colors
text_color = "#8732a8"
background_color = "#edd8ed"

#step 2: 
#window size
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('540x640+200+10')
windows.resizable(False,False)

#Step 8: 
# databse section

def Submit():
      if firstnameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your First name')
      elif lastnameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your Lastt name')
   
      elif emailEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your email')

      elif gender.get()=='':
            messagebox.showerror('Alert!', 'Please enter your Gender')
      elif OM.get()=='':
            messagebox.showerror('Alert!', 'Please enter your country ')

      elif usernameEntry.get()=='':
           messagebox.showerror('Alert!', 'Please enter your username')

      elif passwordEntry.get()=='':
           messagebox.showerror('Alert!', 'Please enter your password ')

      elif confirmpasswordEntry.get()=='':
           messagebox.showerror('Alert!', 'Please confrim your password ')

      else:
            db=pymysql.connect(host='localhost', user='root', password='12345678')
            cur=db.cursor()

            query='create database Personal_registration_form'
            cur.execute(query)
            query='use Personal_registration_form'
            cur.execute(query)

# Step 6           

#show and hide password
def show1():
    passwordEntry.configure(show='#')
    check1.configure(command=hide1)

def hide1():
    passwordEntry.configure(show='')
    check1.configure(command=show1)


def show2():
      confirmpasswordEntry.configure(show='#')
      check2.configure(command=hide2)

def hide2():
      confirmpasswordEntry.configure(show='')
      check2.configure(command=show2)


# Step 4:

#section for getting data from the entry fields
firstname = StringVar()
lastname = StringVar()
email = StringVar()
gender = StringVar()
variable1=StringVar()
username = StringVar()
password = StringVar()
confirmpassword = StringVar()
OM = StringVar()

# Step 3:

#frame=Frame(windows)

frame=Frame(windows, width=610, height=640, bg='black', bd=8)
frame.place(x=0,y=0)

#labels on window
heading =Label(frame, text='Personal Registration Form', fg='#97FFFF', bg='black', font=('Calibre', 20, 'bold'))
heading.place(x=90, y=3)

firstnamelbl = Label(frame, text="First Name:", fg='#97FFFF',bg='black', font=('Calibre', 15, 'bold'))
firstnamelbl.place(x=10, y=70)

firstnameEntry=Entry(frame, width=30, borderwidth=2)
firstnameEntry.place(x=240, y=70)

lastnamelbl = Label(frame, text="Last Name:", fg='#97FFFF',bg='black', font=('Calibre', 15, 'bold'))
lastnamelbl.place(x=10, y=110)

lastnameEntry=Entry(frame, width=30, borderwidth=2)
lastnameEntry.place(x=240, y=110)

emaillbl=Label(frame, text='Email:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
emaillbl.place(x=10, y=150)

emailentry=Entry(frame, width=30, borderwidth=2)
emailentry.place(x=240, y=150)

genderlbl =Label(frame, text='Select Gender:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
genderlbl.place(x=10, y=200)

gender.set(0)
genderRadio1=Radiobutton(frame, text='Male', variable=gender, value='Male', font='tahoma 13 bold')
genderRadio1.place(x=240, y=200)

genderRadio2=Radiobutton(frame, text='Female', variable=gender, value='Female', font='tahoma 13 bold')
genderRadio2.place(x=350, y=200)

countryLabel=Label(frame, text='Select Country:', fg='#97FFFF', bg='black', font=('Calibre', 13, 'bold'))
countryLabel.place(x=10, y=250)

country=['Algeria', "Australia", 'Bahamas', 'Canada']

OM.set('Select Country')

countryLabelDropdown=OptionMenu(frame, OM, *country)
countryLabelDropdown.place(x=240, y=250)

usernamelbl = Label(frame, text='Username:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
usernamelbl.place(x=10, y=300)

usernameEntry=Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=240, y=300)

passwordlbl = Label(frame, text='Password:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
passwordlbl.place(x=10, y=350)

passwordEntry=Entry(frame, width=30, borderwidth=2)
passwordEntry.place(x=240, y=350)

confirmpasswordlbl = Label(frame, text='Confirm Password:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
confirmpasswordlbl.place(x=10, y=400)

confirmpasswordEntry=Entry(frame, width=30, borderwidth=2)
confirmpasswordEntry.place(x=240, y=400)

# Step 5: 
#to show and hide password

check1 = Checkbutton(frame, text='', bg='black',command=show1)
check1.place(x=420, y=350)

check2 = Checkbutton(frame, text='', bg='black',command=show2)
check2.place(x=420, y=400)

submit1btn = Button(frame, text='Submit', width=15, borderwidth=5, height=2,bg='#7f7fff',fg='white', cursor='hand2', border=2,
                font=('#57a1f8',16,'bold'))#,command=submit
                
submit1btn.place(x=150, y=500)

# Step 7: 

bckbtn = Button(frame, text='<<', width=15, border=2, height=2,cursor='hand2')
                
bckbtn.place(x=0, y=550)


windows.mainloop()


