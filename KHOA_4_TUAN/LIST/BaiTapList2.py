from random import randrange

print("Nhap gia tri n")
n=int(input())
str=[0]*n
for i in range(n):
    str[i]=randrange(-10,10)
print(str)
print('Nhap phan tu muon xoa k:')
k=int(input())
while str.count(k)>0:
    str.remove(k)
print(str)
print("*"*10)
def DoiXung(str):
    check=True
    for i in range(len(str)):
        if (str[i]!=str[len(str)-i-1]):
            check=False
            break
    return check
if DoiXung(str)==True:
    print("Mang khong doi xung")
else:
    print("Mang khong doi xung")
