from tkinter import*
from windowcenter import *
root=Tk()
root.title("Bypass PUBG")
root.resizable(height=True,width=True)
root.minsize(height=100,width=400)
makecenter(root)
Label(root,text="Bypass vip pubg",fg='red').pack()
key=StringVar()
Entry(root,text="Key:",textvariable=key,width=300).pack()
Button(root,text="Enter",command=root.quit).pack()
root.mainloop()
