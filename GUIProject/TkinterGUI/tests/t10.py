"""尝试Label使用方法"""


import tkinter as tk
from tkinter import messagebox


class  Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master=master)
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        # 创建菜单控件
        self.mainMenu = tk.Menu(master=self.master)
        self.fileMenu = tk.Menu(master=self.mainMenu,tearoff=0)
        self.editMenu = tk.Menu(master=self.mainMenu)
        self.helpMenu = tk.Menu(master=self.mainMenu)

        # 将子菜单加入主菜单
        self.mainMenu.add_cascade(label="File",menu=self.fileMenu)
        self.mainMenu.add_cascade(label="Edit",menu=self.editMenu)
        self.mainMenu.add_cascade(label="Help",menu=self.helpMenu)

        # 在文件操作中加入子操作
        self.fileMenu.add_cascade(label="New",accelerator="ctrl+N",command=self.test)
        self.fileMenu.add_cascade(label="Save",accelerator="ctrl+S",command=self.test)
        self.fileMenu.add_separator()    # 添加分割线
        self.fileMenu.add_cascade(label="Exit",accelerator="ctrl+E",command=self.test)

        self.master.bind("<Key>",self.test)

        # 将菜单显示在主窗口
        self.master["menu"] = self.mainMenu

        self.textPad = tk.Text(master=self.master,width=50,height=50,bg="yellow")
        self.pack()

        # 创建右键弹出菜单
        self.bounceMenu = tk.Menu(self.master,tearoff=0)
        self.bounceMenu.add_cascade(label="New",command=self.test)
        self.master.bind("<Button-3>",self.respond) # 绑定右键


    def test(self,event=None):
        print("Click")
        messagebox.showinfo(message="Cilck")

    def respond(self,event):
        self.bounceMenu.post(event.x_root,event.y_root)



root = tk.Tk()
root.title("Notebook")
root.geometry('500x300+200+300')

app =  Application(master=root)

root.mainloop()