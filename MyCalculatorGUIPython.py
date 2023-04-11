#Here I am importing all the needed libraries

from tkinter import *

#variable to store the user entered expression
exp=""

#Function to store the values entered by user (number and operators)
def press_keys(number_on_keys):
    global exp
    exp += str(number_on_keys)
    users_equation.set(exp)

def equal_key_press():
    try:
        global exp
        #eval to evaluate the expression
        total = str(exal(exp))
        users_equation.set(total)
        #initialize the expression variable
        expression = ""
    except:
        #display syntax error if we are unable to evaluate user expression
        users_equation.set("Syntax error ")
        exp =""

#Function to clear the entered expression
def clean_up():
    global exp
    exp=""
    users_equation.set("")

#To create root window
tk = Tk()
tk.configure(background="grey")
tk.title("Calculator")
tk.geometry("280x280")

#To store the values entered by the user
users_equation = StringVar()

#Entry Box to accept the user's expression(input)
Text_User_Input_Box = Entry(tk, textvariable=users_equation, width=20)
Text_User_Input_Box.grid(columnspan=8, ipadx=100)

h2 = 2
w7 = 7
fgb = "black"
bghash = "#8f8f8f"



button1 = Button(tk, text=" 1 ", fg=fgb, bg=bghash, command=lambda:press_keys(1), height=2, width=7)
button1.grid(row=2,column=0)

button2 = Button(tk, text=" 2 ",fg=fgb, bg=bghash, command=lambda:press_keys(2),  height=2, width=7)
button2.grid(row=2,column=1)

button3 = Button(tk, text=" 3 ",fg=fgb, bg=bghash, command=lambda:press_keys(3),  height=2, width=7)
button3.grid(row=2,column=2)

button4 = Button(tk, text=" 4 ", fg=fgb, bg=bghash, command=lambda:press(4),  height=2, width=7)
button4.grid(row=3,column=0)

button5 = Button(tk, text=" 5 ", fg=fgb, bg=bghash, command=lambda:press_keys(5),  height=2, width=7)
button5.grid(row=3, column=1)

button6 = Button(tk, text=" 6 ", fg=fgb, bg=bghash, command=lambda:press_keys(6),  height=2, width=7)
button6.grid(row=3, column=2)

button7 = Button(tk, text=" 7 ",fg=fgb,bg=bghash, command=lambda:press_keys(7),  height=2, width=7)
button7.grid(row=4,column=0)

button8 = Button(tk, text=" 8 ", fg=fgb, bg=bghash, command=lambda:press_keys(8),  height=2, width=7)
button8.grid(row=4,column=1)

button9 = Button(tk, text=" 9 ", fg=fgb, bg=bghash, command=lambda:press_keys(9),  height=2, width=7)
button9.grid(row=4, column=2)

button0 = Button(tk, text=" 0 ", fg=fgb, bg=bghash, command=lambda:press_keys(0),  height=2, width=7)
button0.grid(row=5, column=0)

plus = Button(tk, text =" + ", fg=fgb, bg=bghash, command=lambda:press_keys("+"),  height=2, width=7)
plus.grid(row=5, column=1)

minus = Button(tk, text=" - ", fg=fgb, bg=bghash, command=lambda:press_keys("-"),  height=2, width=7)
minus.grid(row=5,column=2)

multiply = Button(tk, text=" * ", fg=fgb, bg=bghash, command=lambda:press_keys("*"),  height=2, width=7)
multiply.grid(row=6,column=0)

divide = Button(tk, text=" / ", fg=fgb, bg=bghash, command=lambda:press_keys("/"),  height=2, width=7)
divide.grid(row=6, column=1)

equal = Button(tk, text=" = ", fg=fgb, bg=bghash, command=equal_key_press(),  height=2, width=7)
equal.grid(row=6, column=2)

clean = Button(tk, text="Clear", fg=fgb, bg=bghash, command=clean_up(),  height=2, width=7)
clean.grid(row=7, column=0)

#Run the GUI of the calculator
tk.mainloop()