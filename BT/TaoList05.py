#List 05: Viết chương trình in số lớn thứ 2 và số nhỏ thứ 2 trong list
    # 2: in ra vị trí index số đó
   #ví dụ list
    #lst=[1,2,3,4,5]
    # số lớn thít 2: 4 , vị trí index trong list là 3
    # số nhỏ thứ 2 trong list là 2, vị tri index trong list là 1
lst=[1,2,3,4,5]
max=max(lst)
for i in range(len(lst)):
    if(lst[i]<max):
        a=i
        b=lst[i]
print("So lon thu 2:{0} o vi tri:{1}".format(b,a))