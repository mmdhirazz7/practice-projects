from tkinter import *

# Screen
window = Tk()
window.title("Mile to km converter")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

# Label
label1 = Label(text="Miles")
label1.grid(column=60, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="    ")
label3.grid(column=50, row=1)

label4 = Label(text="km")
label4.grid(column=60, row=1)


# Miles to km converter
def converter(n):
    return n * 1.60934


# Button
def button_clicked():
    new_text = input.get()
    output = converter(float(new_text))
    label3["text"] = str(output)


button = Button(text="calculate", command=button_clicked)
button.grid(column=50, row=50)

# Entry

input = Entry(width=10)
input.grid(column=50, row=0)

window.mainloop()
