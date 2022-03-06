'''
Python hỗ trợ hàm name.remove(ten phan tu),khong ton tai phan tu ==>ERROR, xóa phần tử đầu tiên trong List
hoac del st[0]
del st[x:y] xoa tu pt thu x den pt thu y-1
'''
st=[2,2,0,1,8,0]
st.remove(2)
print(st)
print("*"*20)
st=[2,0,1,8,0]
del st[0]
print(st)