# class Car:
#     tocdo=250
#     nhienlieu="Xang"

# xea=Car()
# print(xea.tocdo)
# class Car:
#     tocdo=250
#     nhienlieu="Xang"
#     def PhuongThuc(self):
#         print("Xe chạy với vận tốc: ",self.tocdo)

# xea=Car()
# print(xea.PhuongThuc())

class Car:
    tocdo=250
    nhienlieu="Xang"
    def PhuongThuc(self,tocdo):
        print("Xe chạy với vận tốc: ",tocdo)

xea=Car()
print(xea.PhuongThuc(10000))