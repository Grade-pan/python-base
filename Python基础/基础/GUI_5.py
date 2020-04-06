# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk
from logging import root

window = tk.Tk()
window.title('THIS IS MY SIXTH PROJECT')
window.geometry('800x1000')
canvas = tk.Canvas(window, height=500, width=1000)
# 画图
x0, y0, x1, y1 = 0, 0, 0, 0
line = canvas.create_line(x0 + 50, y0 + 50, x1, y1, fill='red')
oval = canvas.create_oval(x0 + 300, y0 + 300, x1 + 50, y1 + 50, fill='green')
rect = canvas.create_rectangle(330, 30, 500, 200, fill='blue')
canvas.pack()


def move_rect():
    canvas.move(rect, 20, 20)


def move_line():
    canvas.move(line, 20, 20)


def move_oval():
    canvas.move(oval, 20, 20)


b = tk.Button(window, text='move rect', command=move_rect, anchor='w')
b2 = tk.Button(window, text='move line', command=move_line)
b3 = tk.Button(window, text='move oval', command=move_oval, anchor='e')
b.pack()
b2.pack()
b3.pack()
window.mainloop()
