from tkinter import*
root=Tk()
x=IntVar()
def display():
    if x.get()==0:
        root.config(bg='blue')
    else:
        root.config(bg='green')

root.title("Check Button")
root.iconbitmap("Icon.ico")
root.geometry('300x300')
root.resizable(0,0)
# x=IntVar()
check=Checkbutton(root,text="Check",font=('Arian 12'),bg='red',fg='black',onvalue=1,offvalue=0,variable=x,command=display)
check.pack()

root.mainloop()



