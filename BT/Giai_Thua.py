def GiaiThuaK(n):
    s=1
    for i in range(1,n+1):
        s*=i
    print(s)

def main():
    print("Nhap gia tri n: ")
    n=int(input())
    if n>=0:
        print(GiaiThuaK(n))
main()