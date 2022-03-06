from math import pow
x,y=eval(input("Nhap chieu cao can nang "))
def TinhChiSo(x,y):
    return y/pow(x,2)

def PhanLoai(bmi):
    print("Phan Loai-Nguy Co")
    if bmi<18.5:
        print("Gay-Thap")
    elif bmi<=24.9:
        print("Binh thuong-Trung Binh")
    elif bmi<=29.9:
        print("Hoi Beo-Cao")
    elif bmi<=34.9:
        print("Beo Phi Cap 1-Cao")
    elif bmi<=39.9:
        print("Beo Phi Cap 2-Rat Cao")
    else:
        print("Beo phi cap 3-Nguy Hiem")
PhanLoai(TinhChiSo(x,y))