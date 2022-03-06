def Tong(m,n=1,k=3):
    s=0
    for i in range(1,m+n+k):
       s+=i
    return  s
print(Tong(2))#Tuc la m=2
print(Tong(3,4))#Tuc la m=2,n=4
print(Tong(2,k=1))#Tuc la m=2 k=1

