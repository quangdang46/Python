'''
x=input("Nhap chuoi: ")
y=input("Nhap chuoi: ")
for i in x,y:
    print(i.upper())
'''
line=[]
while True:
    x=input()
    if x:
        line.append(x.upper())
    else:
        break
for element in line:
    print(element)