# -*- coding: UTF-8 -*-

# Filename:图形用户界面.py
# author by : PXY
import tkinter as tk

window = tk.Tk()
window.title('THIS IS MY SEVENTH PROJECT')
window.geometry('500x500')
l_ = tk.Label(window, text=' ', bg='green')
l_.pack()
counter = 0


def d0_job():
    global counter
    l_.config(text='d0 this ' + str(counter))
    counter += 1


def add(x, y):
    l_.config(text=str(x) + '+' + str(y) + '=' + str(x + y))


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='Add', command=add(a, b))
filemenu.add_command(label='New', command=d0_job)
filemenu.add_command(label='new', command=d0_job)
filemenu.add_command(label='Open', command=d0_job)
filemenu.add_command(label='Save as', command=d0_job)
filemenu.add_command(label='Open recent', command=d0_job)
filemenu.add_command(label='Close project', command=d0_job)
filemenu.add_command(label='Rename project', command=d0_job)
filemenu.add_command(label='settings', command=d0_job)
filemenu.add_command(label='other settings', command=d0_job)
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='edit', menu=editmenu)
editmenu.add_command(label='Undo typing', command=d0_job)
editmenu.add_command(label='Redo', command=d0_job)
editmenu.add_command(label='cut', command=d0_job)
editmenu.add_command(label='copy', command=d0_job)
editmenu.add_command(label='copy path', command=d0_job)
editmenu.add_command(label='copy reference', command=d0_job)
editmenu.add_command(label='paste', command=d0_job)
editmenu.add_command(label='delete', command=d0_job)
editmenu.add_command(label='find', command=d0_job)
# 创建二级菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Python file', command=d0_job)
window.config(menu=menubar)
window.mainloop()
