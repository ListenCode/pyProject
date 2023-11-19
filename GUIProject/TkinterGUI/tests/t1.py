"""第一个窗口程序"""

import tkinter as tk

root = tk.Tk()

root.title('My Window')
root.geometry('500x300+200+100')


bt1 = tk.Button(root,text='Click')

bt1.pack()


root.mainloop()
