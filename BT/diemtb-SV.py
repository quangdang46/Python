diem=float(input("Hay nhap diem cua ban: "))
if diem<=10 and diem>=0:
    if diem>=9:
        print("Ban dat duoc loai: A")
    elif diem>=7 and diem<9:
        print("Ban dat duoc loai: B")
    elif diem>=5 and diem<7:
        print("Ban dat duoc loai: C")
    else:
        print("Diem cua ban dat duoc loai: D")
else:print("Ban hay kiem tra lai diem")
