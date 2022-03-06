from tkinter import*
from tkinter import messagebox
root=Tk()

root.title("Check Button")
root.iconbitmap("Icon.ico")
root.geometry('300x300')
root.resizable(0,0)
lbl=Label(root,text='')
lbl.pack()
def Click():
    # msb=messagebox.showwarning('Waring','Day la warning!')
    # msb=messagebox.showinfo('Info','Day la Info!')
    # msb=messagebox.showerror('Error','Day la Error!')
    msb=messagebox.askokcancel('Mes','Moi ban chon')#tra ve 0,1
    # msb=messagebox.askquestion('Mes','Moi ban chon')#tra ve yes no
    # msb=messagebox.askretrycancel('Mes','Moi ban chon')#tra ve 0 1
    # msb=messagebox.askyesno('Mes','Moi ban chon')#tra ve 0 
    # msb=messagebox.askyesnocancel('Mes','Moi ban chon')#tra ve 0 1
    lbl.config(text=msb)
    if msb==1:
        lbl.config(text="Hahaha")
    else:
        lbl.config(text="GGGGGGGG")


btn=Button(root,text='Click',command=Click).pack()


root.mainloop()