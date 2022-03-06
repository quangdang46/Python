def NhapMang(n):
    list=[]
    for i in range(n):
        print("Nhap phan tu {}:".format(i))
        x=int(input())
        list.append(x)
    return list

def XuatMang(list):
    for number in list:
        print(number,end='\t')

def TinhTongLe(list):
    dem=0
    for number in list:
        if number%2==1:
            dem+=number
    print("\nTong cac phan tu le trong mang: ",dem)

def TongPhanTuViTriChan(list):
    dem=0
    for i in range(len(list)):
        if i%2==0:
            dem+=list[i]
    print("\nTong cac phan tu vi tri chan: ",dem)

def XoaPhanTuAm(list):
    for i in range(len(list)-1,-1,-1):
        if list[i]<0:
            list.remove(list[i])

def ViTriMax(list):
    #hoac dung ham max=max(list)
    max=list[0]
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
            a=i
    print("\nPhan tu co gia tri lon nhat la: {0}\nO vi tri {1}".format(max,a))


def DoiPhanTuAm(list):
    for i in range(len(list)):
        if list[i]<0:
            list.remove(list[i])
            list.insert(i,0)
def main():
    print("Nhap gia tri n: ")
    n=int(input())
    list=NhapMang(n)
    XuatMang(list)
    TinhTongLe(list)
    TongPhanTuViTriChan(list)
    XoaPhanTuAm(list)
    XuatMang(list)
    ViTriMax(list)
    DoiPhanTuAm(list)
    XuatMang(list)
main()