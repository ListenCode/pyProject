"""
Entry：做一个简单的登录界面。
登录密码是：123
"""


import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.label1 = tk.Label(text="Account")
        self.label1.pack()
        var1 = tk.StringVar()
        var1.set("admin")
        self.entry1 = tk.Entry(textvariable=var1)
        self.entry1.pack()

        self.label2 = tk.Label(text="Password")
        self.label2.pack()
        var2 = tk.StringVar()
        self.entry2 = tk.Entry(textvariable=var2,show='*')
        self.entry2.pack()


        tk.Button(text="Login", command=self._login).pack()

    def _login(self):
        account = self.entry1.get()
        pwd = self.entry2.get()
        print("Account: "+account)
        print("Password:"+pwd)
        if account == "admin" and pwd =="123":
            messagebox.showinfo(title="Success", message=(self.entry1.get()+",Nice to meet you"))
        else:
            messagebox.showinfo(title="Fail", message="Sorry,your password is error")


root = tk.Tk()
root.title("TkinterGUI")
root.geometry('500x300+200+300')

app = Application(master=root)

root.mainloop()
