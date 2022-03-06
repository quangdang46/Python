
def XoaKiTu(s):
    s.strip()
    s1=''
    str=s.split(' ')
    for word in str:
        if len(word)!=0:
            s1=s1+word+" "
    return s1.strip()

def main():
    print("Nhap chuoi: ")
    s=input()
    print(XoaKiTu(s))

main()