from tkinter import *
from tkinter import messagebox
root=Tk()
def Click():
    messagebox.showinfo("Key","Moi ban nhap key")
root.resizable(height=True,width=True)
label1=Label(root,text="Helo cac ban",font=("Arial",14,"underline","bold"),bg='red',fg='black')
label1.pack()

button1=Button(root,text="Nhan vao day",bg='black',fg='green',command=Click)
button1.pack()
root.mainloop()