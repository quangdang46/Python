#Tao mang 2 chieu va xuat mang cot hang
from random import randrange

def XuatMang(D):
    for row in D:
        for element in row:
            print(element,end="\t")
        print()

def XuatDong(D):
    print("Nhap so dong can lay ra: ")
    k=int(input())
    for element in D[k]:
        print(element,end="\t")    


def TaoMang(m,n):
    D=[]
    for i in range(m):
        sort=[]
        for j in range(n):
            sort.append(randrange(-10,10))
        D.append(sort)
    return D

def XuatCot(D):
    print("\nNhap so cot can lay ra: ")
    k=int(input())
    for row in D:
        print(row[k],end="\t")


def MaxMang(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j]>max:
                max=D[i][j]
    
    print("\nGia tri lon nhat cua mang ",max)
def main():
    print("Nhap so dong: ")
    m=int(input())
    print("Nhap so cot: ")
    n=int(input())
    D=TaoMang(m,n)
    XuatMang(D)
    XuatDong(D)
    XuatCot(D)
    MaxMang(D)
main()