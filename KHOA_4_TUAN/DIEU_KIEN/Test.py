print("CHUONG TRINH GIAI PHUONG TRINH BAC 2")
a=int(input(print("Moi ban nhap gia tri a: ")))
b=int(input(print("moi ban nhap gia tri b: ")))
if(a==0 and b==0):
    print("Phuong trinh vo so nghiem")
if(a==0 and b!=0):
    print("Phuong trinh vo nghiem")
if(a!=0 and b!=0):
    print("Phuong trinh co nghiem duy nhat ",-b/a)