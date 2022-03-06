'''
Viết một chương trình tính giai thừa của một số nguyên dương n.
Với n được nhập từ bàn phím. Ví dụ, n = 8 thì kết quả đầu ra phải là 1*2*3*4*5*6*7*8 = 40320.
'''
def GiaiThua(n):
    dem=1
    for i in range(1,n+1):
        print(i,"*",end='')
        dem*=i
    print("= ",dem)
def main():
    print("Nhap gia tri n: ")
    n=int(input())
    GiaiThua(n)
main()
