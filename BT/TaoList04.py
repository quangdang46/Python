#List 04: Viết chương trình nhập vào 1 list
    #1 in ra có bao nhiêu số nhỏ hơn 5,
    #2 và in ra vị trí index các số đó
n=int(input("Nhap n: "))
list=[]
for i in range(n):
    x= int(input("Nhap phan tu: "))
    list.append(x)
b=[]
dem=0
for i in range(n):
    if list[i]<5:
        dem+=1
    b.append(i)
print("So phan tu <5:",dem)
