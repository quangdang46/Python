'''
a=5 b=7
nếu a khác b thì gán c 113 ngược lại c=115

'''
a=5
b=7
#cach thong thuong
'''
if(a!=b):
    c=113
else:
    c=115
print(c)

#cach khac
c = 113 if a!=b else 115
print(c)
'''
print("Nhap")
d=int(input())
if d%2==0:
    print("So chan")
else:
    print("So le")


print("Nhap so bat ki")
e=int(input())
print("Chan" if e%2==0 else "Le")