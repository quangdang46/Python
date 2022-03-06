def LuuFile(path,data):
    file= open(path,'a', encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()

def DocFile(path):
    list= []
    file= open(path,'r', encoding='utf-8')
    for line in file:
        data=line.strip()
        str=data.split(',')
        list.append(str)
    file.close()
    return list
