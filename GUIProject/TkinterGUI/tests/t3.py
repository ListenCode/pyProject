"""尝试Label使用方法"""


import tkinter as tk
from tkinter import messagebox


class  Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master=master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.label01 = tk.Label(text="Hello\nThis is a test of Label object!",width=40)
        self.label01.pack()
        global minionPhoto  # 把 minionPhoto 声明成全局变量。如果是局部变量，本方法执行完毕后，图像对象销毁，窗囗显示不出。
        minionPhoto = tk.PhotoImage(file="../img/Minion.gif")
        self.label_gif = tk.Label(image=minionPhoto)
        # self.label_gif.image = minionPhoto 或者采用此方法让图片显示
        self.label_gif.pack()


root = tk.Tk()
root.title("TkinterGUI")
root.geometry('500x300+200+300')

app =  Application(master=root)

root.mainloop()