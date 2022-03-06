n=int(input(print("Nhap gia tri n:")))
def Fibonancy(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonancy(n-1)+Fibonancy(n-2)
#Xuat day Fibonancy tu 1 den n
def XuatDay(n):
    for i in range(1,n+1):
        print(Fibonancy(i),end=' ')

XuatDay(n)