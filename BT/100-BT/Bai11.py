items=[]
x=input("Nhap chuoi: ")
for i in x.strip(",").split(","):
    items.append(i)
items.sort()
print(",".join(items))

