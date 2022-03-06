#Grid Cot hang
from tkinter import*
root=Tk()
root.title("Hello")
lb1=Label(root,text='Helo mn',bg='red',font=('Arian 18'),fg='black')
lb2=Label(root,text='Helo mn',bg='blue',font=('Arian 18'),fg='black')
lb3=Label(root,text='         ',bg='brown',font=('Arian 18'),fg='black')
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=2)
lb3.grid(row=0,column=1)
root.mainloop()