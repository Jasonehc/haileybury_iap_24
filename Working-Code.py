# (1) Import packages
from tkinter import *
from tkinter import messagebox
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
frame=Frame(windows, width=610, height=640, bg='#bed8e6', bd=8)
frame.place(x=0,y=0)

# Window label
heading =Label(frame, text='Personal Registration Form', fg='#0d4763', bg='#bed8e6', font=('Calibre', 20, 'bold'))
heading.place(x=90, y=3)

# First and last name
firstnamelbl = Label(frame, text="First Name:", fg='#0d4763',bg='#bed8e6', font=('Calibre', 15, 'bold'))
firstnamelbl.place(x=10, y=70)

firstnameEntry=Entry(frame, width=30, borderwidth=2)
firstnameEntry.place(x=240, y=70)

lastnamelbl = Label(frame, text="Last Name:", fg='#0d4763',bg='#bed8e6', font=('Calibre', 15, 'bold'))
lastnamelbl.place(x=10, y=110)

lastnameEntry=Entry(frame, width=30, borderwidth=2)
lastnameEntry.place(x=240, y=110)

# Email 
emaillbl=Label(frame, text='Email:', fg='#0d4763', bg='#bed8e6', font=('Calibre', 15, 'bold'))
emaillbl.place(x=10, y=150)

emailEntry=Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=240, y=150)

# Gender
genderlbl =Label(frame, text='Select Gender:', fg='#0d4763', bg='#bed8e6', font=('Calibre', 15, 'bold'))
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

def switch():
    if clicked.get() == 0:  
        passwordEntry.config(show="*")
    else:
        passwordEntry.config(show="")

clicked = IntVar(value=0)

checkbox = Checkbutton(master = frame, variable = clicked, command = switch)
checkbox.place(x=500, y = 350)

# Submit Button
def submit():
    if firstnameEntry.get() == "":
        messagebox.showerror(message = "Missing first name, please fill in")
    elif lastnameEntry.get() == "":
        messagebox.showerror(message = "Missing last name, please fill in")
    elif gender.get() == "0":
        messagebox.showerror(message = "Missing gender, please fill in")
    elif country.get() == 'Select Country':
        messagebox.showerror(message = "Missing country, please fill in")
    elif confirmpasswordEntry.get() != passwordEntry.get():
        messagebox.showerror(message = "Passwords don't match")
    elif '@' not in emailEntry.get():
        messagebox.showerror(message = "Bad email")
    else:
        db = pymysql.connect(host='localhost', user = 'root', password=  'password')
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
        
        # Insert data into the table
        cur.execute("INSERT INTO user_data (firstname, lastname, email, gender, country, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), gender, country, usernameEntry.get(), passwordEntry.get()))

        cur.execute("select password from user_data where username = 'bluebear';")
        rows = cur.fetchall()
        print(rows)
        for i in rows:
            print(i)
        db.commit()
        cur.close()

        messagebox.showinfo(message = "Success! Submitted!")

def reset():
    firstnameEntry.delete(first = 0, last = len(firstnameEntry.get())) 
    lastnameEntry.delete(first = 0, last = len(lastnameEntry.get()))
    emailEntry.delete(first = 0, last = len(firstnameEntry.get()))
    gender.set('0')
    country.set('Select Country')
    
submit_button = Button(master = frame, text = "Submit", command = submit) 
submit_button.place(x=300,  y = 500)

reset_button = Button(master = frame, text = "Reset", command = reset) 
reset_button.place(x=200,  y = 500)
# Run application

        # Connect to MySQL serve

windows.mainloop()