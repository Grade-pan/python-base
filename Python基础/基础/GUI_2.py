# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk

window = tk.Tk()
window.title('THIS IS MY THIRD PROJECT')
window.geometry('500x500')
var = tk.StringVar()
l_ = tk.Label(window, text=None, bg='yellow', fg='green', font='Arial,15', width=20)
l_.pack()


def print_selection():
    l_.config(text='you have selected ' + var.get())


r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r1.pack()
r2.pack()
r3.pack()
window.mainloop()
