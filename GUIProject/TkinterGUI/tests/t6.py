"""
Grid布局：计算器界面设计
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
        buttonText = (("MC", "M+", "M-", "MR"),
                      ("C", "±", "÷", "×"),
                      (7, 8, 9, "-"),
                      (4, 5, 6, "+"),
                      (1, 2, 3, "="),
                      (0, "."))
        tk.Entry(self).grid(row=0,column=0,columnspan=4,pady=10)
        for rindex,r in enumerate(buttonText):
            for cindex,c in enumerate(r):
                if c == "=":
                    tk.Button(self,width=2,text=c).grid(row=rindex+1,column=cindex,rowspan=2,sticky="nsew")
                elif c == 0:
                    tk.Button(self,width=2, text=c).grid(row=rindex + 1, column=cindex,columnspan=2,sticky="ew")
                elif c == ".":
                    tk.Button(self,width=2, text=c).grid(row=rindex + 1, column=cindex+1,sticky="ew")
                else:
                    tk.Button(self,width=2,text=c).grid(row=rindex+1,column=cindex,sticky="ew")



root = tk.Tk()
root.resizable(False,False)
root.title("TkinterGUI")
root.geometry('200x250+200+300')

app = Application(master=root)

root.mainloop()
