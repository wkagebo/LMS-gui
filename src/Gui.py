from tkinter import *

# Login page GUI
startScreen = Tk()
startScreen.title("Admin Login")

mainFrame = Frame(startScreen)
mainFrame.pack()

bottomFrame = Frame(startScreen)
bottomFrame.pack(side=BOTTOM)

entryName = Label(mainFrame, text="Email Address")
entryName.pack(side=LEFT)

userInput = Entry(mainFrame)
userInput.pack(side=RIGHT)

loginButton = Button(bottomFrame, text="Login")
loginButton.pack(side=LEFT)

startScreen.mainloop()
