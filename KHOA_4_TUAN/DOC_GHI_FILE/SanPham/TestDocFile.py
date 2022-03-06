from XuLiFile import *
dssp=DocFile('Datebase.txt')

def InSp(dssp):
    for row in dssp:
        for element in row:
            print(element,end='\t')
        print()

def main():
    InSp(dssp)

main()