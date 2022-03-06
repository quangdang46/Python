def CheckSNT(n):
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    return dem

def In(n):
    for i in range(2,n+1):
        if CheckSNT(i)==2:
            print(i,end=' ')

def main():
    print("Nhap n: ")
    n=int(input())
    In(n)
main()