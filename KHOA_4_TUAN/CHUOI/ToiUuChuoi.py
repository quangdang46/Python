
def ToiUuChuoi(s):
    s=s.lower().strip()
    s1=""
    str=s.split(' ')
    for word in str:
        if(len(word)!=0):
            s1=s1+word+" "
    s1=s1.strip().title()
    return s1
def main():
    print("Nhap chuoi ")
    s=input()
    print(ToiUuChuoi(s))

main()
