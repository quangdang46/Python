from XuLi import *
data =DocFile('csdl_so.txt')
for line in data:
    for element in line:
        if int(element)<0:
            print(element,end="\t")
    print()