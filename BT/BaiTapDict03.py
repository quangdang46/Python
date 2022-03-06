"""
Cho data 1 cửa hàng, dữ liệu kiểu như sau :
d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]

#1. Tìm tất cả user có số điện thoại kết thúc bằng 8
#2: tìm tất cả user o có địa chỉ email
"""

d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]
dienthoai=[]
for dic in d:
    phone = dic["phone"]
    if phone[-1]=="8":
        print(dic["name"])
        print(dic["phone"])
        print(dic["email"])

    
