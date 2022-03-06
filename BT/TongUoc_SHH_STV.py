'''
Câu 4:Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
 * 4.1 : Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không?
(Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó. Vd: 6 có
 các ước số là 1,2,3 và 6=1+2+3 →6 là số hoàn thiện)
 4.2: Kiểm tra số nguyên dương n có phải là số thịnh vượng (Abundant number)hay
 không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó.
 Vd:12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6 →12 là số thịnh vượng)
'''
n=int(input(print("Nhap 1 so bat ki")))
def TongUoc(n):
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i;
    return tong
#4.1
def SoHoanThien(n):
    if TongUoc(n)==n:
        print(n,"La so hoan thien")
    else:
        print(n,"Khong la so hoan thien")


#4.2
def SoThinhVuong(n):
    if TongUoc(n)>n:
        print(n,"La so thinh vuong")
    else:
        print(n,"Khong la so thinh vuong")

SoHoanThien(n)
SoThinhVuong(n)