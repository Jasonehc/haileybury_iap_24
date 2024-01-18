from tkinter import *
from tkinter import messagebox, font
from PIL import ImageTk, Image
import pymysql

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('550x300+0+0')
        self.title('FakeBook')

        self.bg_color = '#3b5997'
        self.big_font = font.Font(size=30)
        self.small_font = font.Font(size=15)
        self.page_dictionary = {}
        self.page_dictionary["UserHomePage"] = (UserHomePage(self), '550x300+0+0')
        self.page_dictionary["LookUpPage"] = (LookUpPage(self), '550x300+0+0')
        self.page_dictionary["RegistrationPage"] = (RegistrationPage(self), '550x500+0+0')
        self.page_dictionary["HomePage"] = (HomePage(self), '550x300+0+0')
        self.page_dictionary["LogInPage"] = (LogInPage(self), '550x300+0+0')

        self.raise_frame("HomePage")

    def raise_frame(self, next_screen):
        new_screen, new_screen_size = self.page_dictionary[next_screen]
        self.geometry(new_screen_size)
        new_screen.tkraise()

class HomePage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root

        title = Label(self, text = "FakeBook", font = self.root.big_font, background = self.root.bg_color, foreground = "white")
        title.place(x= 300, y = 50, width = 200, height = 100)

        #header = Label(self, text = "Fakebook", background = self.root.bg_color, foreground = "white")

        button1 = Button(self, text = "Register", background = self.root.bg_color, foreground ="white", command = lambda: root.raise_frame("RegistrationPage"))
        button1.place(x=300,y=160,width=200,height=25)

        button2 = Button(self, text = "Log In", background = self.root.bg_color, foreground ="white", command = lambda: root.raise_frame("LogInPage"))
        button2.place(x=300,y=185,width=200,height=25)

        logo = Image.open('facebook_logo.png')
        logo_img = ImageTk.PhotoImage(logo)

        logo_label = Label(self, image=logo_img)
        logo_label.image = logo_img
        logo_label.place(x=20, y=20)

        self.place(x=0,y=0,width=550,height=500)

class UserHomePage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        
        title1 = Label(self, text = "Fakebook", background = self.root.bg_color, foreground ="white")
        title1.place(x=0,y=0,width=600,height=20)

        button1 = Button(self, text = "Register new user", background = self.root.bg_color, foreground ="white", command = lambda: root.raise_frame("RegistrationPage"))
        button1.place(x=300,y=150,width=200,height=25)

        button2 = Button(self, text = "Lookup users", background = self.root.bg_color, foreground ="white", command = lambda: root.raise_frame("LookUpPage"))
        button2.place(x=300,y=175,width=200,height=25)

        self.place(x=0,y=0,width=1000,height=900)

class LookUpPage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.bg_color = self.root.bg_color
        self.fg = 'white'
        title = Label(self, text = "Query users", background = self.bg_color, foreground ="white")
        title.place(x=0,y=20,width=200,height=50)

        button1 = Button(self, text = "Go back", background = self.bg_color, foreground ="white", command = self.return_to_home)
        button1.place(x=0,y=150,width=100,height=25)

        self.place(x=0,y=0,width=1000,height=900)

        query_label = Label(self, width=15, text = "Enter query:", background = self.bg_color, foreground='white')
        query_label.place(x=0, y=100)

        self.query_entry=Entry(self, width=50, borderwidth=2)
        self.query_entry.place(x=120, y=100)

        run_query_button = Button(self, text="Run query", width=15,borderwidth=5, height=2,bg=self.bg_color,fg=self.fg, cursor='hand2', border=2, command=self.run_query)
        run_query_button.place(x=120, y=150, height=25)

        self.query_results = Label(self, text = "")
        self.query_results.place(x=0, y=200)

    def return_to_home(self):
        self.query_results.config(text = "")
        self.root.raise_frame("UserHomePage")

    def run_query(self):
        db = pymysql.connect(host='localhost', user='root', password='password', database='Personal_registration_form')
        cur = db.cursor()
        query = self.query_entry.get()
        cur.execute(query)

        counter = 0
        txt = ""
        for idx, row in enumerate(cur):
            if idx > 10:
                break
            txt += str(row) + '\n'

        self.query_results.config(text = txt)

class LogInPage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.fg = 'white'
        self.bg = root.bg_color

        title1 = Label(self, text = "Fakebook", background = self.root.bg_color, foreground ="white")
        title1.place(x=0,y=0,width=600,height=20)

        username_label = Label(self, text="Username:", fg=self.fg, bg=self.bg, width = 20)
        username_label.place(x=20, y=60)

        self.username_entry=Entry(self, width=30, borderwidth=2)
        self.username_entry.place(x=240, y=60)

        self.password_label = Label(self, text="Password:", fg=self.fg, bg=self.bg, width = 20)
        self.password_label.place(x=20, y=100)

        self.password_entry=Entry(self, width=30, borderwidth=2)
        self.password_entry.place(x=240, y=100)

        submit_button = Button(self, text='submit', width=15, borderwidth=5, height=2,bg=self.bg,fg=self.fg, cursor='hand2', border=2, command=self.submit)
        submit_button.place(x=240, y=160)

        home_button = Button(self, text='return to home', width=15, border=2, height=2,cursor='hand2', command= lambda: self.root.raise_frame("HomePage"))
        home_button.place(x=20, y=160)

        self.place(x=0,y=0,width=1000,height=900)
    
    def submit(self):
        db = pymysql.connect(host='localhost', user='root', password='password', database='Personal_registration_form')
        cur = db.cursor()
        
        # Find password for specified user
        cur.execute("SELECT password FROM user_data WHERE username = %s", self.username_entry.get())
        
        rows = cur.fetchall()
        cur.close()
        
        if rows and rows[0] and self.password_entry.get() == rows[0][0]:
            self.root.raise_frame("UserHomePage")
        else:
            messagebox.showerror(message="wrong password. Please try again.")
            self.password_entry.delete(0, 'end')

class RegistrationPage(Frame):
    def __init__(self, root, *args):
        Frame.__init__(self, root, *args)
        self.root = root
        self.fg = 'white'
        self.bg = self.root.bg_color

        title1 = Label(self, text = "Fakebook", background = self.root.bg_color, foreground ="white")
        title1.place(x=0,y=0,width=600,height=20)

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

        self.place(x=0,y=0,width=1000,height=900)
    
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
        cur.close()

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
            self.go_back()

    def go_back(self):
        # Clear entry fields
        self.firstnameEntry.delete(0, 'end')
        self.lastnameEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.gender.set(0)  # Reset gender selection
        self.country.set('Country:')  # Reset country selection
        self.usernameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.confirmpasswordEntry.delete(0, 'end')
        self.displaypw1.set(0)  # Uncheck password display toggle
        self.displaypw2.set(0)  # Uncheck confirm password display toggle

    def place_buttons(self):
        submit1btn = Button(self, text='submit', width=15, borderwidth=5, height=2,bg=self.bg,fg=self.fg, cursor='hand2', border=2, command=self.submit)
        submit1btn.place(x=200, y=350)

        bckbtn = Button(self, text='reset', width=15, border=2, height=2,cursor='hand2', command=self.go_back)     
        bckbtn.place(x=100, y=350)

        home_button = Button(self, text='return to home', width=15, border=2, height=2,cursor='hand2', command= lambda: self.root.raise_frame("HomePage"))
        home_button.place(x=0, y=350)

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
        
        check1 = Checkbutton(self, variable= self.displaypw1,command=show1)
        check1.place(x=425, y=257)

        check2 = Checkbutton(self, variable= self.displaypw2,command=show2)
        check2.place(x=425, y=287)

    def place_country_dropdown(self):
        countryLabel=Label(self, text='Country:', fg=self.fg, bg=self.bg, width=20)
        countryLabel.place(x=0, y=200)

        countries=['Algeria', "Australia", 'Bahamas', 'Canada']

        countryLabelDropdown=OptionMenu(self, self.country, *countries)
        countryLabelDropdown.config(width=23)
        countryLabelDropdown.place(x=240, y=195)

    def place_gender_buttons(self):
        gender_label =Label(self, text='Gender:', fg=self.fg, bg=self.bg, width=20)
        gender_label.place(x=0, y=170)

        genderRadio1=Radiobutton(self, text='Male', variable=self.gender, value='Male')
        genderRadio1.place(x=240, y=170)

        genderRadio2=Radiobutton(self, text='Female', variable=self.gender, value='Female')
        genderRadio2.place(x=350, y=170)

    def place_labels_and_entries(self):
        firstname_label = Label(self, text="First Name:", fg=self.fg, bg=self.bg, width = 20)
        firstname_label.place(x=0, y=80)

        self.firstnameEntry=Entry(self, width=30, borderwidth=2)
        self.firstnameEntry.place(x=240, y=80)

        lastnamelbl = Label(self, text="Last Name:", fg=self.fg, bg=self.bg, width = 20)
        lastnamelbl.place(x=0, y=110)

        self.lastnameEntry=Entry(self, width=30, borderwidth=2)
        self.lastnameEntry.place(x=240, y=110)

        emaillbl=Label(self, text='Email:', fg=self.fg, bg=self.bg, width = 20)
        emaillbl.place(x=0, y=140)

        self.emailEntry=Entry(self, width=30, borderwidth=2)
        self.emailEntry.place(x=240, y=140)

        usernamelbl = Label(self, text='Username:', fg=self.fg, bg=self.bg, width = 20)
        usernamelbl.place(x=0, y=230)

        self.usernameEntry=Entry(self, width=30, borderwidth=2)
        self.usernameEntry.place(x=240, y=230)

        passwordlbl = Label(self, text='Password:', fg=self.fg, bg=self.bg, width = 20)
        passwordlbl.place(x=0, y=260)

        self.passwordEntry=Entry(self, width=30, borderwidth=2)
        self.passwordEntry.place(x=240, y=260)

        confirmpasswordlbl = Label(self, text='Confirm Password:',  fg=self.fg, bg=self.bg, width = 20)
        confirmpasswordlbl.place(x=0, y=290)

        self.confirmpasswordEntry=Entry(self, width=30, borderwidth=2)
        self.confirmpasswordEntry.place(x=240, y=290)

    def place_title(self):
        title = Label(self, text = "Personal Registration Form", background = self.bg, foreground = self.fg)
        title.place(x=0,y=40,width=425,height=30)

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
