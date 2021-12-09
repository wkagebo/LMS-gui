from tkinter import *
from psycopg2 import *
import psycopg2
from tkinter import messagebox

box_title = "Success!"
root = Tk()
# initialize frames used in the GUI
frame_initial = Frame(root)
frame_add = Frame(root)
frame_search = Frame(root)
frame_search_results = Frame(root)
frame_result_details = Frame(root)
frame_edit = Frame(root)
v1 = StringVar()
isdamagedglobalvariablecauseidkhowtofixthecheckbutton = StringVar(frame_add)

for frame in (frame_initial, frame_add, frame_search, frame_search_results, frame_result_details, frame_edit):
    frame.grid(row=0, column=0, sticky='news')


def raise_frame(frame):
    frame.tkraise()


def popup():
    messagebox.showinfo(
        box_title, "Entry was successfully added to the database!")


def popup_deletion():
    messagebox.showinfo(box_title, "Entry has been deleted!")


def raise_initial_frame(from_frame):
    # create/search toggle GUI
    Label(frame_initial, text="Choose between creating or searching for items:").pack()
    Button(frame_initial, text="Add a User", command=lambda: add_new("user")).pack()
    Button(frame_initial, text="Add a Book", command=lambda: add_new("book")).pack()
    Button(frame_initial, text="Search", command=lambda: search(frame_initial)).pack()
    if from_frame:
        switch_frame(from_frame, frame_initial)
    else:
        raise_frame(frame_initial)


# Creation GUI
def add_new(type):
    values = {}
    switch_frame(frame_initial, frame_add)
    if type == "user":
        Label(frame_add, text='userid').pack()
        entry = Entry(frame_add, textvariable=IntVar(frame_add))
        values['userid'] = entry
        entry.pack()
        for key in ['name', 'address', 'email', 'program']:
            Label(frame_add, text=key).pack()
            entry = Entry(frame_add, textvariable=StringVar(frame_add))
            values[key] = entry
            entry.pack()
    elif type == "book":
        for key in ['title', 'author', 'genre', 'language', 'isbn', 'publisher', 'dop']:
            Label(frame_add, text=key).pack()
            entry = Entry(frame_add, textvariable=StringVar(frame_add))
            values[key] = entry
            entry.pack()
        for key in ['bookid', 'pages', 'edition', 'prequelid']:
            Label(frame_add, text=key).pack()
            entry = Entry(frame_add, textvariable=IntVar(frame_add))
            values[key] = entry
            entry.pack()
    else:
        Label(frame_add, text='bookid').pack()
        values['bookid'] = type
        Label(frame_add, text=type).pack()

        Label(frame_add, text='physicalid').pack()
        entry = Entry(frame_add, textvariable=IntVar(frame_add))
        values['physicalid'] = entry
        entry.pack()

        Label(frame_add, text='damaged').pack()
        entry = Checkbutton(frame_add, variable=isdamagedglobalvariablecauseidkhowtofixthecheckbutton, onvalue='true',
                            offvalue='false')
        # values['damaged'] = entry
        entry.pack()

    Button(frame_add, text="Add",
           command=lambda val=values, typ=type: create(val, typ)).pack()
    Button(frame_add, text="Back", command=lambda: raise_initial_frame(frame_add)).pack()


def create(values, type):
    if type == "user":
        cursor.execute(
            f"insert into users (userid, name, address, email) values ({values['userid'].get()}, '{values['name'].get()}', '{values['address'].get()}', '{values['email'].get()}')")
        cursor.execute(
            f"insert into students (userid, program) values ({values['userid'].get()}, '{values['program'].get()}')")
    elif type == "book":
        cursor.execute(
            f"insert into books (bookid, title, pages) values ({values['bookid'].get()}, '{values['title'].get()}', {values['pages'].get()})")
        cursor.execute(
            f"insert into author (bookid, author) values ({values['bookid'].get()}, '{values['author'].get()}')")
        cursor.execute(
            f"insert into genre (bookid, genre) values ({values['bookid'].get()}, '{values['genre'].get()}')")
        cursor.execute(
            f"insert into language (bookid, language) values ({values['bookid'].get()}, '{values['language'].get()}')")
        temp = values['prequelid'].get()
        if temp:
            cursor.execute(
                f"insert into prequels (bookid, prequelid) values ({values['bookid'].get()}, '{values['prequelid'].get()}')")

        cursor.execute(
            f"insert into edition (bookid, isbn, edition, publisher, dop) values ({values['bookid'].get()}, '{values['isbn'].get()}', {values['edition'].get()}, '{values['publisher'].get()}', '{values['dop'].get()}')")
    else:
        cursor.execute(
            f"insert into resources (physicalid, bookid, damaged) values ({values['physicalid'].get()}, {values['bookid']}, '{isdamagedglobalvariablecauseidkhowtofixthecheckbutton.get()}')")
    connection.commit()
    popup()
    raise_initial_frame(frame_add)


def search(from_frame):
    switch_frame(from_frame, frame_search)
    # search GUI
    search_settings = {}
    cursor.execute("select distinct language from language")
    connection.commit()
    language_options = cursor.fetchall()
    menubutton = Menubutton(frame_search, text="Languages", indicatoron=True, borderwidth=1)
    menu = Menu(menubutton, tearoff=False)
    menubutton.configure(menu=menu)
    languagechoices = {}

    for choice in language_options:
        languagechoices[choice] = IntVar(value=0)
        menu.add_checkbutton(label=choice, variable=languagechoices[choice],
                             onvalue=1, offvalue=0)

    Label(frame_search, text="Search")
    Radiobutton(frame_search, text="User", value=1, indicatoron=0,
                variable=v1).pack()
    Radiobutton(frame_search, text="Book", value=2, indicatoron=0,
                variable=v1).pack()
    search_string = StringVar(frame_search)
    Entry(frame_search, textvariable=search_string).pack()
    Label(frame_search, text="Search Criteria:").pack()
    Button(frame_search, text="Search", command=lambda s=search_string, lang=languagechoices: search_book(s,
                                                                                                          lang) if v1.get() == "2" else search_user(
        s)).pack()
    menubutton.pack()  # add language list
    Button(frame_search, text="Back", command=lambda: raise_initial_frame(frame_search)).pack()


def search_user(s):
    # search results GUI
    Label(frame_search_results, text="Search Results:").pack()
    userdict = {}
    entry = s.get()
    if entry == "":
        cursor.execute(
            "select userid, name, address, email, cast(userid in (select userid from admins) as varchar) as role from users order by name")
    else:
        cursor.execute(
            f"select userid, name, address, email, cast(userid in (select userid from admins) as varchar) as role from users where name ~* '{entry}' OR cast(userid as varchar) ~* '{entry}' order by name")
    connection.commit()
    results = cursor.fetchall()
    for userid, name, address, email, admin in results:
        userdict[userid] = {
            "userid": userid,
            "name": name,
            "address": address,
            "email": email,
            "admin": admin
        }
    text = Text(frame_search_results)
    text.pack(side="left")
    sb = Scrollbar(frame_search_results, command=text.yview)
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
            user['program'], = cursor.fetchone()  # rör inte kommatecknet, det behövs
        b = Button(text,
                   text=f"[{'Admin' if user['admin'] == 'true' else 'Student'}] {user['userid']} - {user['name']}",
                   command=lambda u=user: result_details(u, "user"))
        b.pack()
        text.window_create("end", window=b)
        text.insert("end", "\n")
    text.configure(state="disabled")
    Button(frame_search_results, text="Back", command=lambda: search(frame_search_results)).pack()
    switch_frame(frame_search, frame_search_results)


def search_book(s, lang):
    # search results GUI
    Label(frame_search_results, text="Search Results:").pack()
    whereclause = ""
    for language, val in lang.items():
        if val.get() == 0:
            continue
        if whereclause != "":
            whereclause += " OR "
        whereclause += f"language = \'{language[0]}\'"

    entry = s.get()
    if entry != "":
        if whereclause != "":
            whereclause += "AND"
        whereclause += f" (title ~* \'{entry.lower()}\' OR author ~* \'{entry.lower()}%\')"
    cursor.execute(
        "select bookid, title, author, genre, language, pages, isbn, publisher, edition, concat(dop) from author natural join "
        f"books natural join edition natural join language natural join genre {'where ' if whereclause != '' else ''}" + whereclause)
    connection.commit()
    results = cursor.fetchall()
    bookdict = {}
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
    text = Text(frame_search_results)
    text.pack(side="left")
    sb = Scrollbar(frame_search_results, command=text.yview)
    sb.pack(side="right")
    text.configure(yscrollcommand=sb.set)
    for book in bookdict.values():
        b = Button(text, text=f"{book['title']} - {book['author']}", command=lambda bo=book: result_details(bo, 'book'))
        b.pack()
        text.window_create("end", window=b)
        text.insert("end", "\n")
    text.configure(state="disabled")
    Button(frame_search_results, text="Back", command=lambda: search(frame_search_results)).pack()
    switch_frame(frame_search, frame_search_results)


def switch_frame(from_frame: Frame, to_frame: Frame):
    raise_frame(to_frame)
    for widget in from_frame.winfo_children():
        widget.destroy()


def result_details(result: dict, type):
    raise_frame(frame_result_details)
    temp = {}
    for key, val in result.items():
        Label(frame_result_details, text=f"{key}: {val}").pack()
    for key, val in temp.items():
        result[key] = val

    Button(frame_result_details, text="Delete", command=lambda: delete_object(result, type)).pack()
    Button(frame_result_details, text="Edit", command=lambda: edit_info(result, type)).pack()
    Button(frame_result_details, text="Back",
           command=lambda: switch_frame(frame_result_details, frame_search_results)).pack()
    Label(frame_result_details, text="Physical Copies: CLICK TO DELETE").pack()

    # Get physical copies
    if type == 'book':
        cursor.execute(
            f"select r.physicalid, title, damaged from books left join resources r on books.bookid = r.bookid where r.bookid={result['bookid']}")
    else:
        cursor.execute(
            f"select physicalid, title, damaged from (books natural join resources ) natural join borrowing where borrowing.userid={result['userid']} and dor IS NULL")
    connection.commit()
    bookcopy = {}
    for physicalid, title, damaged in cursor.fetchall():
        bookcopy[physicalid] = {}
        cursor.execute(
            f"select name, concat(dob), concat(doe) from users natural join borrowing where dor is null and physicalid={physicalid}")
        connection.commit()
        temp = cursor.fetchall()
        if temp:
            borrower, dob, doe = temp[0]
            bookcopy[physicalid]["status"] = f"{title} - Borrowed by {borrower} on {dob}, expires {doe}"
        else:
            bookcopy[physicalid][
                "status"] = f"{title} - Available in {'damaged' if damaged == 'true' else 'good'} condition"
        bookcopy[physicalid]["damaged"] = damaged

    text = Text(frame_result_details)
    text.pack(side="left")
    sb = Scrollbar(frame_result_details, command=text.yview)
    sb.pack(side="right")
    text.configure(yscrollcommand=sb.set)
    for physicalid in bookcopy.keys():
        b = Button(text, text=f"{physicalid} - {bookcopy[physicalid]['status']}",
                   command=lambda pid=physicalid: delete_object(pid, "physicalbook"))
        b.pack()
        text.window_create("end", window=b)
        text.insert("end", "\n")

    if type == "book":
        Button(frame_result_details, text="Add copy", command=lambda: add_new(result['bookid'])).pack()
    text.configure(state="disabled")


def edit_info(object, type):
    raise_frame(frame_edit)
    edits = {}
    for key, val in object.items():
        Label(frame_edit, text=key).pack()
        if key == "bookid" or key == "userid" or key == "admin":
            Label(frame_edit, text=val).pack()
            edits[key] = val
            continue
        else:
            if isinstance(val, int):
                entry = Entry(frame_edit, textvariable=IntVar(frame_edit, val))
            else:
                entry = Entry(frame_edit, textvariable=StringVar(frame_edit, val))
            entry.pack()
            edits[key] = entry

    Button(frame_edit, text="Save",
           command=lambda obj=object, ed=edits: update_book(obj, ed) if type == 'book' else update_user(obj, ed)).pack()
    Button(frame_edit, text="Delete", command=lambda obj=object, typ=type: delete_object(obj, typ)).pack()
    Button(frame_edit, text="Back", command=lambda: switch_frame(frame_edit, frame_result_details)).pack()


def delete_object(object, type):
    if type == "user":
        uid = object['userid']
        if object['admin'] == "true":
            cursor.execute(f"delete from admins where userid={uid}")
        else:
            cursor.execute(f"delete from students where userid={uid}")
        cursor.execute(f"delete from users where userid={uid}")
    elif type == "book":
        bid = object['bookid']
        cursor.execute(f"select physicalid from resources where bookid={bid}")
        connection.commit()
        for pid, in cursor.fetchall():
            delete_object(pid, "physicalbook")
        cursor.execute(f"delete from edition where bookid={bid}")
        cursor.execute(f"delete from author where bookid={bid}")
        cursor.execute(f"delete from genre where bookid={bid}")
        cursor.execute(f"delete from prequels where bookid={bid}")
        cursor.execute(f"delete from language where bookid={bid}")
        cursor.execute(f"delete from books where bookid={bid}")
    elif type == "physicalbook":
        pid = object
        cursor.execute(f"select borrowingid from borrowing where physicalid={pid}")
        connection.commit()
        for borid, in cursor.fetchall():
            cursor.execute(f"delete from transactions where borrowingid={borid}")
            cursor.execute(f"delete from fines where borrowingid={borid}")
        cursor.execute(f"delete from borrowing where physicalid={pid}")
        cursor.execute(f"delete from resources where physicalid={pid}")
    connection.commit()
    popup_deletion()


def update_user(old: dict, edits: dict):
    for key, val in edits.items():
        if key == 'userid' or key == 'admin':
            continue
        old[key] = val.get()

    cursor.execute(
        f"update users set name = '{edits['name'].get()}', address = '{edits['address'].get()}', email = '{edits['email'].get()}' where userid = {edits['userid']}")

    if old['admin'] == 'true':
        cursor.execute(
            f"update admins set department = '{edits['department'].get()}', phonenumber = '{edits['phonenumber'].get()}' where userid = {edits['userid']}")
    else:
        cursor.execute(f"update students set program = '{edits['program'].get()}' where userid = {edits['userid']}")

    connection.commit()
    messagebox.showinfo(box_title, "Entry has been edited!")
    switch_frame(frame_edit, frame_result_details)


def update_book(old: dict, edits: dict):
    for key, val in edits.items():
        if key == 'bookid':
            continue
        old[key] = val.get()

    cursor.execute(
        f"update books set title = '{edits['title'].get()}', pages = {edits['pages'].get()} where bookid = {edits['bookid']}")
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
    switch_frame(frame_edit, frame_result_details)


if __name__ == "__main__":
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

    # render initial frame
    raise_initial_frame(None)

    # program loop
    root.mainloop()
