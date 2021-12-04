from tkinter import *
# from psycopg2 import *
# import psycopg2
from tkinter import messagebox


def raise_frame(frame):
    frame.tkraise()


box_title = "Success!"


def popup():
    messagebox.showinfo(
        box_title, "Entry was successfully added to the database!")
    raise_frame(f1)


def popup_deletion():
    messagebox.showinfo(box_title, "Entry has been deleted!")
    raise_frame(f1)


def popup_edit():
    messagebox.showinfo(box_title, "Entry has been edited!")
    raise_frame(f1)


root = Tk()

# initialize frames used in the GUI
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)

v1 = StringVar()

for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9):
    frame.grid(row=0, column=0, sticky='news')

# Login page GUI
Label(f1, text="Email Address").pack()
admin_email = StringVar(f1)  # stores current input
Entry(f1, textvariable=admin_email).pack()
Button(f1, text="Login", command=lambda: raise_frame(f2)).pack()

# create/search toggle GUI
Label(f2, text="Choose between creating or searching for items:").pack()
Button(f2, text="Add a User", command=lambda: raise_frame(f3)).pack()
Button(f2, text="Add a Book", command=lambda: raise_frame(f4)).pack()
Button(f2, text="Search", command=lambda: raise_frame(f5)).pack()

# User creation GUI
Label(f3, text="Create User").pack()

Label(f3, text="User ID:").pack()
user_id = StringVar(f3)
Entry(f3, textvariable=user_id).pack()

Label(f3, text="Name:").pack()
name = StringVar(f3)
Entry(f3, textvariable=name).pack()

Label(f3, text="Address:").pack()
address = StringVar(f3)
Entry(f3, textvariable=address).pack()

Label(f3, text="Email:").pack()
email = StringVar(f3)
Entry(f3, textvariable=email).pack()

Label(f3, text="Program (Students only):").pack()
program = StringVar(f3)
Entry(f3, textvariable=program).pack()

Label(f3, text="Department (Admin only):").pack()
department = StringVar(f3)
Entry(f3, textvariable=department).pack()

Label(f3, text="Phone Number (Admin only):").pack()
phone_number = StringVar(f3)
Entry(f3, textvariable=phone_number).pack()

Button(f3, text="Create User", command=lambda: popup()).pack()

# Book creation GUI
Label(f4, text="Create Book").pack()

Label(f4, text="Book ID:").pack()
book_id = StringVar(f4)
Entry(f4, textvariable=book_id).pack()

Label(f4, text="Title:").pack()
title = StringVar(f4)
Entry(f4, textvariable=title).pack()

Label(f4, text="Pages:").pack()
pages = StringVar(f4)
Entry(f4, textvariable=pages).pack()

Label(f4, text="Physical ID:").pack()
physical_id = StringVar(f4)
Entry(f4, textvariable=physical_id).pack()

Label(f4, text="Damaged:").pack()
damaged = StringVar(f4)
Entry(f4, textvariable=damaged).pack()

Label(f4, text="Prequel ID:").pack()
prequel_id = StringVar(f4)
Entry(f4, textvariable=prequel_id).pack()

Label(f4, text="ISBN:").pack()
isbn = StringVar(f4)
Entry(f4, textvariable=isbn).pack()

Label(f4, text="Publisher:").pack()
publisher = StringVar(f4)
Entry(f4, textvariable=publisher).pack()

Label(f4, text="Date of Publishing:").pack()
date_of_publishing = StringVar(f4)
Entry(f4, textvariable=date_of_publishing).pack()

Label(f4, text="Author:").pack()
author = StringVar(f4)
Entry(f4, textvariable=author).pack()

Label(f4, text="Genre:").pack()
genre = StringVar(f4)
Entry(f4, textvariable=genre).pack()

Label(f4, text="Language:").pack()
language = StringVar(f4)
Entry(f4, textvariable=language).pack()

Button(f4, text="Create Book", command=lambda: popup()).pack()

# search GUI
Label(f5, text="Search")
Radiobutton(f5, text="User", value=1, indicatoron=0,
            variable=v1).pack()
Radiobutton(f5, text="Book", value=2, indicatoron=0,
            variable=v1).pack()
search_string = StringVar(f5)
Entry(f5, textvariable=search_string).pack()
Label(f5, text="Search Criteria:").pack()
Label(f5, text="Languages:").pack()
checkVar1 = IntVar(value=1)
checkVar2 = IntVar(value=1)
checkVar3 = IntVar(value=1)
Checkbutton(f5, text="Swedish", variable=checkVar1,
            onvalue=1, offvalue=0).pack()
Checkbutton(f5, text="English", variable=checkVar2,
            onvalue=1, offvalue=0).pack()
Checkbutton(f5, text="German", variable=checkVar3,
            onvalue=1, offvalue=0).pack()
Button(f5, text="Search", command=lambda: raise_frame(f6)).pack()

# search results GUI
Label(f6, text="Search Results:").pack()

# tillfällig array för att kunna skriva koden
results = ["Harry Potter", "Alfons", "Brott och straff"]
for result in results:
    Button(f6, text=result, command=lambda entry=result: result_details(entry)).pack()

# Book detailed view GUI + update/delete


def result_details(entry):
    raise_frame(f7)
    Label(f7, text=entry).pack()
    Button(f7, text="Edit", command=lambda: edit_view(entry)).pack()
    Button(f7, text="Delete from database",
           command=lambda: popup_deletion()).pack()

# Kommer behöva input i form av datastruktur som innehåller alla attribut till tupeln


def edit_view(entry):
    raise_frame(f8)
    if (v1.get() == "1"):  # if user search
        Label(f8, text="Edit User").pack()

        Label(f8, text="User ID:").pack()
        user_id = StringVar(f8)
        e1 = Entry(f8, textvariable=user_id)
        e1.insert(0, 123)
        e1.pack()

        Label(f8, text="Name:").pack()
        name = StringVar(f8)
        e2 = Entry(f8, textvariable=name)
        e2.insert(0, "Stefan Olsson")
        e2.pack()

        Label(f8, text="Address:").pack()
        address = StringVar(f8)
        e3 = Entry(f8, textvariable=address)
        e3.insert(0, "Birger Jarlsgatan 34")
        e3.pack()

        Label(f8, text="Email:").pack()
        email = StringVar(f8)
        e4 = Entry(f8, textvariable=email)
        e4.insert(0, "test@gmail.com")
        e4.pack()

        Label(f8, text="Program (Students only):").pack()
        program = StringVar(f8)
        e5 = Entry(f8, textvariable=program)
        e5.insert(0, "Datateknik")
        e5.pack()

        Label(f8, text="Department (Admin only):").pack()
        department = StringVar(f8)
        e6 = Entry(f8, textvariable=department)
        e6.insert(0, "")
        e6.pack()

        Label(f8, text="Phone Number (Admin only):").pack()
        phone_number = StringVar(f8)
        e7 = Entry(f8, textvariable=phone_number)
        e7.insert(0, "")
        e7.pack()

    if (v1.get() == "2"):  # if book search
        Label(f8, text="Edit Book").pack()

        Label(f8, text="Book ID:").pack()
        book_id = StringVar(f8)
        e1 = Entry(f8, textvariable=book_id)
        e1.insert(0, "12")
        e1.pack()

        Label(f8, text="Title:").pack()
        title = StringVar(f8)
        e2 = Entry(f4, textvariable=title)
        e2.insert(0, "Harry Potter")
        e2.pack()

        Label(f8, text="Pages:").pack()
        pages = StringVar(f8)
        e3 = Entry(f8, textvariable=pages)
        e3.insert(0, 123)
        e3.pack()

        Label(f8, text="Physical ID:").pack()
        physical_id = StringVar(f8)
        e4 = Entry(f8, textvariable=physical_id)
        e4.insert(0, 43)
        e4.pack()

        Label(f8, text="Damaged:").pack()
        damaged = StringVar(f8)
        e5 = Entry(f8, textvariable=damaged)
        e5.insert(0, "True")
        e5.pack()

        Label(f8, text="Prequel ID:").pack()
        prequel_id = StringVar(f8)
        e6 = Entry(f8, textvariable=prequel_id)
        e6.insert(0, 23)
        e6.pack()

        Label(f8, text="ISBN:").pack()
        isbn = StringVar(f8)
        e7 = Entry(f8, textvariable=isbn)
        e7.insert(0, 12345)
        e7.pack()

        Label(f8, text="Publisher:").pack()
        publisher = StringVar(f8)
        e8 = Entry(f8, textvariable=publisher)
        e8.insert(0, "E.J. Meadows")
        e8.pack()

        Label(f8, text="Date of Publishing:").pack()
        date_of_publishing = StringVar(f8)
        e9 = Entry(f8, textvariable=date_of_publishing)
        e9.insert(0, "2019-08-05")
        e9.pack()

        Label(f8, text="Author:").pack()
        author = StringVar(f8)
        e10 = Entry(f8, textvariable=author)
        e10.insert(0, "JK Rowling")
        e10.pack()

        Label(f8, text="Genre:").pack()
        genre = StringVar(f8)
        e11 = Entry(f8, textvariable=genre)
        e11.insert(0, "fantasy")
        e11.pack()

        Label(f8, text="Language:").pack()
        language = StringVar(f8)
        e12 = Entry(f8, textvariable=language)
        e12.insert(0, "svenska")
        e12.pack()

    Button(f8, text="Save changes", command=lambda: popup_edit()).pack()


# render initial GUI
raise_frame(f1)

# program loop
root.mainloop()

""" 
# Connect to PSQL Database
try:
    connection = psycopg2.connect(user="kagebo",
                                  password="D1EIvI0A",
                                  host = "127.0.0.0",
                                  database = "labb3")
    # The cursor is used to perform database operations 
    cursor = connection.cursor()
    item_tuple = (12, "Keyboard", item_purchase_time, 150)
 """
