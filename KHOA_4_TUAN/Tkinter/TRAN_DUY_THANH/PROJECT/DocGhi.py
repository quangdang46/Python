def LuuFile(path,data):
    file= open(path,'a', encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()


def GhiFile(path):
    danhsach=[]
    file= open(path,'r', encoding='utf-8')
    for line in file:
        arr=line.split(';')
        danhsach.append(arr)
    file.close()
    return danhsach

