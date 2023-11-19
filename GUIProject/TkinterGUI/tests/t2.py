"""尝试一个经典的 TkinterGUI 程序的写法，使用面向对象的方式"""

import tkinter as tk
from tkinter import messagebox


class  Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master=master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.bt1 = tk.Button(text='Welcome', command=self.bt1_message)
        self.bt1.pack()

    def bt1_message(self):
        messagebox.showinfo('Welcome', 'Nice to meet you')

root = tk.Tk()
root.title("GUI程序(面向对象方法创建)")
root.geometry('500x300+200+300')

app = Application(master=root)

root.mainloop()