from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk

admin_credentials = {'username': 'admin', 'password': 'admin'}


def login_window():
    global username
    global password
    global root

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

    # Creating and placing labels
    welcome_label = Label(root, text="Welcome!", bg="#a7b3bb", fg="#232E34", font=("Poppins", 24, "bold"))
    welcome_label.place(x=860, y=140)

    login_label = Label(root, text="Sign in to continue", bg="#a7b3bb", fg="#232E34", font=("Poppins", 16))
    login_label.place(x=850, y=180)

    # Creating and placing button
    login_button = Button(root, text="Log In ", border=0, bg="#364954", fg="white", activebackground="#364954",
                          activeforeground="#84B1CB", font=("Poppins", 18, "bold"), cursor="hand2",
                          command=open_dashboard)
    login_button.place(x=885, y=410)

    # Creating and placing entries
    username = Entry(root, width=25, border=0, font=("Poppins", 15))
    username.place(x=795, y=240)
    username.focus()

    password = Entry(root, width=25, border=0, font=("Poppins", 16), show="*")
    password.place(x=795, y=330)

    mainloop()


def open_dashboard():
    global window

    if username.get() == '' or password.get() == '':
        messagebox.showinfo("Incomplete Information", "Please enter both username and password to continue!")

    elif username.get() != admin_credentials['username'] or password.get() != admin_credentials['password']:
        messagebox.showinfo("Incorrect Information", "Please enter correct credentials!")

    elif username.get() == admin_credentials['username'] and password.get() == admin_credentials['password']:
        window = Toplevel(root)
        window.geometry("1191x670+60+30")
        window.resizable(0, 0)
        window.title("Dashboard")

        def logout():
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
                                    cursor="hand2")
        issue_button_image.place(x=375, y=420)
        Label(window, text="Issue Book", bg="white", font=("Poppins", 16)).place(x=375, y=505)

        books_button = ImageTk.PhotoImage(resized_image5)
        books_button_image = Button(window, image=books_button, border=0, bg="white", activebackground="white",
                                    cursor="hand2", command=books_window)
        books_button_image.place(x=215, y=170)
        Label(window, text="Books", bg="white", font=("Poppins", 16)).place(x=235, y=265)

        return_button = ImageTk.PhotoImage(resized_image6)
        return_button_image = Button(window, image=return_button, border=0, bg="white", activebackground="white",
                                     cursor="hand2")
        return_button_image.place(x=710, y=420)
        Label(window, text="Return Book", bg="white", font=("Poppins", 16)).place(x=694, y=502)

        logout_button = Button(window, text="Log Out", border=0, bg="#364954", fg="white", activebackground="#364954",
                               activeforeground="#84B1CB", font=("Poppins", 17, "bold"), cursor="hand2", command=logout)
        logout_button.place(x=1020, y=580)

        # Label
        label1 = Label(window, text="Dashboard", bg="#a7b3bb", font=("Times New Roman", 50, "bold"), fg="#151F25")
        label1.place(x=450, y=40)

        mainloop()


def books_window():
    books_window = Toplevel(window)
    books_window.geometry("1191x670+60+30")
    books_window.resizable(0, 0)
    books_window.title("Books")

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
    # Language integer,
    # Publication text,
    # Quantity integer
    # )''')

    def books_window_logout():
        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=books_window)
        if ans:
            window.destroy()
            books_window.destroy()
            username.delete(0, END)
            password.delete(0, END)
            username.focus()

    def add_book_window():
        add = Toplevel()
        add.title("Add Book")
        add.geometry("1191x670+60+30")
        add.resizable(0, 0)

        # Read the Image
        image = Image.open("images/add_and_update.png")

        # Resize the image using resize() method
        resize_image = image.resize((1191, 670))

        # Displaying background image
        bg = ImageTk.PhotoImage(resize_image)
        bg_image = Label(add, image=bg)
        bg_image.place(x=0, y=0)

        def add_book():
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
                for record in records:
                    Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 12), width=27).grid(row=roww, column=1)
                    Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 12), width=17).grid(row=roww, column=2)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 12), width=12).grid(row=roww, column=3)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=4)

                    roww += 1

                conn.commit()
                conn.close()
                add.destroy()

        def clear_add_window():
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
        if book_id.get() != '':
            update_window = Toplevel()
            update_window.title("Update Book")
            update_window.geometry("1191x670+60+30")
            update_window.resizable(0, 0)

            # Read the Image
            image = Image.open("images/add_and_update.png")

            # Resize the image using resize() method
            resize_image = image.resize((1191, 670))

            # Displaying background image
            bg = ImageTk.PhotoImage(resize_image)
            bg_image = Label(update_window, image=bg)
            bg_image.place(x=0, y=0)

            def update_book():
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
                for record in records:
                    Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(
                        row=roww, column=0)
                    Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 12), width=27).grid(
                        row=roww, column=1)
                    Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 12), width=17).grid(
                        row=roww, column=2)
                    Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 12), width=12).grid(
                        row=roww, column=3)
                    Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(
                        row=roww, column=4)
                    roww += 1

                conn.commit()
                conn.close()

            def clear_update_window():
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


    def remove_book():
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
            for record in records:
                Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=0)
                Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 12), width=27).grid(row=roww, column=1)
                Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 12), width=17).grid(row=roww, column=2)
                Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 12), width=12).grid(row=roww, column=3)
                Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=4)

                roww += 1

            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=0)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 12), width=27).grid(row=roww, column=1)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 12), width=17).grid(row=roww, column=2)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 12), width=12).grid(row=roww, column=3)
            Label(myFrame, text='', bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=4)

            book_id.delete(0, END)

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("Invalid Book ID", "Please enter valid book ID to continue.", parent=books_window)

    # Buttons
    search_button = Button(books_window, text="Search", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2")
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

    Label(myFrame, text="S.N", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=4).grid(row=0, column=0)
    Label(myFrame, text="Book Name", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=22).grid(row=0, column=1)
    Label(myFrame, text="Publication", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=14).grid(row=0, column=2)
    Label(myFrame, text="Language", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=10).grid(row=0, column=3)
    Label(myFrame, text="Qty.", bg="white", font=("MS Reference Sans Serif", 13, "bold"), width=4).grid(row=0, column=4)

    c.execute("SELECT *,oid FROM book_details")

    records = c.fetchall()

    roww = 1

    for record in records:
        Label(myFrame, text=record[6], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=0)
        Label(myFrame, text=record[0], bg="white", font=("MS Reference Sans Serif", 12), width=27).grid(row=roww, column=1)
        Label(myFrame, text=record[4], bg="white", font=("MS Reference Sans Serif", 12), width=17).grid(row=roww, column=2)
        Label(myFrame, text=record[3], bg="white", font=("MS Reference Sans Serif", 12), width=12).grid(row=roww, column=3)
        Label(myFrame, text=record[5], bg="white", font=("MS Reference Sans Serif", 12), width=5).grid(row=roww, column=4)

        roww += 1

    conn.commit()
    conn.close()

    mainloop()


def librarians_window():
    librarians_window = Toplevel(window)
    librarians_window.geometry("1191x670+60+30")
    librarians_window.resizable(0, 0)
    librarians_window.title("Librarians")

    # Background image of books window
    img = Image.open("images/management_window.png")
    resized_image = img.resize((1240, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(librarians_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    def librarians_window_logout():
        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=librarians_window)
        if ans:
            window.destroy()
            librarians_window.destroy()
            username.delete(0, END)
            password.delete(0, END)
            username.focus()

    # Buttons
    search_button = Button(librarians_window, text="Search", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2")
    search_button.place(x=295, y=169)

    add_button = Button(librarians_window, text="Add Librarian", border=0, bg="#364954", fg="white",
                        activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                        cursor="hand2")
    add_button.place(x=155, y=297)

    update_button = Button(librarians_window, text="Update Librarian", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2")
    update_button.place(x=137, y=370)

    remove_button = Button(librarians_window, text="Remove Librarian", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2")
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

    mainloop()


def students_window():
    students_window = Toplevel(window)
    students_window.geometry("1191x670+60+30")
    students_window.resizable(0, 0)
    students_window.title("Students")

    # Background image of books window
    img = Image.open("images/management_window.png")
    resized_image = img.resize((1240, 670))
    books_bg = ImageTk.PhotoImage(resized_image)
    books_bg_image = Label(students_window, image=books_bg)
    books_bg_image.place(x=0, y=0)

    def students_window_logout():
        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=students_window)
        if ans:
            window.destroy()
            students_window.destroy()
            username.delete(0, END)
            password.delete(0, END)
            username.focus()

    # Buttons
    search_button = Button(students_window, text="Search", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                           cursor="hand2")
    search_button.place(x=295, y=169)

    add_button = Button(students_window, text="Add Student", border=0, bg="#364954", fg="white",
                        activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 15, "bold"),
                        cursor="hand2")
    add_button.place(x=155, y=297)

    update_button = Button(students_window, text="Update Student", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2")
    update_button.place(x=142, y=370)

    remove_button = Button(students_window, text="Remove Student", border=0, bg="#364954", fg="white",
                           activebackground="#364954", activeforeground="#84B1CB", font=("Poppins", 14, "bold"),
                           cursor="hand2")
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

    mainloop()


login_window()
