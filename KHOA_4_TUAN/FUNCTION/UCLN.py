'''
HAM TINH UCLN
'''
def UCLN(a,b):
    if a==0 or b==0:
        return a+b
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a;
'''
CACH 2
def UCLN(a,b):
#CHAY TU MIN VE 1 NEU CO 1 SO CA 2 DEU CHIA HET LA UCLN

    min=a if a<b else b
    for i in range(min,0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1
            
'''