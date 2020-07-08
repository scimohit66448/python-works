from tkinter import *


class value:
    i = 0


def clicked(button):
    current = data.get()
    clear()
    data.insert(index=0, string=current+button)


def back():
    current = data.get()
    clear()
    data.insert(0,current[:-1])


def equal():

    a = data.get()
    a = eval(str(a))
    clear()
    data.insert(0,a)


def clear():
    data.delete(0, END)
    value.i = 0

if __name__ == '__main__':
    i = 0
    root = Tk()
    root.title("Calculator")
    data = Entry(root, width=40)
    data.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    button1 = Button(root, text="1", padx=30, pady=30, command=lambda: clicked("1"))
    button2 = Button(root, text="2", padx=30, pady=30, command=lambda: clicked("2"))
    button3 = Button(root, text="3", padx=30, pady=30, command=lambda: clicked("3"))
    button4 = Button(root, text="4", padx=30, pady=30, command=lambda: clicked("4"))
    button5 = Button(root, text="5", padx=30, pady=30, command=lambda: clicked("5"))
    button6 = Button(root, text="6", padx=30, pady=30, command=lambda: clicked("6"))
    button7 = Button(root, text="7", padx=30, pady=30, command=lambda: clicked("7"))
    button8 = Button(root, text="8", padx=30, pady=30, command=lambda: clicked("8"))
    button9 = Button(root, text="9", padx=30, pady=30, command=lambda: clicked("9"))
    button0 = Button(root, text="0", padx=30, pady=30, command=lambda: clicked("0"))
    button_eq = Button(root, text="=", padx=30, pady=30, command=equal)
    button_add = Button(root, text="+", padx=30, pady=30, command=lambda: clicked("+"))
    button_sub = Button(root, text="-", padx=30, pady=30, command=lambda: clicked("-"))
    button_mul = Button(root, text="x", padx=30, pady=30, command=lambda: clicked("*"))
    button_div = Button(root, text="/", padx=30, pady=30, command=lambda: clicked("/"))
    button_pow = Button(root, text="^", padx=30, pady=30, command=lambda: clicked("**"))
    button_dec = Button(root, text=".", padx=30, pady=30, command=lambda: clicked("."))
    button_clear = Button(root, text="Clear", padx=21, pady=30, command=clear)
    button_back = Button(root, text= 'back',padx =21,pady=30,command = back)

    button1.grid(row=3, column=1)
    button2.grid(row=3, column=2)
    button3.grid(row=3, column=3)
    button4.grid(row=2, column=1)
    button5.grid(row=2, column=2)
    button6.grid(row=2, column=3)
    button7.grid(row=1, column=1)
    button8.grid(row=1, column=2)
    button9.grid(row=1, column=3)
    button0.grid(row=4, column=1)
    button_add.grid(row=4, column=2)
    button_div.grid(row=4, column=4)
    button_mul.grid(row=3, column=4)
    button_sub.grid(row=2, column=4)
    button_pow.grid(row=4, column=3)
    button_clear.grid(row=5, column=2)
    button_eq.grid(row=1, column=4)
    button_dec.grid(row=5, column=1)
    button_back.grid(row=5,column=3)
    root.mainloop()
