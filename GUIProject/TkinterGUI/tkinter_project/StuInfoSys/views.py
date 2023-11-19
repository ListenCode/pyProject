import tkinter as tk
from tkinter import ttk
from database import db

class AboutFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)

        tk.Label(self, text="This work is created by tkinter").pack()
        tk.Label(self, text="Author: LiSheng").pack()
        tk.Label(self, text="Contact: ******").pack()


class ModifyFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()

        self.creatWidget()

    def creatWidget(self):
        tk.Label(self).grid(row=0,column=0,pady=10)

        tk.Label(self,text="Name").grid(row=1,column=1,pady=5)
        tk.Entry(self,textvariable=self.name).grid(row=1,column=2)

        tk.Label(self,text="Chinese").grid(row=2,column=1,pady=5)
        tk.Entry(self,textvariable=self.chinese).grid(row=2,column=2)

        tk.Label(self,text="Math").grid(row=3,column=1,pady=5)
        tk.Entry(self,textvariable=self.math).grid(row=3,column=2)

        tk.Label(self,text="English").grid(row=4,column=1,pady=5)
        tk.Entry(self,textvariable=self.english).grid(row=4,column=2)

        tk.Button(self,text="Search",width=10,command=self.searchInfo).grid(row=5,column=1,pady=10)
        tk.Button(self, text="Modify", width=10, command=self.modifyInfo).grid(row=5, column=2, pady=10)
        tk.Label(self,textvariable=self.status).grid(row=6,column=2,sticky=tk.E)

    def searchInfo(self):
        flag, info = db.search_by_name(self.name.get())
        if flag:
            self.name.set(info["name"])
            self.chinese.set(info["chinese"])
            self.math.set(info["math"])
            self.english.set(info["english"])
            self.status.set("Data query success")
        else:
            self.status.set(info)

    def modifyInfo(self):
        stu = {"name":self.name.get(),"chinese":self.chinese.get(),
               "math":self.math.get(),"english":self.english.get()}
        print("Modify:",stu)
        db.modify(stu)

        # 录入数据后将录入界面输入框清空
        self.status.set("Update success!")
        self.name.set('')
        self.chinese.set('')
        self.math.set('')
        self.english.set('')



class RecordFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()

        self.creatWidget()

    def creatWidget(self):
        tk.Label(self).grid(row=0,column=0,pady=10)

        tk.Label(self,text="Name").grid(row=1,column=1,pady=5)
        tk.Entry(self,textvariable=self.name).grid(row=1,column=2)

        tk.Label(self,text="Chinese").grid(row=2,column=1,pady=5)
        tk.Entry(self,textvariable=self.chinese).grid(row=2,column=2)

        tk.Label(self,text="Math").grid(row=3,column=1,pady=5)
        tk.Entry(self,textvariable=self.math).grid(row=3,column=2)

        tk.Label(self,text="English").grid(row=4,column=1,pady=5)
        tk.Entry(self,textvariable=self.english).grid(row=4,column=2)

        tk.Button(self,text="Record",width=10,command=self.recordInfo).grid(row=5,column=2,pady=10)
        tk.Label(self,textvariable=self.status).grid(row=6,column=2,sticky=tk.E)

    def recordInfo(self):
        stu = {"name":self.name.get(),"chinese":self.chinese.get(),
               "math":self.math.get(),"english":self.english.get()}
        print("Record:",stu)
        db.insert(stu)

        # 录入数据后将录入界面输入框清空
        self.status.set("Record success!")
        self.name.set('')
        self.chinese.set('')
        self.math.set('')
        self.english.set('')



class QueryFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.creatWidget()
        self.showDataFrame()

    def creatWidget(self):
        columns = ["name", "chinese", "math", "english"]
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        self.tree_view.column("name", width=80, anchor='center')
        self.tree_view.column("chinese", width=80, anchor='center')
        self.tree_view.column("math", width=80, anchor='center')
        self.tree_view.column("english", width=80, anchor='center')

        self.tree_view.heading("name", text="name")
        self.tree_view.heading("chinese", text="chinese")
        self.tree_view.heading("math", text="math")
        self.tree_view.heading("english", text="english")

        self.tree_view.pack(fill=tk.BOTH, expand=True)

        tk.Button(self,text="Refresh Data",command=self.showDataFrame).pack(anchor=tk.E,pady=5)

    def showDataFrame(self):
        # 删除旧的阶段，更新数据时用到
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass

        students = db.all()
        for i, stu in enumerate(students):
            # print(i+1,stu)
            self.tree_view.insert(parent='',index=i+1,values=
            (stu["name"],stu["chinese"],stu["math"],stu["english"]))


class DeleteFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.creatWidget()


    def creatWidget(self):
        self.name = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self,text="Input deteled name:").pack()
        tk.Entry(self,textvariable=self.name).pack()
        tk.Button(self,text="Delete",command=self.deleteInfo).pack()
        tk.Label(self,textvariable=self.status).pack()

    def deleteInfo(self):
        flag,msg = db.delete_by_name(self.name.get())
        print("Want to delete:",self.name.get())
        print(flag,msg)
        self.status.set(msg)
        self.name.set('')


