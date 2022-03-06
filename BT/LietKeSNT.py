def CheckSNT(n):
    check=0;
    for i in range(1,n+1):
        if n%i == 0:
            check+=1;
    return check

def InSNT(n):
    if CheckSNT(n)==2:
        print(n)

def main():
    for i in range(10000,11000):
        InSNT(i)
main()