print("chung toi se giai cho ban phuong trinh Ax+B=0")
a=float(input("Hay nhap a: "))
b=float(input("Hay nhap b: "))
if a==0 and b==0:
    print("phuong trinh vo so nghiem")
if a==0 and b!=0:
    print("phuong trinh vo nghiem")
if a!=0 and b==0:
    print("phuong trinh co nghiem duy nhat la: x=0")
if a!=0 and b!=0:
    nghiem=-b/a
    print("nghiem pt la: x= ",nghiem)
print("------------------------------")
