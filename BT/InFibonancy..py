
#su dung de qui
def Fibonacci(n):
    if n==0 or n==1:
        return n;
    else:
        return Fibonacci(n-1) +Fibonacci(n-2)

#khong si dung de qui
def Fibonaccia(n):
    f0=0
    f1=1
    fn=1
    if n==0 or n==1:
        return n;
    else:
        for i in range(2,n):
            f0=f1
            f1=fn
            fn=fn+f1
        return fn

def main():
    print("Nhap so luong n: ")
    n=int(input())
    for i in range(1,n+1):
        print(Fibonaccia(i),end=' ')

main()