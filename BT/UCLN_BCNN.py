def Tim(a,b):
    if a>=0 and b>=0:
        if a==0 or b==0:
            return a+b
        else:
            bc=a*b
            while a!=b:
                if a>b:
                    a=a-b
                else:
                    b=b-a
            print("UCLN",a)
            print("BCNN",bc/a)
    else:
        print("Khong ton tai!")
def main():
    a=int(input(print("Nhap a: ")))
    b=int(input(print("Nhap b: ")))
    Tim(a,b)
main()
'''
"""
 * Tìm ước số chung lớn nhất (USCLN)
 *
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return USCLN của a và b
"""
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
 
"""
 * Tìm bội số chung nhỏ nhất (BSCNN)
 * 
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return BSCNN của a và b
"""
def bscnn(a, b):
    return int((a * b) / uscln(a, b));
 
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
#tính BSCNN của a và b
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));

'''