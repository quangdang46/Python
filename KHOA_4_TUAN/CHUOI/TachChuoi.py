s="sv007;Nguyễn Thị Tẹt;1/1/1999"
arr=s.split(';') #tách ra bởi dấu ;
for x in arr:
   print (x)


s="""Obama
   hahaha
    ali333"""
arr=s.splitlines()
for line in arr:
    print (line.strip(), "a->",line.count ("a"))
    #Hàm splitlines tách các dòng

s="""sv01;Nguyễn Thị Hạnh;1/1/1990
sv02;Trần văn phúc;2/2/1995
sv03;Hồ văn An;2/3/1998
sv04; Phạm thị Lành;4/4/1994"""
arrSV=s.splitlines ()
for line in arrSV:
   arrInfor=line.split(';')
   if len(arrInfor)==3:
       print(arrInfor)