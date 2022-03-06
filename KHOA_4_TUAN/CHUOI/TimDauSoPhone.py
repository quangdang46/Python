#Bai 1 cho 1 list sdt tim dau so
#Bai 2 cho 1 list sdt xuat danh sach dau so

def TimDauSo(dauso):
    str=["18001115","0948476636","0909701814","0916912902","0918495041","0913114267","0902411627","0935090491"]
    for phone in str:
        if phone.startswith(dauso):
            print("Da tim thay")
    return "Khong tim thay"
print("Nhap dau so can tim")
dauso=input()
TimDauSo(dauso)

#BAI 2
def TimDauSo(dauso):
    str=["18001115","0948476636","0909701814","0916912902","0918495041","0913114267","0902411627","0935090491"]
    Fphone=[]
    for phone in str:
        if phone.startswith(dauso):
            Fphone.append(phone)
    return Fphone
print("Nhap dau so can tim")
dauso=input()
Fphone=TimDauSo(dauso)
print(Fphone)
