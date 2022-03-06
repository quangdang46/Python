#Tinh thoi gian thuc hien chuong trinh
from time import *
a=int(input(print("Nhap gia tri n ")))
start=clock()
for i in range(1,a+1):
    print(i,end=' ')
print("Ket thuc chuong trinh")
end=clock()
print("Thoi gian thuc hien ct ",end-start)
