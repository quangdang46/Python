# dict1={"Ten1":"Le van hao","Ten 2":"Tran quang dang","Ten 3":"Nguyen quang tien"}
# # x=dict1.items()
# # print(x);
# del dict1[1]
# for key,val in dict1.items():
#     print(key)
#     print(val)
# def Cong(a,b,c=1):
#     return a + b + c
# x=Cong(1,2)
# print(x)
# def Cong(*data):
#     sum=0
#     for i in data:
#         sum+=i
#     return sum

# x=Cong(1,2,3,2,3,4,5)
# print(x)
# def Cong(*data):
#     x=[]
#     sum=0
#     for i in data:
#         for j in i:
#             sum+=j
#         x.append(sum)
#     return x
# z=Cong([1,2,3,4],[5,6,7,8])
# print(z)


# def Listphone(**data):
#     gia=0
#     for key,val in data.items():
#         gia+=val
#         print("{:10} {:10}".format(key,val));
#     print("-"*20)
#     print("{:10} {:10}".format("Gia",gia));
    

# Listphone(nokia=5000,iphone=10000,motorola=55000)

# def Cong(n1,n2,n3,*data,**data1):
#     t1=t2=t3=0
#     t1=n1+n2+n3
#     for i in data:
#         t2+=i
#     for k,v in data1.items():
#         t3+=v
#     x=[t1,t2,t3]
#     return x

# x=Cong(1,2,3,4,5,2,3,4,5,one=1,two=2,three=3,four=4)
# print(x)

# list1=[1,2,3,4,5,5]
# l=iter(list1)
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())

#Cover ham range
# def myrange(start,end,step=1):
#     i=0
#     while i<end:
#         yield i
#         i+=step

# for i in myrange(0,10,2):
#     print(i)

#Dem so ki tu khac nhau trong mot list
# def diffCharts(*data):
#     dic={}
#     for items in data:
#         for i in items:
#             i.upper()
#             if i in dic:
#                 dic[i]+=1
#             else:
#                 dic[i]=1
#     return dic

# print(diffCharts("hahahah","huhuhu","Python"))


def myrange(*thamso):
    start=end=step=0
    if len(thamso)==3:
        start=thamso[0]
        end=thamso[1]
        step=thamso[2]
    elif len(thamso)==2:
        start=thamso[0]
        end=thamso[1]
    else:
        end=thamso[1]
    i=start
    while i<end:
        yield i
        i+=step
print(list(myrange(0,6,2)))
