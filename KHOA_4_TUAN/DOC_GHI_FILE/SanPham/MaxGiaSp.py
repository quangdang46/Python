from XuLiFile import *
dssp=DocFile('Datebase.txt')
def MaxSp(dssp):
    max=dssp[0][2]
    for i in range(len(dssp)):
        if dssp[i][2]>max:
            max=dssp[i][2]
            a=dssp.index(dssp[i])
    print("Gia cao nhat la:\n",dssp[a])

'''
def Sort(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp))
            a=dssp[i]
            b=dssp[j]
            if a[2]>b[2]:
                dssp[i]=b
                dssp[j]=a
'''
MaxSp(dssp)
