'''
Viết chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố trong Python. N là số nguyên dương được nhập từ bàn phím.
'''

def CheckSNT(n):
    check =0
    for i in range(1,n+1):
        if n%i == 0:
            check +=1
    return check

def Fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return Fibonacci(n-1) +Fibonacci(n-2)

def InSNT(n):
    for i in range(1,n+1):
        if CheckSNT(Fibonacci(i))==2:
            print(i,end=' ')

def main():
    print("Nhap gia tri n:")
    n=int(input())
    for i in range(1, n + 1):
        print(Fibonacci(i),end=' ')
    print()
    print("*"*20)
    InSNT(n)

main()
