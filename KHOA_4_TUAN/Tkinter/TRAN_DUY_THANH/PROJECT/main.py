from tkinter import*
from DocGhi import *
root=Tk()
root.title("Quan Ly Sach")
root.geometry('400x400')
# root.config(bg='white')
root.iconbitmap('Logo.ico')
list_ma=[]
list_ten=[]
list_nam=[]
list_main=[]
def Clear():
    list.delete(0,END)
def display():
    x=str(htma.get())
    y=str(htten.get())
    z=htnam.get()
    LuuFile("ma.txt",x)
    LuuFile("ten.txt",y)
    LuuFile("nam.txt",z)
    list_ma.append(x)
    list_ten.append(y)
    list_nam.append(z)
    display_data=x+';'+y+';'+z
    LuuFile("data.txt",display_data)
    t=x+'{'+y+'}'+z
    # list.delete(0,END)
    list_main.append(t)
    list.insert(0,t)
    htma.delete(0,END)
    htten.delete(0,END)
    htnam.delete(0,END)
    print(list_main)
def Find():
    htma.delete(0,END)
    htten.delete(0,END)
    htnam.delete(0,END)
    x=str(htma.get())
    list_main1=GhiFile('data.txt')
    for i in range(len(list_main1)):
        if x==list_ma[i]:
            Clear()
            list.insert(0,list_main[i])
            break
        else:
            Clear()
            list.insert(0,'Khong tim thay')
            break

def XuatDanhSach():
    list.delete(0,END)
    dulieu=GhiFile('data.txt')
    print(dulieu)
    for items in dulieu:
        list.insert(END,items)
def SapXep():
    array=GhiFile('data.txt')
    for i in range(len(array)):
        for j in range(len(array)):
            a=array[i]
            b=array[j]
            if a[2]>b[2]:
                array[i]=b
                array[j]=a
    Clear()
    for line in array:
        list.insert(0,line)

lb1=Label(root,text='QUAN LI SACH',fg='blue',font=('Arian 20'))
lb1.place(x=100,y=6)
list=Listbox(root,width=65,bd=3)
list.place(y=55)
ma=Label(root,text='Ma',fg='black')
ma.place(y=230)
ten=Label(root,text='Ten',fg='black')
ten.place(y=250)
xuatban=Label(root,text='Nam xuat ban',fg='black')
xuatban.place(y=270)
htma=Entry(root,width=40)
htma.place(x=100,y=230)
htten=Entry(root,width=40)
htten.place(x=100,y=250)
htnam=Entry(root,width=40)
htnam.place(x=100,y=270)
chucnang=Frame(root)
them=Button(chucnang,text='Them',padx=10,command=display).pack(side="left")
tim=Button(chucnang,text='Tim',padx=10,command=Find).pack(side="left")
sapxep=Button(chucnang,text='Sap xep',padx=10,command=SapXep).pack(side="left")
thoat=Button(chucnang,text='Thoat',padx=10,command=chucnang.quit).pack(side="left")
chucnang.place(x=100,y=290)
congcu=Frame(root)
xuat=Button(congcu,text='Xuat Danh Sach',bg='blue',command=XuatDanhSach).pack(side="left",fill=X)
clear=Button(congcu,text='Clear',bg='red',padx=10,command=Clear).pack(side="left",fill=X)
congcu.place(x=140,y=317)
root.mainloop()
