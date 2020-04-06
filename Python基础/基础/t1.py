import re
import tkinter as tk
import urllib
from urllib import request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    imgre = re.compile(r'src="(.+?\.jpg)"')
    html = html.decode('utf-8')  # python3
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1


def start(url):
    html = getHtml(url)
    print(getImg(html))


x = tk.Tk()
label1 = tk.Label(x, text="请输入网址：")
label1.grid(row=0, column=0)
label2 = tk.Label(x, text="请输入文件存放路径：")
label2.grid(row=1, column=0)
var1 = tk.StringVar()
entry1 = tk.Entry(x, textvariable=var1)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(x)
entry2.grid(row=1, column=1)


def seturl():
    url = "https://tieba.baidu.com/p/5475267611"
    # 本来想动态获取文本框输入的，不知道为什么WINDOWS10上运行返回值是NONE，
    # 另一台电脑WIN7却又可以，不知道是不是环境配置问题
    # print(var1.get())
    start(url)


cbbtn1 = tk.Checkbutton(x, text="同意协议")
cbbtn1.grid(row=2, column=0)

btn1 = tk.Button(x, text="开始抓取", command=seturl)
btn1.grid(row=2, column=2)
btn2 = tk.Button(x, text="取消")
btn2.grid(row=2, column=3)

# img = tk.PhotoImage(file = "C:\Users\123456\Pictures\lovewallpaper\11.jpg")
# imgview = tk.Label(x,image = img)
# imgview.grid(row = 0,column = 2)
x.mainloop()
