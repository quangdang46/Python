#KIỂM TRA SỐ NGUYÊN TỐ VÀ HỎI NGƯỜI DÙNG CÓ TIẾP TỤC HAY KHÔNG
while True:
    n=int(input(print("Nhap mot so bat ki: ")))
    check=1
    for i in range(2,n):
        if n%i==0:
            check=0
            break
    if check==1:
        print(n,"La so nguyen to")
    else:
        print(n,"Khong la so nguyen to")
    x=input(print("Ban co muon tiep tuc khong C/K:"))
    if x=='k' or x=="K":
        break
print("BYE")