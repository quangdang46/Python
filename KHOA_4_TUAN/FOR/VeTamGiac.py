n=int(input(print("Nhap chieu cao: ")))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or i==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''
dung while:
'''
print("_"*15)
i=0
while i<n:
    j=0
    while j<n:
        if j==0 or j==i or i==n-1:
            print("#",end='')
        else:
            print(" ",end='')
        j+=1
    i+=1
    print()