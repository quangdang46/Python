'''
Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng 
chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. Với giá trị cố định của C là 
50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá 
trị của D được phân cách bằng dấu phẩy.
'''
'''
from math import sqrt
c=50
h=30
def q(d):
    return sqrt((2*c*d)/h)
list=[]
n=int(input('Nhap n: '))
for i in range(n):
    x=int(input("Nhap phan tu: "))
    list.append(x)
print(list)
dapan=[]
for i in list:
    dapan.append(q(i))
print(dapan)
'''
import math
c=50
h=30
value = []
items=[x for x in input("Nhập giá trị của d: ").split(',')]
for d in items:
 value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# Code by Quantrimang.com
print (','.join(value))

