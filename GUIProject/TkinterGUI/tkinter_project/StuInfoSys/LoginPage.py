import tkinter as tk
from tkinter import messagebox
from database import db
from MainPage import MainPage


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.creatWidget()

    def creatWidget(self):
        self.page = tk.Frame(master=self.master)
        self.page.pack()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.username.set("admin")
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text="Username:").grid(row=1, column=1)
        tk.Label(self.page, text="Password:").grid(row=2, column=1)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=2)

        tk.Button(self.page, text="Login", command=self.login).grid(row=3, column=1, pady=10)
        tk.Button(self.page, text="Exit", command=self.page.quit).grid(row=3, column=2, pady=10)

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        print(name, pwd)
        flag, msg = db.check_login(name, pwd)
        if flag:
            self.page.destroy()
            MainPage(self.master)
        else:
            messagebox.showwarning(title="Fail success", message=msg)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200+150+250")
    LoginPage(root)
    root.mainloop()
