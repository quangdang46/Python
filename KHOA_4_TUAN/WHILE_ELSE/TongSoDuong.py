#Tinh tong cac so duong
s=0
cout=0
while cout<5:
    val=int(input(print("Nhap gia tri val: ")))
    if(val<0):
        print(val,"la so am")
        break
    s+=val
    cout+=1
else:
    print("Gia tri trung binh la ",s/cout)