x,y=eval(input("Nhap Doanh thu-Chi phi: "))
def TinhRoi(x,y):
    return (x-y)/y
def DauTu(roi):
    print(roi)
    if roi>=0.75:
        print("Ban nen dau tu")
    else:
        print("Ban khong nen dau tu")

DauTu(TinhRoi(x,y))