from XuLi import *
data=DocFile('csdl_so.txt')
for line in data:
    for element in line:
        print(element,end="\t")
    print()