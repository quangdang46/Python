def LuuFile(path,data):
    file=open(path,'a', encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()