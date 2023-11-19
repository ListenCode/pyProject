"""
event事件对象
1.在根窗口左键单击
2.在画布中拖拽
"""

import tkinter as tk


def mouse_test(event):
    print(f"鼠标左键单击位置(相对于父窗口)：({event.x},{event.y})")
    print(f"鼠标左键单击位置(相对于屏幕窗口)：({event.x_root},{event.y_root})")
    print(f"事件绑定的组件：{event.widget}")


def testDrag(event):
    """在画布中拖拽"""
    canvas.create_line(event.x, event.y, event.x + 1, event.y + 1)


root = tk.Tk()
root.geometry("500x300")
root.title("Event test")

canvas = tk.Canvas(root, width=200, height=100, bg="green")
canvas.pack()

root.bind("<Button-1>", mouse_test)
canvas.bind("<B1-Motion>", testDrag)

root.mainloop()
