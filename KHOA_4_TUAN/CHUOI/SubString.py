x = "Hello World!"
print(x[2:]) #"llo World!" từ vị trí 2 đến hết chuỗi
print(x[6:2]) #"He" từ vị trí 6 đén vị trí 2-1
print(x[:-2]) #"Hello Worl" từ đầu đến vị trí -2-1
print(x[-2:]) #"d!" từ vi trí -2 đén hết
print(x[2:-2])#"llo Worl" từ vi trí 2 đến vị trí -2-1
print(x[6:11])#"World" từ vị trí 6 đến vị trí 11

s="d:/tailieu/python/lamchupython.pdf"
p=s.rfind('/')
print(s[p+1:1])
p2=s.rfind ('.')
print(s[p+1:p2])
'''
x[a:b] tu vi tri a den vi tri b-1
'''