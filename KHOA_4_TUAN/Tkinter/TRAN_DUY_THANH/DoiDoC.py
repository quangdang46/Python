from tkinter import *
root=Tk()
def Chuyen():
    x=float(htnhietdo.get())
    y=(5/9)*(x-32)
    htdoc.delete(0,END)
    htdoc.insert(0,round(y,2))
root.title("Doi Do C")
root.iconbitmap('Icon.ico')
root.geometry('400x200')
root.config(bg='yellow')
nhietdo=Label(root,text='Nhap do F',font=('Arian 18'),fg='black')
nhietdo.place(y=20)
htnhietdo=Entry(root,width=20,bd=3)
htnhietdo.place(y=26,x=180)
chuyen=Button(root,text='Chuyen',font='8',bg='blue',command=Chuyen)
chuyen.place(y=60,x=200)
doc=Label(root,text='Do C',font=('Arian 18'),fg='black')
doc.place(y=100)
htdoc=Entry(root,width=20,bd=3)
htdoc.place(y=110,x=180)

root.mainloop()
