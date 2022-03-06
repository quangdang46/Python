#kiem tra in hoa
def DemInHoa(s):
    dem=0
    for word in s:
        if word.islower():
            dem+=1
    return dem
#kiem tra in thuong
def DemInThuong(s):
    dem=0
    for word in s:
        if word.isupper():
            dem+=1
    return dem
#kiem tra so
def KiemTraSo(s):
    dem=0
    for word in s:
        if word.isdigit():
            dem+=1
    return dem
#dem khoang trang
def DemKhoangTrang(s):
    dem=0
    for word in s:
        if word==' ':
            dem+=1
    return dem
#dem ki tu dac biet
def DemKiTuDacBiet(s):
    dem=0
    for word in s:
        if word.isalnum()==False:
            dem+=1
    return dem-DemKhoangTrang(s)


def main():
    print("Nhap chuoi ki tu: ")
    s=input()
    print("So ki tu hoa ",DemInHoa(s))
    print("So ki tu thuong ",DemInThuong(s))
    print("So ki tu so ",KiemTraSo(s))
    print("So khoang trang ",DemKhoangTrang(s))
    print("So ki tu dac biet ",DemKiTuDacBiet(s))

main()
