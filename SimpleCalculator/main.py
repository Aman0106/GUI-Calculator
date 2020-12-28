import tkinter

_list = []

root = tkinter.Tk()

label = tkinter.Label(root, text="This is the label")
label2 = tkinter.Label(root, text="2nd label")
label3 = tkinter.Label(root, text="3rd label")

label.pack()
label2.pack()
label3.pack()

root.mainloop()
