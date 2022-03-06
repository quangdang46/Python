"""
ex2: cho
dict_01 = {
    "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
    "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
    "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
    "V":4,"W":4,"X":8,"Y":4,"Z":10}
#1: Tách số và chữ , hiển thị lên màn hình
#2: tính tổng các số
#3 chuyển đổi chuỗi : "University of Technology and Education" sang số

"""
from sympy import symbols

dict_01 = {
    "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
    "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
    "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
    "V":4,"W":4,"X":8,"Y":4,"Z":10}
chu=[]
so=[]
for i in dict_01:
    chu.append(i)
    so.append(str(dict_01[i]))
#chuyen list thanh chuoi chi dung cho kieu du lieu str
a=" ".join(chu)
b=" ".join(so)
print("Cac ki tu: ",a)
print("Cac so: ",b)
sum=0
for key in dict_01:
    sum+=dict_01[key]
print("Tong :",sum)
str="University of Technology and Education"
print(str)
str1=str.upper()
for i in range(len(str1)):
    if str[i]!=" ":
        print(dict_01[str1[i]],end="")
    else:
        print(" ",end="")
print("\n")
print("_"*10)
chuoimoi=""
print(chuoimoi)
y=diff(f,a,b)