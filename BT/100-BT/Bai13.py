list=[]
x=input("Nhap chuoi: ")
list.append(x.strip().split(' '))
list.sort()
print(" ".join(list))
