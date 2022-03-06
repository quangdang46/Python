from random import randint
nguoichoi=input("nhap cai ma ban muon: ")
may=randint(0,2)
if may==0:may="keo"
if may==1:may="bua"
if may==2:may="bao"
print("--------------------------------")
print("Ban chon: ",nguoichoi)
print("May chon: ",may)
if nguoichoi=="keo":
    if may=="keo":
        print("hoa")
    if may=="bua":
        print("thua")
    if may=="bao":
        print("thang")

if nguoichoi=="bua":
    if may=="keo":
        print("hoa")
    if may=="bua":
        print("thua")
    if may=="bao":
        print("thang")

if nguoichoi=="bao":
    if may=="keo":
        print("hoa")
    if may=="bua":
        print("thua")
    if may=="bao":
        print("thang")
print("chuc ban choi game vui ve")
