print("CHUONG TRINH GIAI PT BAC 2")
a=float(input("nhap gia tri a: "))
b=float(input("nhap gia tri b: "))
c=float(input("nhap gia tri c: "))
print("-"*15)
e=b**2-4*a*c
if e<0:
    print("pt vo nghiem")
if e>=0:
    import math
    d=math.sqrt(e)
    if d>0:
        x1=float((-b+d)/(2*a))
        x2=float((-b-d)/(2*a))
        print("nghiem thu nhat la:",x1)
        print("nghiem thu nhat la:",x2)
    if d==0:
        x3=float(-b/(2*a))
        print("pt co nghiem duy nhat la:",x3)

