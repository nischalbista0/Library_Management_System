from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.geometry("1191x670+60+30")
root.resizable(0, 0)
root.title("Library Management System")

# Read the Image
image = Image.open("images/login_window.png")

# Resize the image using resize() method
resize_image = image.resize((1191, 670))

# Displaying background image
bg = ImageTk.PhotoImage(resize_image)
bg_image = Label(root, image=bg)
bg_image.place(x=0, y=0)

admin_credentials = {'username':'admin', 'password':'admin'}

def login():
    if username.get() == '' or password.get() == '':
        messagebox.showinfo("Incomplete Information", "Please enter both username and password to continue!")

    elif username.get() != admin_credentials['username'] or password.get() != admin_credentials['password']:
        messagebox.showinfo("Incorrect Information", "Please enter correct credentials!")

    elif username.get() == admin_credentials['username'] and password.get() == admin_credentials['password']:
        root.destroy()
        window = Tk()
        window.geometry("1191x670+60+30")
        window.resizable(0, 0)
        window.title("Dashboard")

        # Functions
        def books():
            pass

        # Read the Image
        img1 = Image.open("images/dashboard.png")
        img2 = Image.open("images/admin.png")
        img3 = Image.open("images/student.png")
        img4 = Image.open("images/issue.png")
        img5 = Image.open("images/books.jpg")
        img6 = Image.open("images/return.png")

        # Resize the image using resize() method
        resized_image1 = img1.resize((1191, 670))
        resized_image2 = img2.resize((100, 105))
        resized_image3 = img3.resize((90, 80))
        resized_image4 = img4.resize((100, 80))
        resized_image5 = img5.resize((110, 100))
        resized_image6 = img6.resize((85, 80))

        # Displaying background image
        background = ImageTk.PhotoImage(resized_image1)
        background_image = Label(window, image=background)
        background_image.place(x=0, y=0)

        # Buttons
        admin_button = ImageTk.PhotoImage(resized_image2)
        admin_button_image = Button(window, image=admin_button, border=0, bg="white", activebackground="white", cursor="hand2")
        admin_button_image.place(x=545, y=175)
        Label(window, text="Librarians", bg="white", font=("Poppins", 16)).place(x=542, y=265)

        std_button = ImageTk.PhotoImage(resized_image3)
        std_button_image = Button(window, image=std_button, border=0, bg="white", activebackground="white", cursor="hand2")
        std_button_image.place(x=860, y=185)
        Label(window, text="Students", bg="white", font=("Poppins", 16)).place(x=865, y=265)

        issue_button = ImageTk.PhotoImage(resized_image4)
        issue_button_image = Button(window, image=issue_button, border=0, bg="white", activebackground="white", cursor="hand2")
        issue_button_image.place(x=375, y=420)
        Label(window, text="Issue Book", bg="white", font=("Poppins", 16)).place(x=375, y=505)

        books_button = ImageTk.PhotoImage(resized_image5)
        books_button_image = Button(window, image=books_button, border=0, bg="white", activebackground="white", cursor="hand2", command=books)
        books_button_image.place(x=215, y=170)
        Label(window, text="Books", bg="white", font=("Poppins", 16)).place(x=235, y=265)

        return_button = ImageTk.PhotoImage(resized_image6)
        return_button_image = Button(window, image=return_button, border=0, bg="white", activebackground="white", cursor="hand2")
        return_button_image.place(x=710, y=420)
        Label(window, text="Return Book", bg="white", font=("Poppins", 16)).place(x=694, y=502)

        logout_button = Button(window, text="Log Out", border=0, bg="#364954", fg="white", activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 17, "bold"), cursor="hand2")
        logout_button.place(x=1020, y=580)

        # Label
        label1 = Label(window, text="Dashboard", bg="#a7b3bb", font=("Times New Roman", 50, "bold"), fg="#151F25")
        label1.place(x=450, y=40)

        mainloop()


# Creating and placing labels
welcome_label = Label(root, text="Welcome!", bg="#a7b3bb", fg="#232E34", font=("Poppins", 24, "bold"))
welcome_label.place(x=860, y=140)

login_label = Label(root, text="Sign in to continue", bg="#a7b3bb", fg="#232E34", font=("Poppins", 16))
login_label.place(x=850, y=180)

# Creating and placing button
login_button = Button(root, text="Log In ", border=0, bg="#364954", fg="white", activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2", command=login)
login_button.place(x=885, y=410)

# Creating and placing entries
username = Entry(root, width=25, border=0, font=("Poppins", 15))
username.place(x=795, y=240)
username.focus()

password = Entry(root, width=25, border=0, font=("Poppins", 16), show="*")
password.place(x=795, y=330)

mainloop()
