from tkinter import*
root=Tk()
root.title("Check Button")
root.iconbitmap("Icon.ico")
root.geometry('300x300')
root.resizable(0,0)
lbl=Label(root,text='',font='12',bg='red')
lbl.pack()
def dathang():
    x.get()
    if x.get()==0:
        lbl.config(text="Ban da chon nhan")
    elif x.get()==1:
        lbl.config(text="Ban da chon xoai")
    elif x.get()==2:
        lbl.config(text="Ban da chon cam")
    elif x.get()==3:
        lbl.config(text="Ban da chon buoi")
    else:
        pass
        
traicay=['nhan','xoai','cam','buoi']

x=IntVar()
for index in range(len(traicay)):
    radio=Radiobutton(root,text=traicay[index],font='12',value=index,variable=x,command=dathang)
    radio.pack()

root.mainloop()