from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
from datetime import date


def login_window():
    """Opens login window"""

    global username
    global password
    global root

    root = Tk()
    root.geometry("1191x670+60+30")
    root.resizable(0, 0)
    root.title("Library Management System")
    root.iconbitmap("images/icon.ico")

    # Read the Image
    image = Image.open("images/login_window.png")

    # Resize the image using resize() method
    resize_image = image.resize((1191, 670))

    # Displaying background image
    bg = ImageTk.PhotoImage(resize_image)
    bg_image = Label(root, image=bg)
    bg_image.place(x=0, y=0)

    # Creating and placing labels
    welcome_label = Label(root, text="Welcome!", bg="#a7b3bb", fg="#232E34", font=("Poppins", 24, "bold"))
    welcome_label.place(x=860, y=140)

    login_label = Label(root, text="Sign in to continue", bg="#a7b3bb", fg="#232E34", font=("Poppins", 16))
    login_label.place(x=850, y=180)

    # Creating and placing button
    login_button = Button(root, text="Log In ", border=0, bg="#364954", fg="white", activebackground="#364954",
                          activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2", command=open_dashboard)
    login_button.place(x=885, y=410)

    # Creating and placing entries
    username = Entry(root, width=25, border=0, font=("Poppins", 15))
    username.place(x=795, y=240)
    username.focus()

    password = Entry(root, width=25, border=0, font=("Poppins", 16), show="*")
    password.place(x=795, y=330)

    mainloop()


# Function that opens dashboard of librarian or student window
def open_dashboard():
    """Takes data through entries for login and opens dashboard of respective window"""

    global window
    global std_username

    std_username = username.get()

    # Connecting to students database to get students credentials
    conn = sqlite3.connect("students_database.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM student_details")

    student_records = c.fetchall()

    student_username = []
    student_password = []

    for student_record in student_records:
        student_username.append(student_record[2])
        student_password.append(student_record[3])

    conn.commit()
    conn.close()

    # Connecting to librarians database to get librarians credentials
    conn = sqlite3.connect("librarians_database.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM librarian_details")

    librarian_records = c.fetchall()

    librarian_username = []
    librarian_password = []

    for librarian_record in librarian_records:
        librarian_username.append(librarian_record[2])
        librarian_password.append(librarian_record[3])

    conn.commit()
    conn.close()

    # Show message box if username and password entry is empty
    if username.get() == '' or password.get() == '':
        messagebox.showinfo("Incomplete Information", "Please enter both username and password to continue!")

    # Student Window Login
    elif username.get() in student_username and password.get() in student_password:
        student_window = Toplevel(root)
        student_window.geometry("1191x670+60+30")
        student_window.resizable(0, 0)
        student_window.iconbitmap("images/icon.ico")
        student_window.title("Student Dashboard")

        # Read the Image
        img1 = Image.open("images/student_dashboard.png")
        img2 = Image.open("images/books.jpg")
        img3 = Image.open("images/issue.png")

        # Resize the image using resize() method
        resized_image1 = img1.resize((1191, 670))
        resized_image2 = img2.resize((110, 100))
        resized_image3 = img3.resize((100, 85))

        # Displaying background image
        background = ImageTk.PhotoImage(resized_image1)
        background_image = Label(student_window, image=background)
        background_image.place(x=0, y=0)

        def logout():
            """Destroys student window and opens login window"""

            ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=student_window)
            if ans:
                student_window.destroy()
                username.delete(0, END)
                password.delete(0, END)
                username.focus()

        # Label
        label1 = Label(student_window, text="Dashboard", bg="#a7b3bb", font=("Times New Roman", 50, "bold"),
                       fg="#151F25")
        label1.place(x=450, y=40)

        # Buttons
        books_button = ImageTk.PhotoImage(resized_image2)
        books_button_image = Button(student_window, image=books_button, border=0, bg="white", activebackground="white",
                                    cursor="hand2", command=available_books)
        books_button_image.place(x=390, y=235)
        Label(student_window, text="Available Books", bg="white", font=("Poppins", 12, "bold")).place(x=382, y=328)

        issued_books_button = ImageTk.PhotoImage(resized_image3)
        issued_books_button_image = Button(student_window, image=issued_books_button, border=0, bg="white",
                                           activebackground="white", cursor="hand2", command=my_books)
        issued_books_button_image.place(x=685, y=240)
        Label(student_window, text="My Books", bg="white", font=("Poppins", 13, "bold")).place(x=702, y=328)

        logout_button = Button(student_window, text="Log Out", border=0, bg="#364954", fg="white", activebackground="#364954",
                               activeforeground="#84B1CB", font=("Poppins", 17, "bold"), cursor="hand2", command=logout)
        logout_button.place(x=1020, y=580)

        mainloop()

    # Librarians window login
    elif username.get() in librarian_username and password.get() in librarian_password:
        window = Toplevel(root)
        window.geometry("1191x670+60+30")
        window.resizable(0, 0)
        window.iconbitmap("images/icon.ico")
        window.title("Admin Dashboard")

        def logout():
            """Destroys librarian window and opens login window"""
            ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=window)
            if ans:
                window.destroy()
                username.delete(0, END)
                password.delete(0, END)
                username.focus()

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
        admin_button_image = Button(window, image=admin_button, border=0, bg="white", activebackground="white",
                                    cursor="hand2", command=librarians_window)
        admin_button_image.place(x=545, y=175)
        Label(window, text="Librarians", bg="white", font=("Poppins", 16)).place(x=542, y=265)

        std_button = ImageTk.PhotoImage(resized_image3)
        std_button_image = Button(window, image=std_button, border=0, bg="white", activebackground="white",
                                  cursor="hand2", command=students_window)
        std_button_image.place(x=860, y=185)
        Label(window, text="Students", bg="white", font=("Poppins", 16)).place(x=865, y=265)

        issue_button = ImageTk.PhotoImage(resized_image4)
        issue_button_image = Button(window, image=issue_button, border=0, bg="white", activebackground="white",
                                    cursor="hand2", command=issue_window)
        issue_button_image.place(x=375, y=420)
        Label(window, text="Issue Book", bg="white", font=("Poppins", 16)).place(x=375, y=505)

        books_button = ImageTk.PhotoImage(resized_image5)
        books_button_image = Button(window, image=books_button, border=0, bg="white", activebackground="white",
                                    cursor="hand2", command=books_window)
        books_button_image.place(x=215, y=170)
        Label(window, text="Books", bg="white", font=("Poppins", 16)).place(x=235, y=265)

        return_button = ImageTk.PhotoImage(resized_image6)
        return_button_image = Button(window, image=return_button, border=0, bg="white", activebackground="white",
                                     cursor="hand2", command=return_window)
        return_button_image.place(x=710, y=420)
        Label(window, text="Return Book", bg="white", font=("Poppins", 16)).place(x=694, y=502)

        logout_button = Button(window, text="Log Out", border=0, bg="#364954", fg="white", activebackground="#364954",
                               activeforeground="#84B1CB", font=("Poppins", 17, "bold"), cursor="hand2", command=logout)
        logout_button.place(x=1020, y=580)

        # Label
        label1 = Label(window, text="Dashboard", bg="#a7b3bb", font=("Times New Roman", 50, "bold"), fg="#151F25")
        label1.place(x=450, y=40)

        mainloop()

    # Shows messagebox if user enter wrong credentials
    elif (username.get() not in student_username and password.get() not in student_password) or (username.get() in librarian_username and password.get() in librarian_password):
        messagebox.showinfo("Invalid Information", "Please enter correct username and password to continue!", parent=root)


def books_window():
    """Opens books window when respective button is clicked"""

    books_window = Toplevel(window)
    books_window.geometry("1191x670+60+30")
    books_window.resizable(0, 0)
    books_window.title("Books")
    books_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/management_window.png")
    resized_image = img.resize((1240, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(books_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    conn = sqlite3.connect('books_database.db')

    c = conn.cursor()

    # c.execute('''CREATE TABLE book_details(
    # Books_Name text,
    # Category text,
    # Author_Name text,
    # Language text,
    # Book_ID text,
    # Quantity integer
    # )''')

    def books_window_logout():
        """Destroys books window and opens login window"""
        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=books_window)
        if ans:
            window.destroy()
            books_window.destroy()
            username.delete(0, END)
            password.delete(0, END)
            username.focus()

    def search():
        """Takes Book ID as input and searches book of respective book ID"""

        for widgets in myFrame.winfo_children():
            widgets.destroy()

        Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 13, "bold")).grid(row=1, column=0)
        Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=20).grid(row=1,
                                                                                                                  column=1)
        Label(myFrame, text="Publication", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=13).grid(
            row=1,
            column=2)
        Label(myFrame, text="Category", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=10).grid(row=1,
                                                                                                                 column=3)
        Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=4).grid(row=1,
                                                                                                            column=4)
        Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=4).grid(
            row=1, column=5)

        if book_id.get() != '':
            conn = sqlite3.connect('books_database.db')

            c = conn.cursor()

            c.execute("SELECT *, oid FROM book_details")

            records = c.fetchall()

            roww = 2
            num = 1
            for record in records:
                if record[6] == int(book_id.get()):
                    Label(myFrame, text=num, bg="cyan", font=("MS Reference Sans Serif", 10), width=5).grid(row=0,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="cyan", font=("MS Reference Sans Serif", 10), width=30).grid(
                        row=0, column=1)
                    Label(myFrame, text=record[4], bg="cyan", font=("MS Reference Sans Serif", 10), width=20).grid(
                        row=0, column=2)
                    Label(myFrame, text=record[1], bg="cyan", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=0, column=3)
                    Label(myFrame, text=record[5], bg="cyan", font=("MS Reference Sans Serif", 10), width=6).grid(
                        row=0, column=4)
                    Label(myFrame, text=record[6], bg="cyan", font=("MS Reference Sans Serif", 10, "bold"), width=6).grid(
                        row=0, column=5)

                if record[6] > 0:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=30).grid(
                        row=roww, column=1)
                    Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=20).grid(
                        row=roww, column=2)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww, column=3)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(
                        row=roww, column=4)
                    Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=6).grid(
                        row=roww, column=5)

                    roww += 1
                    num += 1

                myFrame.config(bg="white")

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid Book ID to continue!", parent=books_window)

    def add_book_window():
        """Opens 'Add Book' window"""

        add = Toplevel()
        add.title("Add Book")
        add.geometry("1191x670+60+30")
        add.resizable(0, 0)
        add.iconbitmap("images/icon.ico")

        # Read the Image
        image = Image.open("images/add_and_update.png")

        # Resize the image using resize() method
        resize_image = image.resize((1191, 670))

        # Displaying background image
        bg = ImageTk.PhotoImage(resize_image)
        bg_image = Label(add, image=bg)
        bg_image.place(x=0, y=0)

        def add_book():
            """Adds data of book's details into the database"""

            if book_name.get() != '' and category.get() != '' and author_name.get() != '' and language.get() != '' and\
                    publication.get() != '' and quantity.get() != '':

                conn = sqlite3.connect("books_database.db")

                # Create cursor
                c = conn.cursor()

                # Insert into table
                c.execute(
                    "INSERT INTO book_details VALUES (:Book_Name, :Category, :Author_Name, :Language, :Publication, :Quantity)",
                    {
                        'Book_Name': book_name.get(),
                        'Category': category.get(),
                        'Author_Name': author_name.get(),
                        'Language': language.get(),
                        'Publication': publication.get(),
                        'Quantity': quantity.get(),
                    })

                # query of the database
                c.execute("SELECT *, oid FROM book_details")

                # print(records)
                records = c.fetchall()

                roww = 1
                num = 1
                for record in records:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=30).grid(
                        row=roww, column=1)
                    Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=20).grid(
                        row=roww, column=2)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww, column=3)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(
                        row=roww, column=4)
                    Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=6).grid(
                        row=roww, column=5)

                    roww += 1
                    num += 1

                conn.commit()
                conn.close()
                add.destroy()

            else:
                messagebox.showinfo("Incomplete Information", "Please fill all the entries to continue!", parent=add)

        def clear_add_window():
            """Clears all the entries of "Add Book' window"""
            entries = [book_name, category, author_name, language, publication, quantity]
            for entry in entries:
                entry.delete(0, END)

        # Creating and placing labels
        label1 = Label(add, text="Book Name", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label1.place(x=175, y=150)

        label2 = Label(add, text="Category", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label2.place(x=630, y=150)

        label3 = Label(add, text="Author Name", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label3.place(x=178, y=250)

        label4 = Label(add, text="Language", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label4.place(x=630, y=250)

        label5 = Label(add, text="Publication", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label5.place(x=175, y=353)

        label6 = Label(add, text="Quantity", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label6.place(x=630, y=353)

        # Creating and placing entries
        book_name = Entry(add, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        book_name.place(x=180, y=185)
        book_name.focus()

        category = Entry(add, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        category.place(x=635, y=185)

        author_name = Entry(add, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        author_name.place(x=180, y=285)

        language = Entry(add, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        language.place(x=635, y=285)

        publication = Entry(add, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        publication.place(x=180, y=388)

        quantity = Entry(add, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        quantity.place(x=635, y=388)

        # Creating and placing buttons
        add_button = Button(add, text="Add", border=0, bg="#364954", fg="white", activebackground="#364954",
                            activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2", command=add_book)
        add_button.place(x=477, y=506)

        clear_button = Button(add, text="Clear", border=0, bg="#364954", fg="white", activebackground="#364954",
                              activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                              command=clear_add_window)
        clear_button.place(x=655, y=506)

        mainloop()

    def update_book_window():
        """Opens 'Update Book' window"""
        if book_id.get() != '':
            update_window = Toplevel()
            update_window.title("Update Book")
            update_window.geometry("1191x670+60+30")
            update_window.resizable(0, 0)
            update_window.iconbitmap("images/icon.ico")

            # Read the Image
            image = Image.open("images/add_and_update.png")

            # Resize the image using resize() method
            resize_image = image.resize((1191, 670))

            # Displaying background image
            bg = ImageTk.PhotoImage(resize_image)
            bg_image = Label(update_window, image=bg)
            bg_image.place(x=0, y=0)

            def update_book():
                """Updates data of book's details into the database"""
                # Create a databases or connect to one
                conn = sqlite3.connect("books_database.db")

                # Create cursor
                c = conn.cursor()
                record_id = book_id.get()

                c.execute(""" UPDATE book_details SET
                                    Books_Name = :books_name,
                                    Category = :category,
                                    Author_Name = :author_name,
                                    Language = :language,
                                    Publication = :publication,
                                    Quantity = :quantity
                                    WHERE oid = :oid""",
                          {'books_name': book_name.get(),
                           'category': category.get(),
                           'author_name': author_name.get(),
                           'language': language.get(),
                           'publication': publication.get(),
                           'quantity': quantity.get(),
                           'oid': record_id

                           }
                          )

                update_window.destroy()

                # query of the database
                c.execute("SELECT *, oid FROM book_details")

                records = c.fetchall()

                # Loop through the results
                roww = 1
                num = 1
                for record in records:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=30).grid(
                        row=roww, column=1)
                    Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=20).grid(
                        row=roww, column=2)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww, column=3)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(
                        row=roww, column=4)
                    Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=6).grid(
                        row=roww, column=5)

                    roww += 1
                    num += 1

                conn.commit()
                conn.close()

            def clear_update_window():
                """Clears all the entries of 'Uodate Book' window"""
                entries = [book_name, category, author_name, language, publication, quantity]
                for entry in entries:
                    entry.delete(0, END)

            # Create a databases or connect to one
            conn = sqlite3.connect("books_database.db")

            # Create cursor
            c = conn.cursor()

            # Creating and placing labels
            label1 = Label(update_window, text="Book Name", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label1.place(x=175, y=150)

            label2 = Label(update_window, text="Category", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label2.place(x=630, y=150)

            label3 = Label(update_window, text="Author Name", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label3.place(x=178, y=250)

            label4 = Label(update_window, text="Language", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label4.place(x=630, y=250)

            label5 = Label(update_window, text="Publication", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label5.place(x=175, y=353)

            label6 = Label(update_window, text="Quantity", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label6.place(x=630, y=353)

            # Creating and placing entries
            book_name = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            book_name.place(x=180, y=185)
            book_name.focus()

            category = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            category.place(x=635, y=185)

            author_name = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            author_name.place(x=180, y=285)

            language = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            language.place(x=635, y=285)

            publication = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            publication.place(x=180, y=388)

            quantity = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            quantity.place(x=635, y=388)

            # Creating and placing buttons
            update_button = Button(update_window, text="Update", border=0, bg="#364954", fg="white", activebackground="#364954",
                                activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                                command=update_book)
            update_button.place(x=467, y=506)

            clear_button = Button(update_window, text="Clear", border=0, bg="#364954", fg="white", activebackground="#364954",
                                  activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                                  command=clear_update_window)
            clear_button.place(x=655, y=506)

            id = book_id.get()

            c.execute("SELECT * FROM book_details WHERE oid=" + id)
            records = c.fetchall()

            # loop through the results
            for record in records:
                book_name.insert(0, record[0])
                category.insert(0, record[1])
                author_name.insert(0, record[2])
                language.insert(0, record[3])
                publication.insert(0, record[4])
                quantity.insert(0, record[5])

            conn.commit()
            conn.close()

            mainloop()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid Book ID to continue!", parent=books_window)

    def remove_book():
        """Removes data of book's details from the database"""
        if book_id.get() != '':
            # create database
            conn = sqlite3.connect("books_database.db")

            # create cursor
            c = conn.cursor()

            # delete a record
            c.execute("DELETE from book_details WHERE oid = " + book_id.get())

            # query of the database
            c.execute("SELECT *, oid FROM book_details")

            records = c.fetchall()

            # Loop through the results
            roww = 1
            num = 1
            for record in records:
                Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                         column=0)
                Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=30).grid(
                    row=roww, column=1)
                Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=18).grid(
                    row=roww, column=2)
                Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                    row=roww, column=3)
                Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(row=roww,
                                                                                                               column=4)
                Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(row=roww,
                                                                                                               column=5)

                roww += 1
                num += 1

            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=0)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=30).grid(row=roww, column=1)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=20).grid(row=roww, column=2)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww, column=3)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(row=roww, column=4)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=6).grid(row=roww, column=5)

            book_id.delete(0, END)

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid book ID to continue.", parent=books_window)

    # Buttons
    search_button = Button(books_window, text="Search", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2", command=search)
    search_button.place(x=295, y=169)

    add_button = Button(books_window, text="Add Book", border=0, bg="#364954", fg="white",
                        activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                        cursor="hand2", command=add_book_window)
    add_button.place(x=165, y=297)

    update_button = Button(books_window, text="Update Book", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2", command=update_book_window)
    update_button.place(x=150, y=370)

    remove_button = Button(books_window, text="Remove Book", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2", command=remove_book)
    remove_button.place(x=150, y=440)

    exit_button = Button(books_window, text="Exit", border=0, bg="#364954", fg="white",
                         activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                         cursor="hand2", command=books_window.destroy)
    exit_button.place(x=198, y=525)

    books_window_logout = Button(books_window, text="Log Out", border=0, bg="#364954", fg="white",
                                 activebackground="#364954", activeforeground="#84B1CB",
                                 font=("Poppins", 14, "bold"), cursor="hand2", command=books_window_logout)
    books_window_logout.place(x=1013, y=597)

    # Entry
    book_id = Entry(books_window, width=18, border=0, bg="#a7b3bb", font=("Poppins", 15))
    book_id.place(x=67, y=178)
    book_id.focus()

    # Label
    Label(books_window, text="Menu", bg="#a7b3bb", font=("Times New Roman", 19)).place(x=77, y=85)

    # Create Frame with scrollbar
    cover = LabelFrame(books_window, height=800, width=1000, bd=0)
    cover.place(x=416, y=105)

    myCanvas = Canvas(cover, height=472, width=676, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 13, "bold")).grid(row=0, column=0)
    Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=20).grid(row=0,
                                                                                                              column=1)
    Label(myFrame, text="Publication", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=13).grid(row=0,
                                                                                                                column=2)
    Label(myFrame, text="Category", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=10).grid(row=0,
                                                                                                             column=3)
    Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=4).grid(row=0, column=4)
    Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=4).grid(row=0, column=5)

    c.execute("SELECT *,oid FROM book_details")

    records = c.fetchall()

    roww = 1
    num = 1

    for record in records:
        Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=0)
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=30).grid(row=roww, column=1)
        Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=20).grid(row=roww, column=2)
        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww, column=3)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=6).grid(row=roww, column=4)
        Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=6).grid(row=roww, column=5)

        roww += 1
        num += 1

    conn.commit()
    conn.close()

    mainloop()


def librarians_window():
    """Opens librarian window when respective button is clicked"""
    librarians_window = Toplevel(window)
    librarians_window.geometry("1191x670+60+30")
    librarians_window.resizable(0, 0)
    librarians_window.title("Librarians")
    librarians_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/management_window.png")
    resized_image = img.resize((1240, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(librarians_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    conn = sqlite3.connect('librarians_database.db')

    c = conn.cursor()

    # c.execute('''CREATE TABLE librarian_details(
    # Librarian_Name text,
    # Librarian_ID integer,
    # Username text,
    # Password text,
    # Email text,
    # Contact_Num integer
    # )''')

    def librarians_window_logout():
        """Destroys librarian window and opens login window"""
        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=librarians_window)
        if ans:
            window.destroy()
            librarians_window.destroy()
            username.delete(0, END)
            password.delete(0, END)
            username.focus()

    def search():
        """Takes librarian ID as input and searches librarian of respective ID"""
        for widgets in myFrame.winfo_children():
            widgets.destroy()

        Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 12, "bold")).grid(row=1, column=0)
        Label(myFrame, text="Librarian Name", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=15).grid(
            row=1,
            column=1)
        Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=8).grid(row=1,
                                                                                                          column=2)
        Label(myFrame, text="Username", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=1,
                                                                                                                 column=3)
        Label(myFrame, text="Password", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=1,
                                                                                                                 column=4)
        Label(myFrame, text="Contact", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=10).grid(row=1,
                                                                                                                column=5)

        if librarians_id.get() != '':
            conn = sqlite3.connect('librarians_database.db')

            c = conn.cursor()

            c.execute("SELECT *, oid FROM librarian_details")

            records = c.fetchall()

            roww = 2
            num = 1
            for record in records:
                if record[1] == int(librarians_id.get()):
                    Label(myFrame, text=num, bg="cyan", font=("MS Reference Sans Serif", 10), width=5).grid(row=0,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="cyan", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=0, column=1)
                    Label(myFrame, text=record[1], bg="cyan", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=0, column=2)
                    Label(myFrame, text=record[2], bg="cyan", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=0, column=3)
                    Label(myFrame, text=record[3], bg="cyan", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=0, column=4)
                    Label(myFrame, text=record[5], bg="cyan", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=0, column=5)

                if record[1] > 0:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=roww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=roww,
                        column=2)
                    Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=3)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=4)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=roww,
                        column=5)

                    roww += 1
                    num += 1

                myFrame.config(bg="white")

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid Librarian ID to continue!", parent=librarians_window)

    def add_librarian_window():
        """Opens 'Add Librarian' window"""
        add_window = Toplevel()
        add_window.title("Add Librarian")
        add_window.geometry("1191x670+60+30")
        add_window.resizable(0, 0)
        add_window.iconbitmap("images/icon.ico")

        # Read the Image
        image = Image.open("images/add_and_update.png")

        # Resize the image using resize() method
        resize_image = image.resize((1191, 670))

        # Displaying background image
        bg = ImageTk.PhotoImage(resize_image)
        bg_image = Label(add_window, image=bg)
        bg_image.place(x=0, y=0)

        def add_librarian():
            """Adds data of librarian's details into the database"""
            if librarian_name.get() != '' and librarian_ID.get() != '' and username.get() != '' and password.get() != '' and\
                    email.get() != '' and contact_num.get() != '':

                conn = sqlite3.connect("librarians_database.db")

                # Create cursor
                c = conn.cursor()

                # Insert into table
                c.execute(
                    "INSERT INTO librarian_details VALUES (:Librarian_Name, :Librarian_ID, :Username, :Password, :Email, :Contact_Num)",
                    {
                        'Librarian_Name': librarian_name.get(),
                        'Librarian_ID': librarian_ID.get(),
                        'Username': username.get(),
                        'Password': password.get(),
                        'Email': email.get(),
                        'Contact_Num': contact_num.get(),
                    })

                # query of the database
                c.execute("SELECT *, oid FROM librarian_details")

                # print(records)
                records = c.fetchall()

                roww = 1
                num = 1
                for record in records:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=roww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=roww,
                        column=2)
                    Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=3)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=4)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=roww,
                        column=5)

                    roww += 1
                    num += 1

                conn.commit()
                conn.close()
                add_window.destroy()

            else:
                messagebox.showinfo("Incomplete Information", "Please fill all entries to continue!", parent=add_window)

        def clear_add_window():
            """Clears all the entries of 'Add Librarian' window"""
            entries = [librarian_name, librarian_ID, username, password, email, contact_num]
            for entry in entries:
                entry.delete(0, END)

        # Creating and placing labels
        label1 = Label(add_window, text="Librarian Name", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label1.place(x=175, y=150)

        label2 = Label(add_window, text="Librarian ID", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label2.place(x=630, y=150)

        label3 = Label(add_window, text="Username", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label3.place(x=178, y=250)

        label4 = Label(add_window, text="Password", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label4.place(x=630, y=250)

        label5 = Label(add_window, text="E-mail", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label5.place(x=175, y=353)

        label6 = Label(add_window, text="Contact Number", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb", fg="#232E34")
        label6.place(x=630, y=353)

        # Creating and placing entries
        librarian_name = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        librarian_name.place(x=180, y=185)
        librarian_name.focus()

        librarian_ID = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        librarian_ID.place(x=635, y=185)

        username = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        username.place(x=180, y=285)

        password = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        password.place(x=635, y=285)

        email = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        email.place(x=180, y=388)

        contact_num = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        contact_num.place(x=635, y=388)

        # Creating and placing buttons
        add_button = Button(add_window, text="Add", border=0, bg="#364954", fg="white", activebackground="#364954",
                            activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2", command=add_librarian)
        add_button.place(x=477, y=506)

        clear_button = Button(add_window, text="Clear", border=0, bg="#364954", fg="white", activebackground="#364954",
                              activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                              command=clear_add_window)
        clear_button.place(x=655, y=506)

        mainloop()

    def update_librarian_window():
        """Opens 'Update Librarian' window"""
        if librarians_id.get() != '':
            update_window = Toplevel()
            update_window.title("Update Librarian")
            update_window.geometry("1191x670+60+30")
            update_window.resizable(0, 0)
            update_window.iconbitmap("images/icon.ico")

            # Read the Image
            image = Image.open("images/add_and_update.png")

            # Resize the image using resize() method
            resize_image = image.resize((1191, 670))

            # Displaying background image
            bg = ImageTk.PhotoImage(resize_image)
            bg_image = Label(update_window, image=bg)
            bg_image.place(x=0, y=0)

            def update_librarian():
                """Updates data of librarian's details in the database"""
                # Create a databases or connect to one
                conn = sqlite3.connect("librarians_database.db")

                # Create cursor
                c = conn.cursor()
                record_id = librarians_id.get()

                c.execute(""" UPDATE librarian_details SET
                                    Librarian_Name = :librarian_name,
                                    Librarian_ID = :librarian_id,
                                    Username = :username,
                                    Password = :password,
                                    Email = :email,
                                    Contact_Num = :contact_num
                                    WHERE Librarian_ID = :id""",
                          {'librarian_name': librarian_name.get(),
                           'librarian_id': librarian_ID.get(),
                           'username': username.get(),
                           'password': password.get(),
                           'email': email.get(),
                           'contact_num': contact_num.get(),
                           'id': record_id

                           }
                          )

                update_window.destroy()

                # query of the database
                c.execute("SELECT *, oid FROM librarian_details")

                records = c.fetchall()

                # Loop through the results
                roww = 1
                num = 1
                for record in records:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=roww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=roww,
                        column=2)
                    Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=3)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=4)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=roww,
                        column=5)

                    roww += 1
                    num += 1

                conn.commit()
                conn.close()

            def clear_update_window():
                """Clears all the entries of 'Update Librarian' window"""
                entries = [librarian_name, librarian_ID, username, password, email, contact_num]
                for entry in entries:
                    entry.delete(0, END)

            # Create a databases or connect to one
            conn = sqlite3.connect("librarians_database.db")

            # Create cursor
            c = conn.cursor()

            # Creating and placing labels
            label1 = Label(update_window, text="Librarian Name", font=("MS Reference Sans Serif", 16, "bold"),
                           bg="#a7b3bb", fg="#232E34")
            label1.place(x=175, y=150)

            label2 = Label(update_window, text="Librarian ID", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label2.place(x=630, y=150)

            label3 = Label(update_window, text="Username", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label3.place(x=178, y=250)

            label4 = Label(update_window, text="Password", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label4.place(x=630, y=250)

            label5 = Label(update_window, text="E-mail", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label5.place(x=175, y=353)

            label6 = Label(update_window, text="Contact Number", font=("MS Reference Sans Serif", 16, "bold"),
                           bg="#a7b3bb", fg="#232E34")
            label6.place(x=630, y=353)

            # Creating and placing entries
            librarian_name = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                                   fg="black")
            librarian_name.place(x=180, y=185)
            librarian_name.focus()

            librarian_ID = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                                 fg="black")
            librarian_ID.place(x=635, y=185)

            username = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            username.place(x=180, y=285)

            password = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            password.place(x=635, y=285)

            email = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            email.place(x=180, y=388)

            contact_num = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                                fg="black")
            contact_num.place(x=635, y=388)

            # Creating and placing buttons
            update_button = Button(update_window, text="Update", border=0, bg="#364954", fg="white", activebackground="#364954",
                                activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                                command=update_librarian)
            update_button.place(x=465, y=506)

            clear_button = Button(update_window, text="Clear", border=0, bg="#364954", fg="white",
                                  activebackground="#364954",
                                  activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                                  command=clear_update_window)
            clear_button.place(x=655, y=506)

            id = librarians_id.get()

            c.execute("SELECT * FROM librarian_details WHERE Librarian_ID=" + id)
            records = c.fetchall()

            # loop through the results
            for record in records:
                librarian_name.insert(0, record[0])
                librarian_ID.insert(0, record[1])
                username.insert(0, record[2])
                password.insert(0, record[3])
                email.insert(0, record[4])
                contact_num.insert(0, record[5])

            conn.commit()
            conn.close()

            mainloop()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid Librarian ID to continue!", parent=librarians_window)

    def remove_librarian():
        """Removes data of librarian's details from the database"""
        if librarians_id.get() != '':
            # create database
            conn = sqlite3.connect("librarians_database.db")

            # create cursor
            c = conn.cursor()

            # delete a record
            c.execute("DELETE from librarian_details WHERE Librarian_ID = " + librarians_id.get())

            # query of the database
            c.execute("SELECT *, oid FROM librarian_details")

            records = c.fetchall()

            # Loop through the results
            roww = 1
            num = 1
            for record in records:
                Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                         column=0)
                Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                    row=roww,
                    column=1)
                Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                    row=roww,
                    column=2)
                Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                    row=roww,
                    column=3)
                Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                    row=roww,
                    column=4)
                Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                    row=roww,
                    column=5)

                roww += 1
                num += 1

            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=0)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(row=roww, column=1)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(row=roww, column=2)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww, column=3)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww, column=4)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(row=roww, column=5)

            librarians_id.delete(0, END)

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid book ID to continue.", parent=librarians_window)


    # Buttons
    search_button = Button(librarians_window, text="Search", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2", command=search)
    search_button.place(x=295, y=169)

    add_button = Button(librarians_window, text="Add Librarian", border=0, bg="#364954", fg="white",
                        activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                        cursor="hand2", command=add_librarian_window)
    add_button.place(x=155, y=297)

    update_button = Button(librarians_window, text="Update Librarian", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2", command=update_librarian_window)
    update_button.place(x=137, y=370)

    remove_button = Button(librarians_window, text="Remove Librarian", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2", command=remove_librarian)
    remove_button.place(x=132, y=442)

    exit_button = Button(librarians_window, text="Exit", border=0, bg="#364954", fg="white", activebackground="#364954",
                         activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2", command=librarians_window.destroy)
    exit_button.place(x=198, y=525)

    librarians_window_logout = Button(librarians_window, text="Log Out", border=0, bg="#364954", fg="white",
                                      activebackground="#364954", activeforeground="#84B1CB",
                                      font=("Poppins", 14, "bold"), cursor="hand2", command=librarians_window_logout)
    librarians_window_logout.place(x=1013, y=597)

    # Entry
    librarians_id = Entry(librarians_window, width=18, border=0, bg="#a7b3bb", font=("Poppins", 15))
    librarians_id.place(x=67, y=178)
    librarians_id.focus()

    # Label
    Label(librarians_window, text="Menu", bg="#a7b3bb", font=("Times New Roman", 19)).place(x=77, y=85)

    # Create Frame with scrollbar
    cover = LabelFrame(librarians_window, height=800, width=1000, bd=0)
    cover.place(x=416, y=105)

    myCanvas = Canvas(cover, height=472, width=676, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 12, "bold")).grid(row=0, column=0)
    Label(myFrame, text="Librarian Name", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=15).grid(row=0,
                                                                                                              column=1)
    Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=8).grid(row=0,
                                                                                                                column=2)
    Label(myFrame, text="Username", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=0,
                                                                                                             column=3)
    Label(myFrame, text="Password", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=0, column=4)
    Label(myFrame, text="Contact", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=10).grid(row=0, column=5)

    c.execute("SELECT *,oid FROM librarian_details")

    records = c.fetchall()

    roww = 1
    num = 1

    for record in records:
        Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=0)
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(row=roww,
                                                                                                        column=1)
        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(row=roww,
                                                                                                        column=2)
        Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww,
                                                                                                        column=3)
        Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww,
                                                                                                       column=4)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(row=roww,
                                                                                                               column=5)

        roww += 1
        num += 1

    conn.commit()
    conn.close()

    mainloop()


# Function that opens student window
def students_window():
    """Opens student window when respective button is clicked"""
    students_window = Toplevel(window)
    students_window.geometry("1191x670+60+30")
    students_window.resizable(0, 0)
    students_window.title("Students")
    students_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/management_window.png")
    resized_image = img.resize((1240, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(students_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    conn = sqlite3.connect('students_database.db')

    c = conn.cursor()

    # c.execute('''CREATE TABLE student_details(
    # Student_Name text,
    # Student_ID integer,
    # Username text,
    # Password text,
    # Email text,
    # Contact_Num integer
    # )''')

    def students_window_logout():
        """Destroys student window and opens login window"""
        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=students_window)
        if ans:
            window.destroy()
            students_window.destroy()
            username.delete(0, END)
            password.delete(0, END)
            username.focus()

    def search():
        """Takes student ID as input and searches student with respective ID"""
        for widgets in myFrame.winfo_children():
            widgets.destroy()

        Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 12, "bold")).grid(row=1, column=0)
        Label(myFrame, text="Student Name", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=15).grid(
            row=1,
            column=1)
        Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=8).grid(row=1,
                                                                                                          column=2)
        Label(myFrame, text="Username", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=1,
                                                                                                                 column=3)
        Label(myFrame, text="Password", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=1,
                                                                                                                 column=4)
        Label(myFrame, text="Contact", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=10).grid(row=1,
                                                                                                                column=5)

        if student_id.get() != '':
            conn = sqlite3.connect('students_database.db')

            c = conn.cursor()

            c.execute("SELECT *, oid FROM student_details")

            records = c.fetchall()

            roww = 2
            num = 1
            for record in records:
                if record[1] == int(student_id.get()):
                    Label(myFrame, text=num, bg="cyan", font=("MS Reference Sans Serif", 10), width=5).grid(row=0,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="cyan", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=0, column=1)
                    Label(myFrame, text=record[1], bg="cyan", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=0, column=2)
                    Label(myFrame, text=record[2], bg="cyan", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=0, column=3)
                    Label(myFrame, text=record[3], bg="cyan", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=0, column=4)
                    Label(myFrame, text=record[5], bg="cyan", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=0, column=5)

                if record[1] > 0:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=roww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=roww,
                        column=2)
                    Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=3)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=4)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=roww,
                        column=5)

                    roww += 1
                    num += 1

                myFrame.config(bg="white")

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Student ID", "Please enter valid Student ID to continue!", parent=students_window)

    def add_student_window():
        """Opens 'Add Student' window"""
        add_window = Toplevel()
        add_window.title("Add Student")
        add_window.geometry("1191x670+60+30")
        add_window.resizable(0, 0)
        add_window.iconbitmap("images/icon.ico")

        # Read the Image
        image = Image.open("images/add_and_update.png")

        # Resize the image using resize() method
        resize_image = image.resize((1191, 670))

        # Displaying background image
        bg = ImageTk.PhotoImage(resize_image)
        bg_image = Label(add_window, image=bg)
        bg_image.place(x=0, y=0)

        def add_student():
            """Adds data of student's details into the database"""
            if student_name.get() != '' and student_ID.get() != '' and username.get() != '' and password.get() != '' and \
                    email.get() != '' and contact_num.get() != '':

                conn = sqlite3.connect("students_database.db")

                # Create cursor
                c = conn.cursor()

                # Insert into table
                c.execute(
                    "INSERT INTO student_details VALUES (:Student_Name, :Student_ID, :Username, :Password, :Email, :Contact_Num)",
                    {
                        'Student_Name': student_name.get(),
                        'Student_ID': student_ID.get(),
                        'Username': username.get(),
                        'Password': password.get(),
                        'Email': email.get(),
                        'Contact_Num': contact_num.get(),
                    })

                # query of the database
                c.execute("SELECT *, oid FROM student_details")

                # print(records)
                records = c.fetchall()

                roww = 1
                num = 1
                for record in records:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=roww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=roww,
                        column=2)
                    Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=3)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=4)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=roww,
                        column=5)

                    roww += 1
                    num += 1

                conn.commit()
                conn.close()
                add_window.destroy()

            else:
                messagebox.showinfo("Incomplete Information", "Please fill all entries to continue!", parent=students_window)

        def clear_add_window():
            """Clears all the entries of 'Add Student' window"""
            entries = [student_name, student_ID, username, password, email, contact_num]
            for entry in entries:
                entry.delete(0, END)

        # Creating and placing labels
        label1 = Label(add_window, text="Student Name", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label1.place(x=175, y=150)

        label2 = Label(add_window, text="Student ID", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label2.place(x=630, y=150)

        label3 = Label(add_window, text="Username", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label3.place(x=178, y=250)

        label4 = Label(add_window, text="Password", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label4.place(x=630, y=250)

        label5 = Label(add_window, text="E-mail", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label5.place(x=175, y=353)

        label6 = Label(add_window, text="Contact Number", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                       fg="#232E34")
        label6.place(x=630, y=353)

        # Creating and placing entries
        student_name = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                               fg="black")
        student_name.place(x=180, y=185)
        student_name.focus()

        student_ID = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        student_ID.place(x=635, y=185)

        username = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        username.place(x=180, y=285)

        password = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        password.place(x=635, y=285)

        email = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        email.place(x=180, y=388)

        contact_num = Entry(add_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
        contact_num.place(x=635, y=388)

        # Creating and placing buttons
        add_button = Button(add_window, text="Add", border=0, bg="#364954", fg="white", activebackground="#364954",
                            activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                            command=add_student)
        add_button.place(x=477, y=506)

        clear_button = Button(add_window, text="Clear", border=0, bg="#364954", fg="white", activebackground="#364954",
                              activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                              command=clear_add_window)
        clear_button.place(x=655, y=506)

        mainloop()

    def update_student_window():
        """Opens 'Update Student' window"""
        if student_id.get() != '':
            update_window = Toplevel()
            update_window.title("Update Student")
            update_window.geometry("1191x670+60+30")
            update_window.resizable(0, 0)
            update_window.iconbitmap("images/icon.ico")

            # Read the Image
            image = Image.open("images/add_and_update.png")

            # Resize the image using resize() method
            resize_image = image.resize((1191, 670))

            # Displaying background image
            bg = ImageTk.PhotoImage(resize_image)
            bg_image = Label(update_window, image=bg)
            bg_image.place(x=0, y=0)

            def update_student():
                """Updates data of student's details in the database"""
                # Create a databases or connect to one
                conn = sqlite3.connect("students_database.db")

                # Create cursor
                c = conn.cursor()
                record_id = student_id.get()

                c.execute(""" UPDATE student_details SET
                                    Student_Name = :student_name,
                                    Student_ID = :student_id,
                                    Username = :username,
                                    Password = :password,
                                    Email = :email,
                                    Contact_Num = :contact_num
                                    WHERE Student_ID = :id""",
                          {'student_name': student_name.get(),
                           'student_id': student_ID.get(),
                           'username': username.get(),
                           'password': password.get(),
                           'email': email.get(),
                           'contact_num': contact_num.get(),
                           'id': record_id

                           }
                          )

                update_window.destroy()

                # query of the database
                c.execute("SELECT *, oid FROM student_details")

                records = c.fetchall()

                # Loop through the results
                roww = 1
                num = 1
                for record in records:
                    Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                             column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                        row=roww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                        row=roww,
                        column=2)
                    Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=3)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                        row=roww,
                        column=4)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                        row=roww,
                        column=5)

                    roww += 1
                    num += 1

                conn.commit()
                conn.close()

            def clear_update_window():
                """Clears all the entries of 'Update Student' window"""
                entries = [student_name, student_ID, username, password, email, contact_num]
                for entry in entries:
                    entry.delete(0, END)

            # Create a databases or connect to one
            conn = sqlite3.connect("students_database.db")

            # Create cursor
            c = conn.cursor()

            # Creating and placing labels
            label1 = Label(update_window, text="Student Name", font=("MS Reference Sans Serif", 16, "bold"),
                           bg="#a7b3bb", fg="#232E34")
            label1.place(x=175, y=150)

            label2 = Label(update_window, text="Student ID", font=("MS Reference Sans Serif", 16, "bold"),
                           bg="#a7b3bb",
                           fg="#232E34")
            label2.place(x=630, y=150)

            label3 = Label(update_window, text="Username", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label3.place(x=178, y=250)

            label4 = Label(update_window, text="Password", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label4.place(x=630, y=250)

            label5 = Label(update_window, text="E-mail", font=("MS Reference Sans Serif", 16, "bold"), bg="#a7b3bb",
                           fg="#232E34")
            label5.place(x=175, y=353)

            label6 = Label(update_window, text="Contact Number", font=("MS Reference Sans Serif", 16, "bold"),
                           bg="#a7b3bb", fg="#232E34")
            label6.place(x=630, y=353)

            # Creating and placing entries
            student_name = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                                   fg="black")
            student_name.place(x=180, y=185)
            student_name.focus()

            student_ID = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                                 fg="black")
            student_ID.place(x=635, y=185)

            username = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                             fg="black")
            username.place(x=180, y=285)

            password = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                             fg="black")
            password.place(x=635, y=285)

            email = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb", fg="black")
            email.place(x=180, y=388)

            contact_num = Entry(update_window, bd=0, font=("MS Reference Sans Serif", 15), width=28, bg="#a7b3bb",
                                fg="black")
            contact_num.place(x=635, y=388)

            # Creating and placing buttons
            update_button = Button(update_window, text="Update", border=0, bg="#364954", fg="white",
                                   activebackground="#364954",
                                   activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                                   command=update_student)
            update_button.place(x=465, y=506)

            clear_button = Button(update_window, text="Clear", border=0, bg="#364954", fg="white",
                                  activebackground="#364954",
                                  activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                                  command=clear_update_window)
            clear_button.place(x=655, y=506)

            id = student_id.get()

            c.execute("SELECT * FROM student_details WHERE Student_ID=" + id)
            records = c.fetchall()

            # loop through the results
            for record in records:
                student_name.insert(0, record[0])
                student_ID.insert(0, record[1])
                username.insert(0, record[2])
                password.insert(0, record[3])
                email.insert(0, record[4])
                contact_num.insert(0, record[5])

            conn.commit()
            conn.close()

            mainloop()

        else:
            messagebox.showinfo("Invalid Student ID", "Please enter valid Student ID to continue!", parent=books_window)

    def remove_student():
        """Remove data of student detail's from the database"""
        if student_id.get() != '':
            # create database
            conn = sqlite3.connect("students_database.db")

            # create cursor
            c = conn.cursor()

            # delete a record
            c.execute("DELETE from student_details WHERE Student_ID = " + student_id.get())

            # query of the database
            c.execute("SELECT *, oid FROM student_details")

            records = c.fetchall()

            # Loop through the results
            roww = 1
            num = 1
            for record in records:
                Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww,
                                                                                                         column=0)
                Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(
                    row=roww,
                    column=1)
                Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(
                    row=roww,
                    column=2)
                Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                    row=roww,
                    column=3)
                Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(
                    row=roww,
                    column=4)
                Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(
                    row=roww,
                    column=5)

                roww += 1
                num += 1

            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=0)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(row=roww, column=1)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(row=roww, column=2)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww, column=3)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww, column=4)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(row=roww, column=5)

            student_id.delete(0, END)

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid book ID to continue.", parent=students_window)

    # Buttons
    search_button = Button(students_window, text="Search", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2", command=search)
    search_button.place(x=295, y=169)

    add_button = Button(students_window, text="Add Student", border=0, bg="#364954", fg="white",
                        activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                        cursor="hand2", command=add_student_window)
    add_button.place(x=155, y=297)

    update_button = Button(students_window, text="Update Student", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2", command=update_student_window)
    update_button.place(x=142, y=370)

    remove_button = Button(students_window, text="Remove Student", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2", command=remove_student)
    remove_button.place(x=139, y=442)

    exit_button = Button(students_window, text="Exit", border=0, bg="#364954", fg="white", activebackground="#364954",
                         activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2",
                         command=students_window.destroy)
    exit_button.place(x=198, y=525)

    students_window_logout = Button(students_window, text="Log Out", border=0, bg="#364954", fg="white",
                                    activebackground="#364954", activeforeground="#84B1CB",
                                    font=("Poppins", 14, "bold"), cursor="hand2", command=students_window_logout)
    students_window_logout.place(x=1013, y=597)

    # Entry
    student_id = Entry(students_window, width=18, border=0, bg="#a7b3bb", font=("Poppins", 15))
    student_id.place(x=67, y=178)
    student_id.focus()

    # Label
    Label(students_window, text="Menu", bg="#a7b3bb", font=("Times New Roman", 19)).place(x=77, y=85)

    # Create Frame with scrollbar
    cover = LabelFrame(students_window, height=800, width=1000, bd=0)
    cover.place(x=416, y=105)

    myCanvas = Canvas(cover, height=472, width=676, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 12, "bold")).grid(row=0, column=0)
    Label(myFrame, text="Student Name", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=15).grid(
        row=0,
        column=1)
    Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=8).grid(row=0,
                                                                                                      column=2)
    Label(myFrame, text="Username", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=0,
                                                                                                             column=3)
    Label(myFrame, text="Password", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=11).grid(row=0,
                                                                                                             column=4)
    Label(myFrame, text="Contact", bg="white", font=("MS Reference Sans Serif", 12, "bold"), width=10).grid(row=0,
                                                                                                            column=5)

    c.execute("SELECT *,oid FROM student_details")

    records = c.fetchall()

    roww = 1
    num = 1

    for record in records:
        Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=0)
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=21).grid(row=roww,
                                                                                                        column=1)
        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=11).grid(row=roww,
                                                                                                        column=2)
        Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww,
                                                                                                        column=3)
        Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=15).grid(row=roww,
                                                                                                        column=4)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=16).grid(row=roww,
                                                                                                        column=5)

        roww += 1
        num += 1

    conn.commit()
    conn.close()

    mainloop()


def issue_window():
    """Opens 'Issue Book' window"""
    issue_window = Toplevel()
    issue_window.geometry("1191x670+60+30")
    issue_window.resizable(0, 0)
    issue_window.title("Issue Books")
    issue_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/issue_window.png")
    resized_image = img.resize((1191, 670))
    issue_bg = ImageTk.PhotoImage(resized_image)
    issue_bg_image = Label(issue_window, image=issue_bg)
    issue_bg_image.place(x=0, y=0)

    conn = sqlite3.connect('issued_books_database.db')

    c = conn.cursor()

    # c.execute('''CREATE TABLE issued_book_details(
    # Issue_Number integer,
    # Book_Name text,
    # Student_ID integer,
    # Issue_Date text,
    # Return_Date text,
    # Quantity integer
    # )''')

    def search():
        """Takes book ID as input and searches book of respective ID"""
        global book_name_label

        conn = sqlite3.connect("books_database.db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM book_details")

        records = c.fetchall()

        for record in records:
            if int(book_id.get()) == int(record[6]):
                book_name_label = Label(issue_window, text=record[0], bg="#a7b3bb",
                                        font=("MS Reference Sans Serif", 14))
                book_name_label.place(x=220, y=145)

                author_name_label = Label(issue_window, text=record[2], bg="#a7b3bb",
                                          font=("MS Reference Sans Serif", 14))
                author_name_label.place(x=220, y=180)

                quantity_label = Label(issue_window, text=record[5], bg="#a7b3bb", font=("MS Reference Sans Serif", 14))
                quantity_label.place(x=220, y=215)

        conn.commit()
        conn.close()

    def issue_book():
        """Adds data of issued book into the database"""
        if book_id.get() != '' and quantity.get() != '' and issue_to.get() != '':

            conn = sqlite3.connect("issued_books_database.db")

            # Create cursor
            c = conn.cursor()

            c.execute("SELECT *, oid FROM issued_book_details")

            records = c.fetchall()

            last_issue_number = records[-1][0]

            conn.commit()
            conn.close()

            conn = sqlite3.connect("issued_books_database.db")

            # Create cursor
            c = conn.cursor()

            current_date = date.today()

            # Insert into table
            c.execute(
                "INSERT INTO issued_book_details VALUES (:Issue_Number, :Book_Name, :Student_ID, :Issue_Date, :Return_Date, :Quantity)",
                {
                    'Issue_Number': int(last_issue_number) + 1,
                    'Book_Name': book_name_label['text'],
                    'Student_ID': issue_to.get(),
                    'Issue_Date': current_date,
                    'Return_Date': cal.get_date(),
                    'Quantity': quantity.get()
                })

            # query of the database
            c.execute("SELECT *, oid FROM issued_book_details")

            # print(records)
            records = c.fetchall()

            roww = 1
            num = 1
            for record in records:
                Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=9).grid(row=roww,
                                                                                                               column=0)
                Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=23).grid(
                    row=roww, column=1)
                Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=10).grid(
                    row=roww, column=2)
                Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
                    row=roww, column=3)
                Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
                    row=roww, column=4)
                Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(
                    row=roww, column=5)

                roww += 1
                num += 1

            conn.commit()
            conn.close()

    # Creating and placing labels
    label1 = Label(issue_window, text="Issue Book", bg="#a7b3bb", font=("Times New Roman", 20, "bold"))
    label1.place(x=195, y=45)

    label2 = Label(issue_window, text="Issued Books", bg="#a7b3bb", font=("Times New Roman", 20, "bold"))
    label2.place(x=790, y=45)

    label3 = Label(issue_window, text="Book ID :", bg="#a7b3bb", font=("MS Reference Sans Serif", 17, "bold"))
    label3.place(x=40, y=90)

    label4 = Label(issue_window, text="Book Name :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label4.place(x=90, y=145)

    label5 = Label(issue_window, text="Author Name :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label5.place(x=72, y=180)

    label6 = Label(issue_window, text="Quantity :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label6.place(x=115, y=215)

    label7 = Label(issue_window, text="Quantity :", bg="#a7b3bb", font=("MS Reference Sans Serif", 17, "bold"))
    label7.place(x=40, y=262)

    label8 = Label(issue_window, text="Issue To :", bg="#a7b3bb", font=("MS Reference Sans Serif", 17, "bold"))
    label8.place(x=40, y=318)

    label8 = Label(issue_window, text="Select date for return", bg="#a7b3bb", fg="#032D23",
                   font=("MS Reference Sans Serif", 14, "bold"))
    label8.place(x=160, y=365)

    # Creating and placing buttons
    book_search_button = Button(issue_window, text="Search", border=0, bg="#364954", fg="white",
                                activebackground="#364954",
                                activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2",
                                command=search)
    book_search_button.place(x=390, y=87)

    issue_button = Button(issue_window, text="Issue Book", border=0, bg="#364954", fg="white",
                          activebackground="#364954",
                          activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2", command=issue_book)
    issue_button.place(x=211, y=594)

    # Creating and placing entries
    book_id = Entry(issue_window, bd=0, font=("MS Reference Sans Serif", 15), width=12, bg="#a7b3bb", fg="black")
    book_id.place(x=183, y=93)
    book_id.focus()

    quantity = Entry(issue_window, bd=0, font=("MS Reference Sans Serif", 15), width=6, bg="#a7b3bb", fg="black")
    quantity.place(x=189, y=260)

    issue_to = Entry(issue_window, bd=0, font=("MS Reference Sans Serif", 15), width=12, bg="#a7b3bb", fg="black")
    issue_to.place(x=189, y=317)

    # Calendar
    cal = Calendar(issue_window, locale='en_US', date_pattern='y-mm-dd')
    cal.place(x=150, y=399)

    # Create Frame with scrollbar
    cover = LabelFrame(issue_window, height=800, width=1000, bd=0)
    cover.place(x=524, y=86)

    myCanvas = Canvas(cover, height=530, width=610, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    Label(myFrame, text="Issue No.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=8).grid(row=0,
                                                                                                             column=0)
    Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=20).grid(row=0,
                                                                                                              column=1)
    Label(myFrame, text="Student ID", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=9).grid(row=0,
                                                                                                              column=2)
    Label(myFrame, text="Issue Date", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=11).grid(row=0,
                                                                                                               column=3)
    Label(myFrame, text="Return Date", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=11).grid(row=0,
                                                                                                                column=4)
    Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=4).grid(row=0, column=5)

    # query of the database
    c.execute("SELECT *, oid FROM issued_book_details")

    # print(records)
    records = c.fetchall()

    roww = 1
    num = 1
    for record in records:
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=9).grid(row=roww,
                                                                                                       column=0)
        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=23).grid(
            row=roww, column=1)
        Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=10).grid(
            row=roww, column=2)
        Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
            row=roww, column=3)
        Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
            row=roww, column=4)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(
            row=roww, column=5)

        roww += 1
        num += 1

    conn.commit()
    conn.close()

    mainloop()


# Function that opens return book window
def return_window():
    """Opens 'Return Books' window"""
    return_window = Toplevel()
    return_window.geometry("1191x670+60+30")
    return_window.resizable(0, 0)
    return_window.title("Return Books")
    return_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/return_window.png")
    resized_image = img.resize((1191, 670))
    return_bg = ImageTk.PhotoImage(resized_image)
    return_bg_image = Label(return_window, image=return_bg)
    return_bg_image.place(x=0, y=0)

    def search():
        """Takes Issue Number as input and searches issue of respective issue number"""
        conn = sqlite3.connect("issued_books_database.db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM issued_book_details")

        records = c.fetchall()

        for record in records:
            if int(issue_num.get()) == int(record[0]):
                book_name_label = Label(return_window, text=record[1], bg="#a7b3bb",
                                        font=("MS Reference Sans Serif", 14))
                book_name_label.place(x=220, y=145)

                student_ID_label = Label(return_window, text=record[2], bg="#a7b3bb",
                                         font=("MS Reference Sans Serif", 14))
                student_ID_label.place(x=220, y=185)

                quantity_label = Label(return_window, text=record[5], bg="#a7b3bb",
                                       font=("MS Reference Sans Serif", 14))
                quantity_label.place(x=220, y=220)

                issue_date_label = Label(return_window, text=record[3], bg="#a7b3bb",
                                         font=("MS Reference Sans Serif", 14))
                issue_date_label.place(x=220, y=255)

                return_date_label = Label(return_window, text=record[4], bg="#a7b3bb",
                                          font=("MS Reference Sans Serif", 14))
                return_date_label.place(x=220, y=290)

                current_date = str(date.today())
                date1 = current_date.split("-")

                return_date = record[4]
                date2 = return_date.split("-")

                c_date = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
                r_date = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))

                if c_date > r_date:
                    Label(return_window, text="STATUS", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 16, "bold")).place(x=215, y=380)

                    Label(return_window,
                          text="The date for return of this book has already passed.\n So, the fine will be Rs. 100",
                          bg="#a7b3bb", font=("MS Reference Sans Serif", 12, "bold")).place(x=30, y=420)

                else:
                    Label(return_window, text="STATUS", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 16, "bold")).place(x=215, y=380)

                    Label(return_window, text="The date for return of this book has not passed.", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 12, "bold")).place(x=45, y=420)

        conn.commit()
        conn.close()

    def return_book():
        """Remove data of issued books from the database"""
        if issue_num.get() != '':
            # create database
            conn = sqlite3.connect("issued_books_database.db")

            # create cursor
            c = conn.cursor()

            # delete a record
            c.execute("DELETE from issued_book_details WHERE Issue_Number = " + issue_num.get())

            # query of the database
            c.execute("SELECT *, oid FROM issued_book_details")

            records = c.fetchall()

            # Loop through the results
            roww = 1
            num = 1
            for record in records:
                Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=9).grid(row=roww,
                                                                                                               column=0)
                Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=23).grid(
                    row=roww, column=1)
                Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=10).grid(
                    row=roww, column=2)
                Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
                    row=roww, column=3)
                Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
                    row=roww, column=4)
                Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(
                    row=roww, column=5)

                roww += 1
                num += 1

            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=9).grid(row=roww, column=0)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=23).grid(row=roww, column=1)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=10).grid(row=roww, column=2)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(row=roww, column=3)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(row=roww, column=4)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=5)

            issue_num.delete(0, END)

            conn.commit()
            conn.close()

    # Creating and placing labels

    label1 = Label(return_window, text="Return Book", bg="#a7b3bb", font=("Times New Roman", 20, "bold"))
    label1.place(x=195, y=45)

    label2 = Label(return_window, text="Issued Books", bg="#a7b3bb", font=("Times New Roman", 20, "bold"))
    label2.place(x=790, y=45)

    label3 = Label(return_window, text="Issue No. :", bg="#a7b3bb", font=("MS Reference Sans Serif", 17, "bold"))
    label3.place(x=30, y=90)

    label4 = Label(return_window, text="Book Name :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label4.place(x=90, y=145)

    label5 = Label(return_window, text="Student ID :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label5.place(x=90, y=185)

    label6 = Label(return_window, text="Quantity :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label6.place(x=115, y=220)

    label7 = Label(return_window, text="Issue Date :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label7.place(x=95, y=255)

    label8 = Label(return_window, text="Date for Return :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label8.place(x=50, y=290)

    # Creating and placing entries
    issue_num = Entry(return_window, bd=0, font=("MS Reference Sans Serif", 15), width=12, bg="#a7b3bb", fg="black")
    issue_num.place(x=183, y=93)
    issue_num.focus()

    # Buttons
    book_search_button = Button(return_window, text="Search", border=0, bg="#364954", fg="white",
                                activebackground="#364954",
                                activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2",
                                command=search)
    book_search_button.place(x=390, y=87)

    return_button = Button(return_window, text="Return Book", border=0, bg="#364954", fg="white",
                           activebackground="#364954",
                           activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2",
                           command=return_book)
    return_button.place(x=201, y=507)

    # Create Frame with scrollbar
    cover = LabelFrame(return_window, height=800, width=1000, bd=0)
    cover.place(x=524, y=86)

    myCanvas = Canvas(cover, height=530, width=610, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    conn = sqlite3.connect('issued_books_database.db')

    c = conn.cursor()

    Label(myFrame, text="Issue No.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=8).grid(row=0,
                                                                                                             column=0)
    Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=20).grid(row=0,
                                                                                                              column=1)
    Label(myFrame, text="Student ID", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=9).grid(row=0,
                                                                                                              column=2)
    Label(myFrame, text="Issue Date", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=11).grid(row=0,
                                                                                                               column=3)
    Label(myFrame, text="Return Date", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=11).grid(row=0,
                                                                                                                column=4)
    Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=4).grid(row=0, column=5)

    # query of the database
    c.execute("SELECT *, oid FROM issued_book_details")

    # print(records)
    records = c.fetchall()

    roww = 1
    num = 1
    for record in records:
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=9).grid(row=roww,
                                                                                                       column=0)
        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=23).grid(
            row=roww, column=1)
        Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=10).grid(
            row=roww, column=2)
        Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
            row=roww, column=3)
        Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(
            row=roww, column=4)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(
            row=roww, column=5)

        roww += 1
        num += 1

    conn.commit()
    conn.close()

    mainloop()


def available_books():
    """Opens 'Available Books' window of student window"""
    available_books_window = Toplevel()
    available_books_window.geometry("1191x670+60+30")
    available_books_window.resizable(0, 0)
    available_books_window.title("Available Books")
    available_books_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/books_student_window.png")
    resized_image = img.resize((1191, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(available_books_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    def search():
        """Takes book ID as input and searches book of respective ID"""
        for widgets in myFrame.winfo_children():
            widgets.destroy()

        conn = sqlite3.connect("books_database.db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM book_details")

        records = c.fetchall()

        for record in records:
            if str(category.get()).lower().strip() == str(record[1]).lower():
                Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 10, "bold")).grid(row=0,
                                                                                                          column=0)
                Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 10, "bold"),
                      width=25).grid(row=0,
                                     column=1)
                Label(myFrame, text="Publication", bg="white", font=("MS Reference Sans Serif", 10, "bold"),
                      width=16).grid(row=0,
                                     column=2)
                Label(myFrame, text="Category", bg="white", font=("MS Reference Sans Serif", 10, "bold"),
                      width=10).grid(row=0,
                                     column=3)
                Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=5).grid(
                    row=0, column=4)
                Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=5).grid(row=0,
                                                                                                                  column=5)

                roww = 1
                num = 1

                for record in records:
                    if str(category.get()).lower().strip() == str(record[1]).lower():
                        Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 9), width=4).grid(row=roww,
                                                                                                                column=0)
                        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 9), width=28).grid(
                            row=roww, column=1)
                        Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 9), width=18).grid(
                            row=roww, column=2)
                        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 9), width=11).grid(
                            row=roww, column=3)
                        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 9), width=5).grid(
                            row=roww, column=4)
                        Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 9), width=6).grid(
                            row=roww, column=5)

                        roww += 1
                        num += 1

        conn.commit()
        conn.close()

    # Button
    search_button = Button(available_books_window, text="Search", border=0, bg="#364954", fg="white", activebackground="#364954",
                        activeforeground="#84B1CB", font=("Poppins", 16, "bold"), cursor="hand2", command=search)
    search_button.place(x=245, y=217)

    # Entry
    category = Entry(available_books_window, bd=0, font=("MS Reference Sans Serif", 15), width=14, bg="#a7b3bb", fg="black")
    category.place(x=258, y=140)
    category.focus()

    # Labels
    Label(available_books_window, text="Search books by Category", bg="#a7b3bb", fg="#032D23", font=("MS Reference Sans Serif", 15, "bold")).place(x=130, y=100)
    Label(available_books_window, text="Category :", bg="#a7b3bb", font=("MS Reference Sans Serif", 14, "bold")).place(x=120, y=140)

    # Create Frame with scrollbar
    cover = LabelFrame(available_books_window, height=800, width=1000, bd=0)
    cover.place(x=459, y=85)

    myCanvas = Canvas(cover, height=490, width=601, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 10, "bold")).grid(row=0, column=0)
    Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=25).grid(row=0,
                                                                                                              column=1)
    Label(myFrame, text="Publication", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=16).grid(row=0,
                                                                                                                column=2)
    Label(myFrame, text="Category", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=10).grid(row=0,
                                                                                                             column=3)
    Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=5).grid(row=0, column=4)
    Label(myFrame, text="ID", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=5).grid(row=0, column=5)

    conn = sqlite3.connect("books_database.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM book_details")

    records = c.fetchall()

    roww = 1
    num = 1

    for record in records:
        Label(myFrame, text=num, bg="white", font=("MS Reference Sans Serif", 9), width=4).grid(row=roww, column=0)
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 9), width=28).grid(row=roww, column=1)
        Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 9), width=18).grid(row=roww, column=2)
        Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 9), width=11).grid(row=roww, column=3)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 9), width=5).grid(row=roww, column=4)
        Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 9), width=6).grid(row=roww, column=5)

        roww += 1
        num += 1

    conn.commit()
    conn.close()

    mainloop()


def my_books():
    """Opens 'My Books' window of student window"""
    my_books_window = Toplevel()
    my_books_window.geometry("1191x670+60+30")
    my_books_window.resizable(0, 0)
    my_books_window.title("Available Books")
    my_books_window.iconbitmap("images/icon.ico")

    # Background image of books window
    img = Image.open("images/return_window.png")
    resized_image = img.resize((1191, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(my_books_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    conn = sqlite3.connect("students_database.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM student_details")

    student_records = c.fetchall()

    std_ID = []

    for student_record in student_records:
        if student_record[2] == std_username:
            std_ID.append(student_record[1])

    conn.commit()
    conn.close()

    def search():
        conn = sqlite3.connect("issued_books_database.db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM issued_book_details")

        records = c.fetchall()

        for record in records:
            if int(issue_num.get()) == int(record[0]):
                book_name_label = Label(my_books_window, text=record[1], bg="#a7b3bb",
                                        font=("MS Reference Sans Serif", 14))
                book_name_label.place(x=220, y=145)

                quantity_label = Label(my_books_window, text=record[5], bg="#a7b3bb",
                                       font=("MS Reference Sans Serif", 14))
                quantity_label.place(x=220, y=185)

                issue_date_label = Label(my_books_window, text=record[3], bg="#a7b3bb",
                                         font=("MS Reference Sans Serif", 14))
                issue_date_label.place(x=220, y=220)

                return_date_label = Label(my_books_window, text=record[4], bg="#a7b3bb",
                                          font=("MS Reference Sans Serif", 14))
                return_date_label.place(x=220, y=255)

                current_date = str(date.today())
                date1 = current_date.split("-")

                return_date = record[4]
                date2 = return_date.split("-")

                c_date = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
                r_date = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))

                delta = r_date - c_date

                if c_date > r_date:
                    Label(my_books_window, text="STATUS", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 16, "bold")).place(x=215, y=380)

                    Label(my_books_window,
                          text="The date for return of this book has already passed.\n So, the fine will be Rs. 100",
                          bg="#a7b3bb", font=("MS Reference Sans Serif", 12, "bold")).place(x=30, y=420)

                elif c_date == r_date:
                    Label(my_books_window, text="STATUS", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 16, "bold")).place(x=215, y=380)

                    Label(my_books_window,
                          text="The date for return of this book is today.",
                          bg="#a7b3bb", font=("MS Reference Sans Serif", 12, "bold")).place(x=70, y=420)

                else:
                    Label(my_books_window, text="STATUS", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 16, "bold")).place(x=215, y=380)

                    Label(my_books_window, text=f"You have {delta.days} day(s) remaining to return this book.", bg="#a7b3bb",
                          font=("MS Reference Sans Serif", 12, "bold")).place(x=45, y=420)

        conn.commit()
        conn.close()

    def exit():
        my_books_window.destroy()

    # Creating and placing labels

    label1 = Label(my_books_window, text="Book Details", bg="#a7b3bb", font=("Times New Roman", 20, "bold"))
    label1.place(x=195, y=45)

    label2 = Label(my_books_window, text="My Issued Books", bg="#a7b3bb", font=("Times New Roman", 20, "bold"))
    label2.place(x=790, y=45)

    label3 = Label(my_books_window, text="Issue No. :", bg="#a7b3bb", font=("MS Reference Sans Serif", 17, "bold"))
    label3.place(x=30, y=90)

    label4 = Label(my_books_window, text="Book Name :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label4.place(x=90, y=145)

    label6 = Label(my_books_window, text="Quantity :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label6.place(x=115, y=185)

    label7 = Label(my_books_window, text="Issue Date :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label7.place(x=95, y=220)

    label8 = Label(my_books_window, text="Date for Return :", bg="#a7b3bb", font=("MS Reference Sans Serif", 13, "bold"))
    label8.place(x=50, y=255)

    # Creating and placing entries
    issue_num = Entry(my_books_window, bd=0, font=("MS Reference Sans Serif", 15), width=12, bg="#a7b3bb", fg="black")
    issue_num.place(x=183, y=93)
    issue_num.focus()

    # Buttons
    search_issue_button = Button(my_books_window, text="Search", border=0, bg="#364954", fg="white", activebackground="#364954",
                                 activeforeground="#84B1CB", font=("Poppins", 15, "bold"), cursor="hand2", command=search)
    search_issue_button.place(x=390, y=87)

    exit_button = Button(my_books_window, text="Exit", border=0, bg="#364954", fg="white", activebackground="#364954",
                         activeforeground="#84B1CB", font=("Poppins", 17, "bold"), cursor="hand2", command=exit)
    exit_button.place(x=240, y=503)

    # Create Frame with scrollbar
    cover = LabelFrame(my_books_window, height=800, width=1000, bd=0)
    cover.place(x=524, y=86)

    myCanvas = Canvas(cover, height=530, width=610, bg="white")
    myCanvas.pack(side=LEFT, fill='y', expand='yes')

    myFrame = Frame(myCanvas)
    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

    scrollbar = ttk.Scrollbar(cover, orient='vertical', command=myCanvas.yview)
    scrollbar.pack(side=RIGHT, fill='y')
    myCanvas.config(yscrollcommand=scrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

    conn = sqlite3.connect('issued_books_database.db')

    c = conn.cursor()

    Label(myFrame, text="Issue No.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=8).grid(row=0, column=0)
    Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=20).grid(row=0, column=1)
    Label(myFrame, text="Student ID", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=9).grid(row=0, column=2)
    Label(myFrame, text="Issue Date", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=11).grid(row=0, column=3)
    Label(myFrame, text="Return Date", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=11).grid(row=0, column=4)
    Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 10, "bold"), width=4).grid(row=0, column=5)

    # query of the database
    c.execute("SELECT *, oid FROM issued_book_details")

    # print(records)
    records = c.fetchall()

    roww = 1
    num = 1
    for record in records:
        if record[2] in std_ID:
            Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 10), width=9).grid(row=roww, column=0)
            Label(myFrame, text=record[1], bg="white", font=("MS Reference Sans Serif", 10), width=23).grid(row=roww, column=1)
            Label(myFrame, text=record[2], bg="white", font=("MS Reference Sans Serif", 10), width=10).grid(row=roww, column=2)
            Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(row=roww, column=3)
            Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 10), width=13).grid(row=roww, column=4)
            Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 10), width=5).grid(row=roww, column=5)

            roww += 1
            num += 1

    conn.commit()
    conn.close()

    mainloop()


login_window()
