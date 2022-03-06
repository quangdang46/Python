#Tong tu 1 den n Neu gap so 20 thi ngung
s=0
n=int(input(print("Nhap gia tri n:")))
for i in range(1,n+1,1):
    if i==20:
        break
    else:
        s+=i
print("Tong cua chuoi la:",s)