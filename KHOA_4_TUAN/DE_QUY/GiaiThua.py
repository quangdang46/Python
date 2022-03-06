def GiaiThua(n):
    if n==0:
        return 1
    else:
        return n*GiaiThua(n-1)
print(GiaiThua(6))