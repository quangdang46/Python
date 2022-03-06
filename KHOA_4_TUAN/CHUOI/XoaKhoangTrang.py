#Ham strip() Xoa khoang trang hai ben
#Hoặc dùng để xóa kí tụ truyền vào name.strip('x) xóa kí tự x từ 2 bên nếu gặp kí tự khác thì dừng
a="  NAME   "
b="@@@@TEN@@@"
c="%% ##NAME%%%%"
a=a.strip()#XOA KHOANG TRANG
b=b.strip('@')#GAP % THI XOA
c=c.strip('%')#GAP # THÌ DỪNG LẠI KHONG XÓA ĐƯỢC NỮA
print(a)
print(b)
print(c)