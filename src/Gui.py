from tkinter import *
# from psycopg2 import *
# import psycopg2


def loginpage():
    R1.pack_forget()
    R2.pack_forget()

    # randomButton.pack_forget()

    mainFrame.pack()
    bottomFrame.pack(side=BOTTOM)
    entryName.pack(side=LEFT)
    userInput.pack(side=RIGHT)
    loginButton.pack(side=LEFT)


def mainpage():
    mainFrame.pack_forget()
    bottomFrame.pack_forget()
    entryName.pack_forget()
    userInput.pack_forget()
    loginButton.pack_forget()

    L1.pack()
    R1.pack()
    R2.pack()

    # randomButton.pack()

    L2.pack()
    R3.pack()
    R4.pack()


def searchmode():
    inputString.pack()

    L3.pack_forget()
    L4.pack_forget()
    L5.pack_forget()
    L6.pack_forget()


def createmode():
    inputString.pack_forget()

    L3.pack()
    L4.pack()
    L5.pack()
    L6.pack()


Screen = Tk()
Screen.title("LMS")

# Login page GUI
mainFrame = Frame(Screen)
bottomFrame = Frame(Screen)
entryName = Label(mainFrame, text="Email Address")
email = StringVar(Screen)  # stores current input
userInput = Entry(mainFrame, textvariable=email)

loginButton = Button(bottomFrame, text="Login", command=mainpage)

# initial GUI
count = 0
if count == 0:
    mainFrame.pack()
    bottomFrame.pack(side=BOTTOM)
    entryName.pack(side=LEFT)
    userInput.pack(side=RIGHT)
    loginButton.pack(side=LEFT)
    count += 1

# Main page GUI
L1 = Label(Screen, text="Choose between handling users or books:")
L2 = Label(Screen, text="Choose action:")

v1 = StringVar()
v2 = StringVar()

R1 = Radiobutton(Screen, text="User", value=1, indicatoron=0, variable=v1)
R2 = Radiobutton(Screen, text="Book", value=2, indicatoron=0, variable=v1)

#randomButton = Button(text="take me back", command=loginpage)


R3 = Radiobutton(Screen, text="Search", value=1,
                 indicatoron=0, variable=v2, command=searchmode)
R4 = Radiobutton(Screen, text="Create", value=2,
                 indicatoron=0, variable=v2, command=createmode)

# searchmode GUI

searchQuery = StringVar(Screen)
inputString = Entry(Screen, textvariable=searchQuery)

# createmode GUI
L3 = Label(Screen, text="Title")
L4 = Label(Screen, text="Author")
L5 = Label(Screen, text="physical ID")
L6 = Label(Screen, text="Year")


Screen.mainloop()


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
