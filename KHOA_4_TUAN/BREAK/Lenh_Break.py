while True:
    a=int(input(print("Nhap 1 so bat ki: ")))
    print(a,"So chan" if a%2==0 else "So le")
    x=input(print("Ban muon tiep tuc hay khong chon C/K:"))
    if x=="C" or x=="c":
        break;
print("Ket thuc vong lap")