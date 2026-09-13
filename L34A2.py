from tkinter import *
from datetime import date

root = Tk()
root.title('Demo Window')
root.geometry('400x300')

lbl = Label(Text = "Hey There!", fg = "White", bg = "Orange", height = 1, width = 300)
name_entry = Entry()

name_lbl = Label(text="Full Name", bg="Red")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to my app! and todays date is"
    greet = "hello" +name
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="White")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()