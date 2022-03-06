'''
ex1 : viết chương trình sử dụng dict chưa 10 user name và password.
Chương trình yêu cầu nhập vào username và pass,
1. nếu user name o có trong dict, chương trình báo user name o tồn tại
2. nếu user name đúng mà password sai thì báo : PASSWORD SAI
3. nếu user, pass đúng thì báo bạn đã login thành công
'''

dic={"user1":"123456",
"user2":"123456",
"user3":"123456",
"user4":"123456",
"user5":"123456",
"user6":"123456",
"user7":"123456",
"user8":"123456",
"user9":"123456",
"user10":"123456"}
user=input("Nhap tai khoan: ")
pas=input("Nhap mat khau: ")
if user not in dic:
    print("Khong ton tai!")
else:
    if(pas==dic[user]):
        print("Log in thanh cong")
    else:
        print("Pass sai!")

