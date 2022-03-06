#Nhap vao ngay thang nam tim ngay tiep theo
a=int(input(print("Nhap ngay:")))
b=int(input(print("Nhap thang: ")))
c=int(input(print("Nhap nam: ")))
if b!=2:
    if b in (4,6,9,11):
        if a>=1 and a<30:
            print("Ngay {0} thang {1} nam {2}".format(a+1,b,c))
        else:
            print("Ngay {0} thang {1} nam {2}".format(1,b+1, c))
    if b in (1,3,5,7,8,10,12):
        if b!=12:
            if a>=1 and a<=31:
                print("Ngay {0} thang {1} nam {2}".format(a + 1, b, c))
            else:
                print("Ngay {0} thang {1} nam {2}".format(1,b+1, c))
        else:
            print("Ngay {0} thang {1} nam {2}".format(1,1, c+1))
else:
    if a!=29:
        print("Ngay {0} thang {1} nam {2}".format(a+1, b , c))
    else:
        print("Ngay {0} thang {1} nam {2}".format(1, b + 1, c))

