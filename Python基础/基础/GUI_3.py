# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk

window = tk.Tk()
window.title('THIS IS MY FOURTH PROJECT')
window.geometry('500x500')
l_ = tk.Label(window, text=None, width=20, fg='green', font=('Arial', 14))
l_.pack()


def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        l_.config(text='I only love Python')
    elif var1.get() == 0 and var2.get() == 1:
        l_.config(text='I only love Java')
    elif var1.get() == 0 and var2.get() == 0:
        l_.config(text='I do not love either')
    else:
        l_.config(text='I love Java and Python')


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c2 = tk.Checkbutton(window, text='Java', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2.pack()
window.mainloop()
