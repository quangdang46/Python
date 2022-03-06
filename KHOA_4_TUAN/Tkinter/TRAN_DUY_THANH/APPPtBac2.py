from tkinter import *
from math import *
root=Tk()
def Tiep():
    hesoa.set("")
    hesob.set("")
    hesoc.set("")
    kq.set("")
def Giai():
    a=int(hesoa.get())
    b=int(hesob.get())
    c=int(hesoc.get())
    denta=b**2-4*a*c
    if denta<0:
        kq.set("Vo nghiem")
    elif denta==0:
        kq.set("Co nghiem duy nhat:"+str(-b/2*a))
    else:
        x1=(-b+sqrt(denta))/(2*a)
        x2=(-b-sqrt(denta))/(2*a)
        kq.set("x1="+str(x1)+"x2="+str(x2))
hesoa=StringVar()
hesob=StringVar()
hesoc=StringVar()
kq=StringVar()
root.title("PTB2")
root.geometry("300x200")
Label(root,text='GIAI PT BAC 2',fg='red',font=('Arian 18')).grid(row=0,columnspan=2)
Label(root,text='He so a').grid(row=1,column=0)
Label(root,text='He so b').grid(row=2,column=0)
Label(root,text='He so c').grid(row=3,column=0)
Entry(root,width=30,textvariable=hesoa).grid(row=1,column=1)
Entry(root,width=30,textvariable=hesob).grid(row=2,column=1)
Entry(root,width=30,textvariable=hesoc).grid(row=3,column=1)
nut=Frame(root)
Button(nut,text='Giai',bg='blue',command=Giai).pack(side="left")
Button(nut,text='Tiep',bg='blue',command=Tiep).pack(side="left")
Button(nut,text='Thoat',bg='blue',command=quit).pack(side="left")
nut.grid(row=4,columnspan=2)
Label(root,text='Ket qua').grid(row=5,column=0)
Entry(root,width=30,textvariable=kq).grid(row=5,column=1)
root.mainloop()