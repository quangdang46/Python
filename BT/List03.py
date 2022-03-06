#List 03 Viết chương trình trả lời kết quả các phép tính
from math import sqrt
quest = ["2+ 5 + 7 =","5 * 10 =","sqrt(16) =","12%2 =","5//2="]
for i in quest:
    ans=int(input(i))
    dapan=eval(i.strip("="))
    if dapan==ans:
        print("Dung roi")
    else:
        print("Sai roi")