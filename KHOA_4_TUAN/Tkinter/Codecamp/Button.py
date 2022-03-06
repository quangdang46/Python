from tkinter import *
root=Tk()
root.title('Button')
MyButton=Button(root,text='Click Me!',state=DISABLED).pack()
#ham DISABLED tat nut bam di,Vo hieu hoa nut bam
'''
ipadx, ipady: Nó đại diện cho số lượng pixel cho đường viền của gidget.
padx, pady: Nó đại diện cho số lượng pixel bên ngoài đường viền của gidget.
'''
def In():
    lb=Label(root,text='XIn chao')
    lb.pack()
Bt1=Button(root,text='Haha',command=In).pack()
root.mainloop()