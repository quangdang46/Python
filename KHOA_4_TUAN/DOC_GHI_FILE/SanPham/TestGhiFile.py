from XuLiFile import *
masp=input('Nhap ma san pham ')
tensp=input('Nhap ten san pham ')
dongia=float(input('Nhap gia san pham: '))
line=masp+';'+tensp+';'+str(dongia)
luuFile('Datebase.txt', line)