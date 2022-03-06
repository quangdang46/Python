'''
Bài 02:
Câu hỏi:
Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in
thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết
quả đầu ra phải là 40320.
Gợi ý:
 Trong trường hợp dữ liệu đầu vào được cung cấp, bạn hãy chọn cách để người
dùng nhập số vào
'''
def GiaiThua(n):
    if n==0:
        return 1
    dem=1;
    for i in range(1,n+1):
        dem*=i;
    return dem
print("Nhap gia tri n:")
n=int(input())
print(GiaiThua(n))