from random import randrange
x=randrange(1,10)
dem=0
while True:
    y=int(input("Nguoi nhap gia tri:"))
    dem+=1
    if x==y:
        print("Ban da nhap dung")
        print("So lan dem ",dem)
        a=input("Ban muon tiep tuc khong C/K")
        if a =="k" or k =="K":
            break
    if y>x:
        print("So may chon < So ban chon")
        print("So lan dem ",dem)
    else:
        print("So may chon > So ban chon")
        print("So lan dem ",dem)
    if dem==7:
        break
