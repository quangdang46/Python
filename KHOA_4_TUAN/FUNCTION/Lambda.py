def HamSo(f,x):
    return f(x)

def SoChan(x):
    return x%2==0
def SoNguyenTo(x):
    dem=0
    for i in range(1,x+1):
        if x%i==0:
            dem+=1
    return dem==2
kq1=HamSo(lambda x:x%2==0,4)
kq2=HamSo(SoChan,4)
print("Kq1=",kq1)
print("Kq2",kq2)
x=5
kq3=HamSo(lambda x:SoNguyenTo(x),x)
print("Kq3=",kq3)

kq4=HamSo(SoNguyenTo,x)
print("Kq4=",kq4)