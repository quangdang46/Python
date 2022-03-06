'''
Viết chương trình tính tổng của các chữ số của môt số nguyên n trong Python. 
Số nguyên dương n được nhập từ bàn phím. Với n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10
'''
def TongCacChuSo(n):
    tong=0
    while n>0:
        last=n%10
        tong+=+last
        n//=10
    return tong

def main():
    print("Nhap gia tri n:")
    n=int(input())
    print(TongCacChuSo(n))
main()
'''
""""
 * Tính tổng của các chữ số của một số nguyên dương n
 *
 * @param n: số nguyên dương
 * @return
"""
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));
'''
