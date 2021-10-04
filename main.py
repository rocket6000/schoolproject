from tkinter import *
import parser
rootcontain = Tk()
# This is the "ScreenGui" of python
rootcontain.title("Scientific Calculator (Python) - rocket")
# Makes title of container
rootcontain.geometry("355x355")
mainframe = Frame(rootcontain, width=355, height=355)

img = PhotoImage(file="calgfrbhg4.png")
rootcontain.iconphoto(False,img)
textbox = Entry(mainframe,width=20,font="Calibri 20") # makes the textbox
textbox.rowconfigure(1,weight=1)
textbox.grid(row=1,columnspan=4, sticky=N+E+W+S) # makes the size
# NUMBER BUTTONS
i = 0
def getvaribles(number):
    global i
    textbox.insert(i, number)
    i += 1

def getoperator(operator):
    global i
    boollength = len(operator)
    textbox.insert(i, operator)
    i += boollength

def domath():
    expression = textbox.get()
    try:
        exp = parser.expr(expression).compile()
        result = eval(exp)
        print(result)
        textbox.delete(0,END)
        textbox.insert(0,result)
    except Exception:
        textbox.delete(0,END)
        textbox.insert(0,"Invalid Expression")

def clear():
    textbox.delete(0,END)



Grid.rowconfigure(mainframe,0, weight=7)
# Row 2
textbutton = Button(mainframe,height=3, text="1", command=lambda:getvaribles(1)) # makes a button
textbutton.grid(row=2, column=0,sticky=N+E+W+S)
textbutton = Button(mainframe, text="2", command=lambda:getvaribles(2)) # makes a button
textbutton.grid(row=2, column=1,sticky=N+E+W+S)
textbutton = Button(mainframe, text="3", command=lambda:getvaribles(3)) # makes a button
textbutton.grid(row=2, column=2,sticky=N+E+W+S)
# Row 3
textbutton = Button(mainframe,height=3, text="4", command=lambda:getvaribles(4)) # makes a button
textbutton.grid(row=3, column=0,sticky=N+E+W+S)
textbutton = Button(mainframe, text="5", command=lambda:getvaribles(5)) # makes a button
textbutton.grid(row=3, column=1,sticky=N+E+W+S)
textbutton = Button(mainframe, text="6", command=lambda:getvaribles(6)) # makes a button
textbutton.grid(row=3, column=2,sticky=N+E+W+S)
# Row 4
textbutton = Button(mainframe,height=3, text="7", command=lambda:getvaribles(7)) # makes a button
textbutton.grid(row=4, column=0,sticky=N+E+W+S)
textbutton = Button(mainframe, text="8", command=lambda:getvaribles(8)) # makes a button
textbutton.grid(row=4, column=1,sticky=N+E+W+S)
textbutton = Button(mainframe, text="9", command=lambda:getvaribles(9)) # makes a button
textbutton.grid(row=4, column=2,sticky=N+E+W+S)
# Row 5
textbutton = Button(mainframe,height=3, text="=", command=lambda:domath()) # makes a button
textbutton.grid(row=5, column=0,sticky=N+E+W+S)
textbutton = Button(mainframe, text="0", command=lambda:getvaribles(1)) # makes a button
textbutton.grid(row=5, column=1,sticky=N+E+W+S)
textbutton = Button(mainframe, text=".", command=lambda:getvaribles(".")) # makes a button
textbutton.grid(row=5, column=2,sticky=N+E+W+S)
# Operator Buttons
textbutton = Button(mainframe, text="+", command=lambda:getoperator("+")) # makes a button
textbutton.grid(row=2, column=3,sticky=N+E+W+S)
textbutton = Button(mainframe, text="-", command=lambda:getoperator("-")) # makes a button
textbutton.grid(row=3, column=3,sticky=N+E+W+S)
textbutton = Button(mainframe, text="X", command=lambda:getoperator("*")) # makes a button
textbutton.grid(row=4, column=3,sticky=N+E+W+S)
textbutton = Button(mainframe, text="÷", command=lambda:getoperator("/")) # makes a button
textbutton.grid(row=5, column=3,sticky=N+E+W+S)

textbutton = Button(mainframe,height=3, text="CLEAR", command=lambda:clear()) # makes a button
textbutton.grid(row=6, columnspan=4,sticky=N+E+W+S)

mainframe.pack() # should put it at the end
rootcontain.mainloop() # loops the code so it doesn't stop when the code is finished. It must be at the end.

# rocket6000
