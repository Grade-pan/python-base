# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk

window = tk.Tk()
window.title('NCH IS SILLY BOY')
window.geometry('500x500')
var = tk.StringVar()

l_ = tk.Label(window, textvariable=var, bg='yellow', fg='green', font=('Arial', 12), width=30, height=2)
l_.pack()
on_hit = False


def hit_me():
    # global意为将变量设置为全局变量
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('登陆成功')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
e1 = tk.Entry(window, show=None, font=('Arial', 14))
e2 = tk.Entry(window, show='*', font=('Arial', 14))
e = tk.Entry(window, ahow=None)
e1.pack()
e2.pack()
e.pack()
b.pack()


def insert_point():  # 在鼠标焦点处插入输入内容
    var1 = e.get()
    t.insert('insert', var1)


def insert_end():  # 在文本框内容最后接着插入输入内容
    var1 = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=3)
t.pack()

window.mainloop()
