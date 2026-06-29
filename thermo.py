from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ "degree C")

window = Tk()

scale = Scale(window, from_=100, to=0, length=500, tickinterval_=10, troughcolor='#ff1c00', fg='#69fafe', bg='#111111')
scale.pack()

button = Button(window, text='Submit', command=submit)
button.pack()
window.mainloop()