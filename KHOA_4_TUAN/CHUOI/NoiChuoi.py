s="sv007;Nguyễn Thị Tęt;1/1/1990"
arr=s.split(';')
print(len(arr))
for x in arr:
   print (x)
s2="*"
#Noi chuoi theo ki tu nao
s2=s2.join(arr)
#ham name.join() dùng để nối chuỗi
print (s2)
a="Obama"
b=" Kim Un Un"
c=a+b
print (c)
