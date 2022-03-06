from tkinter import *
root =Tk()
root.title("Entry")
ent=Entry(root,fg='black',width=50,borderwidth=2)
ent.pack()
ent.insert(0,"NHap key: ")
#borderwidth la do dam cua duong vien
def In():
    lb=Label(root,text="Hello "+ent.get())
    lb.pack()
#ham get() dung de luu
bt=Button(root,text='Ok!',bg='Green',command=In).pack()
#ham command dung de thuc hien lenh
root.mainloop()