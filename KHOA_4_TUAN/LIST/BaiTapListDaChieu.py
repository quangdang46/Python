from random import randrange

print("Nhap so hang m: ")
m=int(input())
print('Nhap so cot n: ')
n=int(input())
list=[]
for i in range(m):
    arr=[]
    for i in range(n):
        arr.append(randrange(-10,10))
    list.append(arr)
print(list)
#xuat ma tran
for row in list:
    for j in row:
        print(j,end=' ')
    print()
print("Nhap so dong muon xuat: ")
k=int(input())
print(list[k])
print("Nhap so cot muon xuat: ")
y=int(input())
for i in range(m):
    print(list[i][k])
