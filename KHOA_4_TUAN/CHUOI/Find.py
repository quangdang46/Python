'''Hàm find trả về vị trí đầu tiên tìm thấy, hàm rfind trả về vị trí cuối cùng tìm thấy. Nếu
không thấy sẽ trả về -1'''
s="hello hello hello"
x1=s.find('o')#ham find() tra ve vi tri dau tien tim thay
print(x1)
x2=s.rfind ('o')#ham rfind() tra ve vi tri cuoi cung tim thay
print(x2)
x3=s.find('x')#neu khong tim thay tra ve -1
print(x3)
'''
Hàm count trả về số lần xuất hiện của Chuỗi con trong Chuỗi gốc, không tồn tại trả về 0
'''
s="Obama likes Putin, Putin likes Kim Jong Un"
c1=s.count("Putin")#ham cout tra ve so lan xuat hien chuoi con
print(c1)
c2=s.count("Trump")#neu khong ton tai tra ve 0
print(c2)
'''
ham name.count("x",y,z) tim kiem ki tu x tu vi tri y den z
'''
s="c:/music/bolero/doithong2mo.mp3"
p1=s.find('/')
p2=s.rfind ('/')
print("p1=",p1)
print ("p2=",p2)
c=s.count ("o")
print ("o xuất hiện=",c)
c=s.count ("o",16)
print ("o xuất hiện =",c,"từ vị trí thứ 16 của chuỗi gốc")
c=s.count ("o",16,20)
print("o xuất hiện =",c,"lần từ vị trí thứ 16->20 của chuỗi gốc")
