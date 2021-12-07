from tkinter import *
from psycopg2 import *
import psycopg2
from tkinter import messagebox

# Connect to PSQL Database
connection = psycopg2.connect(user="kagebo",
                              password="D1EIvI0A",
                              host="psql-dd1368-ht21.sys.kth.se",
                              database="kagebo")

# The cursor is used to perform database operations
cursor = connection.cursor()

# Executing a SQL query
cursor.execute("SELECT version();")
# Fetch result
record = cursor.fetchone()
print("You are connected to - ", record, "\n")


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

v1 = StringVar()

for frame in (f1, f2, f3, f4, f5, f6, f7, f8):
    frame.grid(row=0, column=0, sticky='news')

# Login page GUI
Label(f1, text="User ID").pack()
admin_id = StringVar(f1)  # stores current input
Entry(f1, textvariable=admin_id).pack()
Button(f1, text="Login", command=lambda: login_verification(admin_id)).pack()


# Login user_id query
def login_verification(key):
    cursor.execute("select 1 from admins where userid=" + key.get())

    if cursor.fetchone():  # if query returns true
        switch_frame(f1, f2)
        connection.commit()  # commit to the database


# create/search toggle GUI
Label(f2, text="Choose between creating or searching for items:").pack()
Button(f2, text="Add a User", command=lambda: switch_frame(f2, f3)).pack()
Button(f2, text="Add a Book", command=lambda: switch_frame(f2, f4)).pack()
Button(f2, text="Search", command=lambda: switch_frame(f2, f5)).pack()

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

Button(f3, text="Create User", command=lambda: add_user()).pack()


def add_user():
    cursor.execute("insert into users values (" + int(user_id.get()) + ", " + str(name.get()) + ", " +
                   str(address.get()) + ", " + str(email.get()) + ")")
    cursor.execute("insert into admins values (" + int(user_id.get()) + ", " + str(department.get()) + ", " +
                   str(phone_number.get()) + ")")
    cursor.execute("insert into students values (" +
                   int(user_id.get()) + ", " + str(program.get()) + ")")
    connection.commit()
    popup()


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

Label(f4, text="Edition:").pack()
edition = StringVar(f4)
Entry(f4, textvariable=edition).pack()

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

Button(f4, text="Create Book", command=lambda: add_book()).pack()


def add_book():
    # cursor.execute("insert into books values (" + book_id.get() +
    #                "," + title.get() + "," + pages.get() + ")")
    #                physical_id.get() + "," + damaged.get() + "," + prequel_id.get() + "," + isbn.get() + "," +
    #                edition.get() + "," + publisher.get())
    cursor.execute("insert into TABLE values (")
    cursor.execute("insert into TABLE values (")
    cursor.execute("insert into TABLE values (")
    cursor.execute("insert into TABLE values (")
    cursor.execute("insert into TABLE values (")
    cursor.execute("insert into TABLE values (")

    connection.commit()
    popup()


# search GUI
search_settings = {}
cursor.execute("select distinct language from language")
connection.commit()
language_options = cursor.fetchall()
menubutton = Menubutton(f5, text="Languages", indicatoron=True, borderwidth=1)
menu = Menu(menubutton, tearoff=False)
menubutton.configure(menu=menu)
languagechoices = {}

for choice in language_options:
    languagechoices[choice] = IntVar(value=0)
    menu.add_checkbutton(label=choice, variable=languagechoices[choice],
                         onvalue=1, offvalue=0)

Label(f5, text="Search")
Radiobutton(f5, text="User", value=1, indicatoron=0,
            variable=v1).pack()
Radiobutton(f5, text="Book", value=2, indicatoron=0,
            variable=v1).pack()
search_string = StringVar(f5)
Entry(f5, textvariable=search_string).pack()
Label(f5, text="Search Criteria:").pack()


results = {}
bookdict = {}
userdict = {}


def search_user():
    entry = search_string.get()
    if entry == "":
        cursor.execute("select userid, name, address, email, cast(userid in (select userid from admins) as varchar) as role from users order by name")
    else:
        cursor.execute(f"select userid, name, address, email, cast(userid in (select userid from admins) as varchar) as role from users where name ~* '{entry}' OR cast(userid as varchar) ~* '{entry}' order by name")
    connection.commit()
    results = cursor.fetchall()
    print("res:", results)
    for userid, name, address, email, admin in results:
        userdict[userid] = {
            "userid": userid,
            "name": name,
            "address": address,
            "email": email,
            "admin": admin
        }
    text = Text(f6)
    text.pack(side="left")
    sb = Scrollbar(f6, command=text.yview)
    sb.pack(side="right")
    text.configure(yscrollcommand=sb.set)
    for user in userdict.values():
        if user['admin'] == 'true':
            cursor.execute(f"select department, phonenumber from admins where userid={user['userid']}")
            connection.commit()
            user['department'], user['phonenumber'] = cursor.fetchone()
        else:
            cursor.execute(f"select program from students where userid={user['userid']}")
            connection.commit()
            user['program'], = cursor.fetchone() # rör inte kommatecknet, det behövs
        b = Button(text, text=f"[{'Admin' if user['admin'] == 'true' else 'Student'}] {user['userid']} - {user['name']}", command=lambda u=user: result_details(u, "user"))
        b.pack()
        text.window_create("end", window=b)
        text.insert("end", "\n")
    text.configure(state="disabled")
    switch_frame(f5, f6)
    print(bookdict)


def search_book():
    whereclause = ""
    for language, val in languagechoices.items():
        if val.get() == 0:
            continue
        if whereclause != "":
            whereclause += " OR "
        whereclause += f"language = \'{language[0]}\'"

    entry = search_string.get()
    if entry != "":
        if whereclause != "":
            whereclause += "AND"
        whereclause += f" (title ~* \'{entry.lower()}\' OR author ~* \'{entry.lower()}%\')"
    cursor.execute(
        "select bookid, title, author, genre, language, pages, isbn, publisher, edition, concat(dop) from author natural join "
        f"books natural join edition natural join language natural join genre {'where ' if whereclause != '' else ''}" + whereclause)
    connection.commit()
    results = cursor.fetchall()
    print(whereclause)
    print(results)
    for bookid, title, author, genre, language, pages, isbn, publisher, edition, dop in results:
        bookdict[bookid] = {
            "bookid": int(bookid),
            "title": title,
            "author": author,
            "genre": genre,
            "language": language,
            "pages": pages,
            "isbn": isbn,
            "publisher": publisher,
            "dop": str(dop),
            "edition": int(edition)
        }
    print("bd = ", bookdict)
    text = Text(f6)
    text.pack(side="left")
    sb = Scrollbar(f6, command=text.yview)
    sb.pack(side="right")
    text.configure(yscrollcommand=sb.set)
    for book in bookdict.values():
        b = Button(text, text=f"{book['title']} - {book['author']}", command=lambda bo=book: result_details(bo, 'book'))
        b.pack()
        text.window_create("end", window=b)
        text.insert("end", "\n")
    text.configure(state="disabled")
    switch_frame(f5, f6)
    print(bookdict)


Button(f5, text="Search", command=lambda: search_book() if v1.get() == "2" else search_user()).pack()

menubutton.pack()  # add language list

# search results GUI
Label(f6, text="Search Results:").pack()


# tillfallig array for att kunna skriva koden
# results = ["Harry Potter", "Alfons", "Brott och straff"]

# Book detailed view GUI + update/delete

def switch_frame(from_frame: Frame, to_frame: Frame):
    raise_frame(to_frame)
    for widget in from_frame.winfo_children():
        widget.destroy()


def result_details(result: dict, type):
    raise_frame(f7)
    temp = {}
    for key, val in result.items():
        Label(f7, text=f"{key}: {val}").pack()
    for key, val in temp.items():
        result[key] = val

    Button(f7, text="Edit", command=lambda: edit_info(result, type)).pack()
    Button(f7, text="Back", command=lambda: switch_frame(f7, f6)).pack()
    Label(f7, text="Physical Copies:").pack()

    # Get physical copies
    if type == 'book':
        cursor.execute(f"select r.physicalid, title, damaged from books left join resources r on books.bookid = r.bookid where r.bookid={result['bookid']}")
    else:
        cursor.execute(
            f"select physicalid, title, damaged from (books natural join resources ) natural join borrowing where borrowing.userid={result['userid']} and dor IS NULL")
    connection.commit()
    bookcopy = {}
    for physicalid, title, damaged in cursor.fetchall():
        bookcopy[physicalid] = {}
        cursor.execute(f"select name, concat(dob), concat(doe) from users natural join borrowing where dor is null and physicalid={physicalid} and userid ={result['userid']}")
        connection.commit()
        temp = cursor.fetchall()
        print("temp = ",temp)
        if temp:
            borrower, dob, doe = temp[0]
            bookcopy[physicalid]["status"] = f"{title} - Borrowed by {borrower} on {dob}, expires {doe}"
        else:
            bookcopy[physicalid]["status"] = f"{title} - Available in {'damaged' if damaged == 'true' else 'good'} condition"
        bookcopy[physicalid]["damaged"] = damaged

    text = Text(f7)
    text.pack(side="left")
    sb = Scrollbar(f7, command=text.yview)
    sb.pack(side="right")
    text.configure(yscrollcommand=sb.set)
    for physicalid in bookcopy.keys():
        b = Button(text, text=f"{physicalid} - {bookcopy[physicalid]['status']}")
        b.pack()
        text.window_create("end", window=b)
        text.insert("end", "\n")
    text.configure(state="disabled")


# will need input i form av datastruktur som contains alla attribut till tupeln

def edit_info(bookcopy, type):
    raise_frame(f8)
    edits = {}
    for key, val in bookcopy.items():
        Label(f8, text=key).pack()
        if key == "bookid" or key == "userid":
            Label(f8, text=val).pack()
            edits[key] = val
            continue
        else:
            if isinstance(val, int):
                entry = Entry(f8, textvariable=IntVar(f8, val))
            else:
                entry = Entry(f8, textvariable=StringVar(f8, val))
            entry.pack()
            edits[key] = entry

    Button(f8, text="Save", command=lambda: update_book(bookcopy, edits) if type == 'book' else update_user(bookcopy, edits)).pack()
    Button(f8, text="Back", command=lambda: switch_frame(f8, f7)).pack()


def update_user(old: dict, edits: dict):
    for key, val in edits.items():
        if key == 'userid' or key == 'admin':
            continue
        old[key] = val.get()

    cursor.execute(f"update users set name = '{edits['name'].get()}', address = '{edits['address'].get()}', email = '{edits['email'].get()}' where userid = {edits['userid']}")

    if old['admin'] == 'true':
        cursor.execute(f"update admins set department = '{edits['department'].get()}', phonenumber = '{edits['phonenumber'].get()}' where userid = {edits['userid']}")
    else:
        cursor.execute(f"update students set program = '{edits['program'].get()}' where userid = {edits['userid']}")

    connection.commit()
    messagebox.showinfo(box_title, "Entry has been edited!")
    switch_frame(f8, f7)


def update_book(old: dict, edits: dict):
    for key, val in edits.items():
        if key == 'bookid':
            continue
        old[key] = val.get()

    cursor.execute(f"update books set title = '{edits['title'].get()}', pages = {edits['pages'].get()} where bookid = {edits['bookid']}")
    cursor.execute(
        f"update author set author = '{edits['author'].get()}' where bookid = {edits['bookid']} and author = '{old['author']}'")
    cursor.execute(
        f"update edition set isbn = '{edits['isbn'].get()}', edition = {edits['edition'].get()}, publisher = '{edits['publisher'].get()}', dop = '{edits['dop'].get()}' where bookid = {edits['bookid']}")
    cursor.execute(
        f"update genre set genre = '{edits['genre'].get()}' where bookid = {edits['bookid']} and genre = '{old['genre']}'")
    cursor.execute(
        f"update language set language = '{edits['language'].get()}' where bookid = {edits['bookid']} and language = '{old['language']}'")
    connection.commit()
    messagebox.showinfo(box_title, "Entry has been edited!")
    switch_frame(f8, f7)


# render initial GUI
raise_frame(f1)

# program loop
root.mainloop()
