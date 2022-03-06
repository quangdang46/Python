n=int(input(print("Nhap chieu cao: ")))
for i in range(n):
    for j in range(n):
        if j==0 or j==i or j==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()