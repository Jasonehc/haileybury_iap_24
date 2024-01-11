#Done by Mr.Noureddine Tadjerout 

# (1) Import packages
from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk
import pymysql

# (2) Set colors
text_color = '#0d4763'
background_color = '#bed8e6'

# (3) Create window
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('540x640+200+10')
windows.resizable(False,False)

# (5) Create frame
frame=Frame(windows, width=610, height=640, bg=background_color, bd=8)
frame.place(x=0,y=0)

# Window label
heading =Label(frame, text='Personal Registration Form', fg=text_color, bg=background_color, font=('Calibre', 20, 'bold'))
heading.place(x=90, y=3)

# First and last name
firstnamelbl = Label(frame, text="First Name:", fg=text_color,bg=background_color, font=('Calibre', 15, 'bold'))
firstnamelbl.place(x=10, y=70)

firstnameEntry=Entry(frame, width=30, borderwidth=2)
firstnameEntry.place(x=240, y=70)

lastnamelbl = Label(frame, text="Last Name:", fg=text_color,bg=background_color, font=('Calibre', 15, 'bold'))
lastnamelbl.place(x=10, y=110)

lastnameEntry=Entry(frame, width=30, borderwidth=2)
lastnameEntry.place(x=240, y=110)

# Email 
emaillbl=Label(frame, text='Email:', fg=text_color, bg=background_color, font=('Calibre', 15, 'bold'))
emaillbl.place(x=10, y=150)

emailEntry=Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=240, y=150)

# Gender
genderlbl =Label(frame, text='Select Gender:', fg=text_color, bg=background_color, font=('Calibre', 15, 'bold'))
genderlbl.place(x=10, y=200)

gender = StringVar(value='0')
genderRadio1=Radiobutton(frame, text='Male', variable=gender, value='Male', font='tahoma 13 bold')
genderRadio1.place(x=240, y=200)

genderRadio2=Radiobutton(frame, text='Female', variable=gender, value='Female', font='tahoma 13 bold')
genderRadio2.place(x=350, y=200)

# Country dropdown
countryLabel=Label(frame, text='Select Country:', fg=text_color, bg=background_color, font=('Calibre', 13, 'bold'))
countryLabel.place(x=10, y=250)

countries=['Algeria', "Australia", 'Bahamas', 'Canada']
country = StringVar(value='Select Country')
countryLabelDropdown=OptionMenu(frame, country, *countries)
countryLabelDropdown.place(x=240, y=250)

# Username
usernamelbl = Label(frame, text='Username:', fg=text_color, bg=background_color, font=('Calibre', 15, 'bold'))
usernamelbl.place(x=10, y=300)

usernameEntry=Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=240, y=300)

# Password
passwordlbl = Label(frame, text="Password:", fg=text_color, bg=background_color, font=('Calibre', 15, 'bold'))
passwordlbl.place(x=10, y=350) 

passwordEntry=Entry(frame, width=30, borderwidth=2)
passwordEntry.place(x=240, y=350)

confirmpasswordlbl = Label(frame, text='Confirm Password:', fg=text_color, bg=background_color, font=('Calibre', 15, 'bold'))
confirmpasswordlbl.place(x=10, y=400)

confirmpasswordEntry=Entry(frame, width=30, borderwidth=2)
confirmpasswordEntry.place(x=240, y=400)

# Toggle password display
displaypw1 = IntVar(value=0)
displaypw2 = IntVar(value=0)

def show1():
    if(displaypw1.get()==1):
        passwordEntry.config(show='*')
    else:
        passwordEntry.config(show='')

def show2():
    if(displaypw2.get()==1):
        confirmpasswordEntry.config(show='*')
    else:
        confirmpasswordEntry.config(show='')

passwordCheck1 = Checkbutton(frame, variable= displaypw1, onvalue=1, offvalue=0, command=show1)
passwordCheck1.place(x=430, y=350)

passwordCheck2 = Checkbutton(frame, variable= displaypw2, onvalue=1, offvalue=0, command=show2)
passwordCheck2.place(x=430, y=400)

# (6) Database

# DB Initialization
db = pymysql.connect(host='localhost', user='root', password='breadeunice')
cur = db.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS Personal_registration_form')
cur.execute('USE Personal_registration_form')

# Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstname VARCHAR(255),
        lastname VARCHAR(255),
        email VARCHAR(255),
        gender VARCHAR(10),
        country VARCHAR(50),
        username VARCHAR(50),
        password VARCHAR(255)
    )
''')
db.commit()

def insert_data(firstname, lastname, email, gender, country, username, password):
     # Connect to MySQL server
      db = pymysql.connect(host='localhost', user='root', password='breadeunice', database='Personal_registration_form')
      cur = db.cursor()
      
      # Insert data into the table
      cur.execute("INSERT INTO user_data (firstname, lastname, email, gender, country, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (firstname, lastname, email, gender, country, username, password))

      # Commit the changes
      db.commit()

      messagebox.showinfo('Success', 'Registration successful!')

def submit():
      if firstnameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your First name')
      elif lastnameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your Last name')
      elif emailEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your email')
      elif gender.get()=='':
            messagebox.showerror('Alert!', 'Please enter your Gender')
      elif country.get()=='Select Country':
            messagebox.showerror('Alert!', 'Please enter your country ')
      elif usernameEntry.get()=='':
           messagebox.showerror('Alert!', 'Please enter your username')
      elif passwordEntry.get()=='':
           messagebox.showerror('Alert!', 'Please enter your password ')
      elif confirmpasswordEntry.get()=='':
           messagebox.showerror('Alert!', 'Please confrim your password ')
      elif passwordEntry.get() != confirmpasswordEntry.get():
           messagebox.showerror('Alert!', 'Please make sure passwords are matching')
      else:
            insert_data(firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), gender.get(), country.get(), usernameEntry.get(), passwordEntry.get())

submit1btn = Button(frame, text='Submit', width=15, borderwidth=5, height=2,bg='#7f7fff',fg='white', cursor='hand2', border=2,
                font=('#57a1f8',16,'bold'), command=submit)
submit1btn.place(x=150, y=500)

# (7) Back button
def go_back():
    # Clear entry fields
    firstnameEntry.delete(0, 'end')
    lastnameEntry.delete(0, 'end')
    emailEntry.delete(0, 'end')
    gender.set(0)  # Reset gender selection
    country.set('Select Country')  # Reset country selection
    usernameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    confirmpasswordEntry.delete(0, 'end')
    displaypw1.set(0)  # Uncheck password display toggle
    displaypw2.set(0)  # Uncheck confirm password display toggle

bckbtn = Button(frame, text='<<', width=15, border=2, height=2,cursor='hand2', command=go_back)     
bckbtn.place(x=0, y=550)

windows.mainloop()


