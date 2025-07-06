from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x200')
root.title('Password Strength Checker')

password_enter = Label(root, text="Please Enter Password:")
password_enter.grid(row=0, column=0, padx=10, pady=10, sticky=W)

password = Entry(root, show="*")
password.grid(row=0, column=1, padx=10, pady=10)


def display():
    pword = password.get()

    if len(pword) <= 6:
        strength.config(text='Password is Weak', fg='red')
    elif 6 < len(pword) <= 10:
        strength.config(text='Password is Moderate', fg='grey')
    else:
        strength.config(text='Password is Strong', fg='green')


btn = Button(root, text="Check Strength", command=display)
btn.grid(row=1, column=0, columnspan=2, pady=10)

strength = Label(root, text="", font=('Arial', 12))
strength.grid(row=2, column=0, columnspan=2)

root.mainloop()
