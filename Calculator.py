from tkinter import *
app = Tk()
app.title("Calculator")
app.wm_iconbitmap("Icon.ico")

def add(obj):
        global operator
        operator= operator + str(obj)
        entry.set(operator)
def clear():
    global operator
    operator=""
    entry.set(operator)
def equal():
    global operator
    evaluate=str(eval(operator))
    entry.set(evaluate)
x=16
y=8
entry = StringVar()
operator=""
screen = Entry(app, font=('arial',10),textvariable=entry, width=30, bg='powder blue', bd=20)
screen.grid(row=0, column=0, columnspan=28)


seven = Button(app,padx=x,pady=y, text="7", bd=5, width=3,command=lambda:add("7"))
seven.grid(row=1, column=0)
eight = Button(app,padx=x,pady=y, text="8", bd=5,width=3, command=lambda:add("8"))
eight.grid(row=1, column=1)
nine = Button(app,padx=x,pady=y, text="9", bd=5, width=3, command=lambda:add("9"))
nine.grid(row=1, column=2)
ac = Button(app,padx=x,pady=y,text="AC", bg='red', bd=5, command=clear)
ac.grid(row=1, column=3)

four = Button(app, padx=x, pady=y, text="4",bd=5, width=3,command=lambda:add("4"))
four.grid(row=2, column=0)
five = Button(app,padx=x,pady=y, text="5", bd=5,width=3, command=lambda:add("5"))
five.grid(row=2, column=1)
six = Button(app, padx=x, pady=y,text="6",bd=5,width=3, command=lambda:add("6"))
six.grid(row=2, column=2)
plus = Button(app,padx=x, pady=y, text="+", bd=5, bg='sky blue',width=3, command=lambda:add("+"))
plus.grid(row=2, column=3)

one = Button(app,padx=x, pady=y, text="1", bd=5,width=3,command=lambda:add("1"))
one.grid(row=3, column=0)
two = Button(app, padx=x, pady=y,text="2", bd=5, width=3,command=lambda:add("2"))
two.grid(row=3, column=1)
three =Button(app,padx=x, pady=y, text="3", bd=5,width=3, command=lambda:add("3"))
three.grid(row=3, column=2)
minus = Button(app, padx=x, pady=y,text="-", bd=5, bg='sky blue',width=3,command=lambda:add("-"))
minus.grid(row=3, column=3)

point = Button(app,padx=x,pady=y, text=".",bd=5, width=3, command=lambda:add("."))
point.grid(row=4, column=2, )
zero = Button(app, padx=x, pady=y, text="0", bd=5, width=14,command=lambda:add("0"))
zero.grid(row=4, column=0, columnspan=2)
equal = Button(app, padx=x,pady=y, text="=",font=('ariel',10,'bold'), bd=5, bg='red',width=12, command=equal)
equal.grid(row=5, column=0, columnspan=2)

divide = Button(app, padx=x,pady=y,text="/", bd=5, bg='sky blue',width=3, command=lambda:add("/"))
divide.grid(row=4, column=3)
multiply = Button(app, padx=x,pady=y,text="X", bd=5, bg='sky blue',width=12, command=lambda:add("*"))
multiply.grid(row=5, column=2, columnspan=2)

app.mainloop()

