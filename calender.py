from tkinter import *
import calendar

root = Tk()
root.title("Calendar")

# Functions

def text():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)


# Labels
label1 = Label(root, text="Month:")
label1.grid(row=0, column=0)

label2 = Label(root, text="Year:")
label2.grid(row=0, column=1)

# spinboxs
month = Spinbox(root, from_=1, to=12, width=8)
month.grid(row=1, column=0, padx=5)

year = Spinbox(root, from_=2000, to=2100, width=10)
year.grid(row=1, column=1, padx=10)

# Buttons
button = Button(root, text="Go", command=text)
button.grid(row=1, column=2, padx=10)

# Textfields
textfield = Text(root, width=25, height=10, fg="red")
textfield.grid(row=2, columnspan=2)

# mainloop
root.mainloop()