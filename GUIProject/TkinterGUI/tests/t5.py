"""CheckButton"""

from tkinter import *
win = Tk()
win.title("C语言中文网")
win.geometry('500x200')
win.resizable(0,0)
lb = Label(text='C语言中文网答疑辅导班',font=('微软雅黑', 18,'bold'),fg='#CD7054')
lb.pack()

# 设置三个复选框控件，
check1 = Checkbutton(win, text="Python",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
check2 = Checkbutton(win, text="C语言",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
check3 = Checkbutton(win, text="Java",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
# 将第一个 复选框按钮的 variable值，设置为 onvalue =1 ，表示选中状态
check1.select ()
# 取消了第一个复选框的选中状态

check1.pack (side = LEFT)
check2.pack (side = LEFT)
check3.pack (side = LEFT)
# 显示窗口
win.mainloop()