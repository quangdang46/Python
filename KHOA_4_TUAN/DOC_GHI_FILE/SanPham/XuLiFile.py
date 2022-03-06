'''
Viết chương trình nhập vào thông tin của một sản phẩm:
Mã: Chuỗi
Tên: Chuỗi
Đơn Giá: Số
Mỗi một Sản phẩm sau khi nhập thành công sẽ lưu nối đuôi vào File theo quy tắc:
MSSP;Tên Sản phẩm; Đơn giá
1) xuất danh sách sản phẩm từ File
2) Sắp xếp Sản phẩm theo đơn giá giảm dần
'''
def luuFile(path,data):
    file = open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def DocFile(path):
    arrProduct=[]
    file = open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        arr=data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct



        
