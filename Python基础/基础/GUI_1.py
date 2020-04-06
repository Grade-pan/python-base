# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk

window = tk.Tk()
window.title('THIS IS MY SECOND PROJECT')
window.geometry('500x300')
var = tk.StringVar()
l_ = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), fg='yellow', width='10')
l_.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var.set(value)


b1 = tk.Button(window, text='Print_selection', width='14', height='2', command=print_selection)
b1.pack()
var1 = tk.StringVar()
var1.set(('中国', '河南省', '洛阳市', '汝阳县'))
lb = tk.Listbox(window, listvariable=var1)
list_items = ['龙门石窟', '汉魏洛阳故城', '隋唐洛阳城', '王城']
for item in list_items:
    lb.insert('end', item)
lb.insert(0, '紫微城')
lb.insert(1, '九州池')
lb.delete(2)
lb.pack()
window.mainloop()
