from tkinter import * 

root = Tk()
root.geometry('400x300')
root.title('Root Screen')

def topwin():
    top = Toplevel()
    top.geometry('180x100')
    top.title('Top Level')

    l2 = Label(top, text='This text is in Top Level window')
    l2.pack()

    top.mainloop()

l1 = Label(root, text='This text is on normal screen')
btn = Button(root, text='Click here to open top window', command=topwin)

l1.pack()
btn.pack()

root.mainloop()