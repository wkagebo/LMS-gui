from tkinter import *
# from psycopg2 import *
# import psycopg2
from tkinter import messagebox


def raise_frame(frame):
    frame.tkraise()


def popup():
    messagebox.showinfo(
        "Success!", "Entry was successfully added to the database!")


root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)

v1 = StringVar()

for frame in (f1, f2, f3, f4, f5, f6):
    frame.grid(row=0, column=0, sticky='news')

if v1.get() == "1":
    Label(f4, text="User search:").pack()
if v1.get() == "2":
    Label(f4, text="Book search:").pack()

# Login page GUI
Label(f1, text="Email Address").pack()
admin_email = StringVar(f1)  # stores current input
Entry(f1, textvariable=admin_email).pack()
Button(f1, text="Login", command=lambda: raise_frame(f2)).pack(side=BOTTOM)

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
Radiobutton(f5, text="User", value=1, indicatoron=0, variable=v1).pack()
Radiobutton(f5, text="Book", value=2, indicatoron=0, variable=v1).pack()
search_string = StringVar(f5)
Entry(f5, textvariable=search_string).pack()
Button(f5, text="Search", command=lambda: raise_frame(f6)).pack()

# search results GUI
Label(f6, text="Search Results:").pack()

# tillfälligt för att kunna skriva koden
results = ["harry potter", "alfons", "brott och straff"]
for result in results:
    Button(f6, text=result).pack()


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
