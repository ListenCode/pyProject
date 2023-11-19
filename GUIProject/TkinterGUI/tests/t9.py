import tkinter as tk
import tkinter.filedialog


def ask():
    filename = tkinter.filedialog.askopenfilenames()
    f = tk.filedialog.askopenfile()
    print(filename)
    label["text"] = filename


root = tk.Tk()

button = tk.Button(text="openfile",command=ask)
button.pack()
label = tk.Label(width=30,height=20,bg="green")
label.pack()

root.mainloop()

