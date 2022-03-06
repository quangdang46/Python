#Hàm reverse() dùng để đảo ngược list thay đổi bản chất list nếu k muốn thay đổi dùng hàm for
a=[1,2,3,4,5,6]
#a.reverse()
for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')
