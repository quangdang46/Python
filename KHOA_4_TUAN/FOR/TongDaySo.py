x=int(input("Nhap so x: "))
n=int(input(print("Nhap gia tri n")))
s=0
for i in range(1,n+1):
    tu=x**i
    mau=1
    for j in range(1,n+1):
        mau*=j
    s+=tu/mau
print("Tong gia tri cua day so la: ",s)