# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk

window = tk.Tk()
window.title('THIS IS MY FIFTH PROJECT')
window.geometry('2000x500')
l_ = tk.Label(window, text=None, font=('Arial', 15), fg='green')
l_.pack()


def print_selection(v):
    l_.config(text='you have selected' + v)
    return l_.config(v)


# from_ , 设置最小值；to , 设置最大值；resolution , 设置步距值；orient = HORIZONTAL #设置水平方向,默认为垂直方向,tickinterval 设置等差值
s = tk.Scale(window, label='请拖动下面的方块', from_=0, to=100, orient=tk.HORIZONTAL, length=2000, tickinterval=5,
             resolution=0.0001, command=print_selection)
s.pack()
window.mainloop()
