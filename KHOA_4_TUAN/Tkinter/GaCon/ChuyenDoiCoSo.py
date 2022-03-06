from tkinter import*
from tkinter import messagebox
root=Tk()
input=StringVar()
def Contract():
    root.geometry('360x200')
def Expand():
    root.geometry('400x400')
def BackSpace():
    a=ent.get()
    a=a[:-1]
    input.set(a)
def Chuyen():
    x=ent.get()
    try:


        if int(x)>0:
            valhex=hex(int(x)) 
            hex.config(text=str(valhex))

            valbin=bin(int(x))
            bin.config(text=str(valbin))

            valoct=oct(int(x))
            oct.config(text=str(valoct))


        else:
            msb=messagebox.showwarning('Error','Moi ban nhap so duong!')   
    except:
        msb=messagebox.showwarning('Error','Moi ban nhap so duong!')





root.title("Chuyen Doi Co So")
root.iconbitmap('Icon.ico')
root.geometry('360x200')
display_Hex=Label(root,text='Hex')
display_Hex.place(x=10,y=15)
hex=Label(root,text='')
hex.place(x=50,y=15)
display_Oct=Label(root,text='Oct')
display_Oct.place(x=10,y=40)
oct=Label(root,text='')
oct.place(x=50,y=40)
display_Bin=Label(root,text='Bin')
display_Bin.place(x=10,y=65)
bin=Label(root,text='')
bin.place(x=50,y=65)
ent=Entry(root,width=56,bg='white',fg='black',textvariable=input)
ent.place(x=10,y=90)
dis_Frame=Frame(root)
dis_Convert=Button(dis_Frame,text='Convert',padx=15,command=Chuyen).pack(side="left",fill=Y)
dis_Back=Button(dis_Frame,text='BackSpace',padx=15,command=BackSpace).pack(side="left",fill=Y)
dis_Expand=Button(dis_Frame,text='Expand',padx=15,command=Expand).pack(side="left",fill=Y)
dis_Contract=Button(dis_Frame,text='Contract',padx=15,command=Contract).pack(side="left",fill=Y)
dis_Frame.place(x=10,y=115)
root.mainloop()