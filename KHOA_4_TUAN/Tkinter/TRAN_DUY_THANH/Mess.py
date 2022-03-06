from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Hoc Mess")
root.resizable(height=True,width=True)
root.minsize(height=300,width=300)
messagebox.showwarning("Waring","Ghi chu")
messagebox.showerror("Error","Ghi chu")
messagebox.showinfo("Info","Ghi chu")
#showwaring canh bao dau !
#showerror bao loi dau X
#showinfo hien ra dau canh bao chu y

root.mainloop()