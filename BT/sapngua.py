from random import randint
may1=randint(0,1)
may2=randint(0,1)
may3=randint(0,1)
#MAY1
if may1==0:
    may1="SAP"
    print("May1: ",may1)
if may1==1:
    may1="NGUA"
    print("May1: ",may1)
#MAY2
if may2==0:
    may2="SAP"
    print("May1: ",may2)
if may2==1:
    may2="NGUA"
    print("May2: ",may2)
#MAY1
if may3==0:
    may3="SAP"
    print("May3: ",may3)
if may3==1:
    may3="NGUA"
    print("May3: ",may3)
print("KET QUA LA")
#HOA
if may1=="SAP" and may2=="SAP" and may3=="SAP":
    print("HOA")
if may1=="NGUA" and may2=="NGUA" and may3=="NGUA":
    print("HOA")
#May1 thang
if may1=="SAP" and may2=="NGUA" and may3=="NGUA":
    print("May1 win")
if may1=="NGUA" and may2=="SAP" and may3=="SAP":
    print("May1 win")
#May2 thang
if may2=="SAP" and may1=="NGUA" and may3=="NGUA":
    print("May2 win")
if may2=="NGUA" and may1=="SAP" and may3=="SAP":
    print("May2 win")
#May3 thang
if may3=="SAP" and may2=="NGUA" and may1=="NGUA":
    print("May3 win")
if may3=="NGUA" and may2=="SAP" and may1=="SAP":
    print("May3 win")
print("-"*15)
