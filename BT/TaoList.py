#List 01: Viết chương trình tạo ra 1 list có n phần tử, # các phần tử là số ngẫu nhiên từ (1,100)
from random import randrange
n=int(input("Nhap phan tu: "))
list=[0]*n
for i in range(n):
    list[i] = randrange(1,100)

print(list)