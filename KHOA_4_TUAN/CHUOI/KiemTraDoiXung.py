def KiemTraDoiXung(s):
    check=True
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            check=False
    return check


def main():
    print("Nhap chuoi can kiem tra: ")
    s=input()
    if KiemTraDoiXung(s):
        print("Chuoi doi xung")
    else:
        print("Chuoi khong doi xung")


main()