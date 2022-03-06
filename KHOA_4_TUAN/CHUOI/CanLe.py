'''
name.rjust(10,"* ") can trai 10 neu con thieu thi in dau *
name.ljust(3,"@") can phai 3 neu con thieu thi in dau @
Neu can be hon chuoi goc thi khong co gi thay doi
name,center(10) can giua cong them ' ' de cho o giua
name.center(10,"*") can giu va cong them * de can giua
'''
name="TRan"
print(name.upper().rjust(10,"@"))
print(name.upper().ljust(10,"*"))
print(name.upper().center(10))#can giua dung khoang trang de can
print(name.upper().center(10,"+"))#can giua dung + de can
print(name.upper().ljust(3,"+"))#Can khong du ne giu nguyen
#Do dai chuoi
print(len(name))
print(name.__len__())