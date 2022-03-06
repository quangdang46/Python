#khoi tai list
from random import randrange
def CheckSNT(n):
    dem=0
    for i in range(1,n+1):
        if n>=2 and n%i==0:
            dem+=1
    return dem
print("Nhap so phan tu")
n=int(input())
str=[0]*n
for i in range(n):
    str[i]=randrange(-10,10)
print(str)
print("Them phan tu k: ")
k=int(input())
str.append(k)
print(str)
print("Kiem tra phan tu x xuat hien: ")
x=int(input())
print("So lan xuat hien" ,str.count(x))
print("*"*10)
tong=0
for pt in str:
    if CheckSNT(pt)==2:
        print(pt,end=' ')
        tong+=pt
print()
print("Tong cac so nguyen to: ",tong)
print("*"*10)
print('Mang dao nguoc \n')
str.sort(reverse=True)
print(str)
print("*"*10)
print('Mang sai khi sap xep \n')
str.sort()
print(str)
print("In mang dao nguoc \n")
str.reverse()
print(str)
print("*"*10)
print("Xoa list ")
del str[2:4]
print(str)
del str[:]
print(str)
