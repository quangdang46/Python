a=float(input("hay nhap canh thu nhat: "))
b=float(input("hay nhap canh thu hai "))
c=float(input("hay nhap canh thu ba "))
if a+b>c and a+c>b and a+c>b:
    if a==b==c:
        print("day la mot tam giac deu")
    elif a==b or b==c or c==a:
        print("day la tam giac can")
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
        print("day la tam giac vuong")
    else:
        print("day la mot tam giac khong dac biet")
else:
    print("day khong phai la mot tam giac")