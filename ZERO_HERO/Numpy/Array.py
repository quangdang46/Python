from audioop import add
import numpy as np
from random import randint
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# # x=np.array(lst)
# x=np.array(lst).reshape(2,7)
# print(x)
# print(x.shape)

# x=np.array(range(10)).reshape(2,5)
# print(x)
# print(type(x))

# x=np.array([1,2,3,4,5,6,7,8,9])
# y=x.reshape(9,1)
# print(y)

# x=np.zeros(10)
# x=np.ones(10)

# print(x)

# x=np.array(range(10)).reshape(2,5)
# print(x)
# # x=x+10
# # x=x**2
# # x-=x
# x=x.T
# print(x)


# x=np.array(range(20))
# print(x)
# a1=x[:10]
# a1=x[10:]
# a1=x[::2]
# a1[:]=100

# print(a1)
# print(x)

# x=np.array(range(10)).reshape(2,5)
# print(x)
# b=x.copy()
# print(b)



# A=np.array(range(25)).reshape(5,5)
'''
[[ 0  1  2  3  4] 
 [ 5  6  7  8  9] 
 [10 11 12 13 14] 
 [15 16 17 18 19] 
 [20 21 22 23 24]]
'''
# print(A[0][1])
# print(A[1:3])
# print(A[1:3,1:3])
#Giao theo chieu ngang va theo chieu doc
'''
[ 6  7] 
 [11 12]]
 '''
 #Lay nhieu hang khac nhau 1 luc
# print(A[[1,3,4]])

#Tong cua ma tran
# print(A.sum())

x=[]
y=[]
for i in range(10):
    x.append(randint(0,10))
    y.append(randint(0,10))
x=np.array(x)
y=np.array(y)


#Cong 2 ma tran
# z=np.add(x,y)


#So sanh cac phan tu tuong ung
# z=np.maximum(x,y)
# z=np.minimum(x,y)


#Lay can bac 2 tung phan tu
# z=np.sqrt(x)


#Lay binh phuong tung phan tu
# z=np.square(x)

#Chia tung phan tu 2 mang tuong ung
# z=np.divide(x,y)

#Lay phan tu mang 1 mu phan tu mang 2 tuong ung
# z=np.power(x,y)


# print(z)

z=np.array([1,1,1,1,2,2,3,2,10,9,4,2,1,10])
#Sap xep tang dan
# z.sort()
#Loc cac phan tu trung
z=np.unique(z)

#So sanh phan tu lon hon mang nay voi phan tu mang kia tra la true false
# z=np.greater(x,y)

#va || &&

#&&
# print(z)
# z=np.all(z)

#||
# print(z)
# z=np.any(z)

#So snah = nhau tra ve true false
# z=np.equal(x,y)
print(z)