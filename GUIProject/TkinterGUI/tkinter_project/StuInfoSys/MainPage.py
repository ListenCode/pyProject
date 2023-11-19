import tkinter as tk
from views import AboutFrame, ModifyFrame, RecordFrame, QueryFrame, DeleteFrame


class MainPage:
    def __init__(self, master: tk.Tk = None):
        self.master = master
        self.master.title("Student Information System v.0.1")
        self.master.geometry("600x400")

        self.creatPage()

    def creatPage(self):
        self.about_frame = AboutFrame(self.master)
        self.modify_frame = ModifyFrame(self.master)
        self.record_frame = RecordFrame(self.master)
        self.query_frame = QueryFrame(self.master)
        self.delete_frame = DeleteFrame(self.master)

        # 菜单栏
        menubar = tk.Menu(self.master)
        menubar.add_command(label="Record", command=self.showRecord)
        menubar.add_command(label="Query", command=self.showQuery)
        menubar.add_command(label="Delete", command=self.showDelete)
        menubar.add_command(label="Modify", command=self.showModify)
        menubar.add_command(label="About", command=self.showAbout)
        # 将菜单栏绑定到父窗口
        self.master.config(menu=menubar)

    # 对一系列show函数代码重构
    # def showOnePage(self, pagename: str):
    #     pagenames = ["Record","Query","Delete","Modify","About"]
    #     for name in pagenames:
    #         if name == pagename:

    def showAbout(self):
        self.about_frame.pack()
        self.modify_frame.pack_forget()
        self.record_frame.pack_forget()
        self.query_frame.pack_forget()
        self.delete_frame.pack_forget()

    def showModify(self):
        self.modify_frame.pack()
        self.about_frame.pack_forget()
        self.record_frame.pack_forget()
        self.query_frame.pack_forget()
        self.delete_frame.pack_forget()

    def showRecord(self):
        self.record_frame.pack()
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.query_frame.pack_forget()
        self.delete_frame.pack_forget()

    def showQuery(self):
        self.query_frame.pack()
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.record_frame.pack_forget()
        self.delete_frame.pack_forget()

    def showDelete(self):
        self.delete_frame.pack()
        self.query_frame.pack_forget()
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.record_frame.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
