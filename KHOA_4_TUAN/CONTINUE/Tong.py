#Tinh tong cac so tu 1 den n bo 2 so 3 va 11
n=int(input(print("Nhap gia tri n")))
s=0
for i in range(1,n+1,1):
    if i==3 or i==11:
        continue
    s+=i
print('Tong cua day la',s)