#List 02: Viết chương trình nhập vào 1 danh sách list sau đó:
     # 1. tạo ra 1 list mới bình phương các phần từ
     #2.Xác định bao nhiêu phần tử lớn hơn 50
n=int(input("Nhap gia tri n:"))
a=[]
b=[]
for i in range(n):
    x=int(input("Nhap phan tu: "))
    a.append(x)

for i in a:
    b.append(i*i)

print(a)
print(b)
for number in b:
    if number>50:
        print(number,end=" ")