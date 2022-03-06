#chuyen do tu co so 10 sang nhi phan
def ChuyenDoi(n):
    str =[]
    while n>0:
        last=n%10
        str.append(last)
    str=str.reverse()
    print(str)

def main():
    print("Nhap gia tri n:")
    n=int(input())
    print(ChuyenDoi(n))

main()
