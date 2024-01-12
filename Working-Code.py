# (1) Import packages
from tkinter import *

# (2) Set colors

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

# Run application
windows.mainloop()
