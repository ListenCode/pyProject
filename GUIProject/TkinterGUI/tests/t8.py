"""
lamabda表达式在事件传参command的应用.
原本command只接受函数对象，
使用command后可以接受函数对象的参数


"""

import tkinter as tk


def show(msg):
    print(f"You have input: {msg}")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()


button = tk.Button(root,text="Click",command=lambda :show(entry.get()))
button.pack()

root.mainloop()