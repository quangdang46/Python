a=6
'''
Chu y neu ket thuc KiemTra() thi gia tri a khong thay doi gia tri a chi thay doi trong ham def
Neu muon thay doi gia tri a thi can them global
'''
def KiemTra():
    global a
    a=a-1
KiemTra()
print(a)