from tkinter import *
from tkinter import messagebox
import pymysql

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('600x640+0+0')
        self.title('Personal Registration Form')

        self.page_dictionary = {}
        self.page_dictionary["HomePage"] = HomePage(self)
        self.page_dictionary["Page1"] = Page1(self)
        self.page_dictionary["RegistrationForm"] = RegistrationForm(self)

        self.raise_frame("HomePage")

    def raise_frame(self, next_screen):
        new_screen = self.page_dictionary[next_screen]
        new_screen.tkraise()
        
class HomePage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bg_color = '#3b5997'
        title1 = Label(self, text = "Homepage", background = self.bg_color, foreground ="white")
        title1.place(x=100,y=20,width=200,height=50)

        button1 = Button(self, text = "Register new user", background = self.bg_color, foreground ="white", command = lambda: root.raise_frame("RegistrationForm"))
        button1.place(x=100,y=195,width=200,height=25)

        button2 = Button(self, text = "Lookup users", background = self.bg_color, foreground ="white", command = lambda: root.raise_frame("Page1"))
        button2.place(x=400,y=195,width=200,height=25)

        self.place(x=100,y=20,width=1000,height=900)

class Page1(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bg_color = '#3b5997'
        title1 = Label(self, text = "Page 1", background = self.bg_color, foreground ="white")
        title1.place(x=100,y=20,width=200,height=50)

        button1 = Button(self, text = "Go back", background = self.bg_color, foreground ="white", command = lambda: root.raise_frame("HomePage"))
        button1.place(x=100,y=195,width=200,height=25)

        self.place(x=100,y=20,width=1000,height=900)

class RegistrationForm(Frame):
    def __init__(self, root, *args):
        Frame.__init__(self, root, *args)
        self.root = root

        self.fg = '#0d4763'
        self.bg = '#bed8e6'

        self.gender = StringVar(value="N/A")
        self.country = StringVar(value="N/A")
        self.displaypw1 = IntVar(value=0)
        self.displaypw2 = IntVar(value=0)
        self.firstnameEntry = None
        self.lastnameEntry = None
        self.emailEntry = None
        self.usernameEntry = None
        self.passwordEntry = None
        self.confirmpasswordEntry = None

        self.database_initialize()

        self.place_title()
        self.place_labels_and_entries()
        self.place_gender_buttons()
        self.place_country_dropdown()
        self.place_checkboxes()
        self.place_buttons()

        self.place(x=100,y=20,width=1000,height=900)
    
    def insert_data(self, firstname, lastname, email, gender, country, username, password):
        # Connect to MySQL server
        db = pymysql.connect(host='localhost', user='root', password='password', database='Personal_registration_form')
        cur = db.cursor()
        
        # Insert data into the table
        cur.execute("INSERT INTO user_data (firstname, lastname, email, gender, country, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (firstname, lastname, email, gender, country, username, password))

        # Commit the changes
        db.commit()

        messagebox.showinfo('Success', 'Registration successful!')

    def submit(self):
        if self.firstnameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your first name')
        elif self.lastnameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your last name')
        elif self.emailEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your email')
        elif self.gender.get()=='':
            messagebox.showerror('Alert!', 'Please enter your gender')
        elif self.country.get()=='':
            messagebox.showerror('Alert!', 'Please enter your country ')
        elif self.usernameEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your username')
        elif self.passwordEntry.get()=='':
            messagebox.showerror('Alert!', 'Please enter your password ')
        elif self.confirmpasswordEntry.get()=='':
            messagebox.showerror('Alert!', 'Please confirm your password ')
        elif self.confirmpasswordEntry.get() != self.passwordEntry.get():
            messagebox.showerror('Alert! Passwords are not matching!')
        else:
            self.insert_data(self.firstnameEntry.get(), self.lastnameEntry.get(), self.emailEntry.get(), self.gender.get(), self.country.get(), self.usernameEntry.get(), self.passwordEntry.get())

    def go_back(self):
        # Clear entry fields
        self.firstnameEntry.delete(0, 'end')
        self.lastnameEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.gender.set(0)  # Reset gender selection
        self.country.set('Select Country')  # Reset country selection
        self.usernameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.confirmpasswordEntry.delete(0, 'end')
        self.displaypw1.set(0)  # Uncheck password display toggle
        self.displaypw2.set(0)  # Uncheck confirm password display toggle

    def place_buttons(self):
        submit1btn = Button(self, text='Submit', width=15, borderwidth=5, height=2,bg=self.bg,fg=self.fg, cursor='hand2', border=2, command=self.submit)
        submit1btn.place(x=150, y=500)

        bckbtn = Button(self, text='reset', width=15, border=2, height=2,cursor='hand2', command=self.go_back)     
        bckbtn.place(x=100, y=550)

        home_button = Button(self, text='return to home', width=15, border=2, height=2,cursor='hand2', command= lambda: self.root.raise_frame("HomePage"))
        home_button.place(x=0, y=550)
    def place_checkboxes(self):
        def show1():
            if (self.displaypw1.get()==1):
                self.passwordEntry.config(show='*')
            else:
                self.passwordEntry.config(show='')

        def show2():
            if(self.displaypw2.get()==1):
                self.confirmpasswordEntry.config(show='*')
            else:
                self.confirmpasswordEntry.config(show='')
        
        check1 = Checkbutton(self, variable= self.displaypw1, bg=self.bg,command=show1)
        check1.place(x=420, y=350)

        check2 = Checkbutton(self, variable= self.displaypw2, bg=self.bg,command=show2)
        check2.place(x=420, y=400)

    def place_country_dropdown(self):
        countryLabel=Label(self, text='Select Country:', fg=self.fg, bg=self.bg)
        countryLabel.place(x=10, y=250)

        countries=['Algeria', "Australia", 'Bahamas', 'Canada']

        countryLabelDropdown=OptionMenu(self, self.country, *countries)
        countryLabelDropdown.place(x=240, y=250)

    def place_gender_buttons(self):
        genderlbl =Label(self, text='Select Gender:', fg=self.fg, bg=self.bg)
        genderlbl.place(x=10, y=200)

        genderRadio1=Radiobutton(self, text='Male', variable=self.gender, value='Male')
        genderRadio1.place(x=240, y=200)

        genderRadio2=Radiobutton(self, text='Female', variable=self.gender, value='Female')
        genderRadio2.place(x=350, y=200)

    def place_labels_and_entries(self):
        firstname_label = Label(self, text="First Name:", fg=self.fg, bg=self.bg)
        firstname_label.place(x=10, y=70)

        self.firstnameEntry=Entry(self, width=30, borderwidth=2)
        self.firstnameEntry.place(x=240, y=70)

        lastnamelbl = Label(self, text="Last Name:", fg=self.fg, bg=self.bg)
        lastnamelbl.place(x=10, y=110)

        self.lastnameEntry=Entry(self, width=30, borderwidth=2)
        self.lastnameEntry.place(x=240, y=110)

        emaillbl=Label(self, text='Email:', fg=self.fg, bg=self.bg)
        emaillbl.place(x=10, y=150)

        self.emailEntry=Entry(self, width=30, borderwidth=2)
        self.emailEntry.place(x=240, y=150)

        usernamelbl = Label(self, text='Username:', fg=self.fg, bg=self.bg)
        usernamelbl.place(x=10, y=300)

        self.usernameEntry=Entry(self, width=30, borderwidth=2)
        self.usernameEntry.place(x=240, y=300)

        passwordlbl = Label(self, text='Password:', fg=self.fg, bg=self.bg)
        passwordlbl.place(x=10, y=350)

        self.passwordEntry=Entry(self, width=30, borderwidth=2)
        self.passwordEntry.place(x=240, y=350)

        confirmpasswordlbl = Label(self, text='Confirm Password:',  fg=self.fg, bg=self.bg)
        confirmpasswordlbl.place(x=10, y=400)

        self.confirmpasswordEntry=Entry(self, width=30, borderwidth=2)
        self.confirmpasswordEntry.place(x=240, y=400)

    def place_title(self):
        title = Label(self, text = "Personal Registration Form", background = self.bg, foreground = self.fg)
        title.place(x=100,y=20,width=200,height=50)

    def database_initialize(self):
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
        db.commit()
