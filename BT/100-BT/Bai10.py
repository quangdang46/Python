x=int(input("Nhap so hang: "))
y=int(input("Nhap so cot: "))
matran=[]
for i in range(x):
    b=[]
    for j in range(y):
        b.append(i*j)
    matran.append(b)
print(matran)
