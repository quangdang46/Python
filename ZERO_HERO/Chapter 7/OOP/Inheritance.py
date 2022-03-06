#Ke thua

# class ConNguoi:
#     def Info(self,name,tuoi):
#         print("Ten la ",name,"Tuoi" ,tuoi)


# class HocSinh(ConNguoi):
#     def __init__(self,lop,truong):
#         print("Lop ",lop,"Truong" ,truong)


# hs=HocSinh(9,"TDT")
# print(hs.Info("Tran quang dang",15))
# print(hs)



class ConNguoi:
    def Info(self,name,tuoi):
        self.name = name
        self.tuoi = tuoi
    #Chuyen ve class chinh

    def Test(self):
        print("Ten la: ",self.name)
        print("Tuoi: ",self.tuoi)


class Student(ConNguoi):
    def __init__(self,lop,truong,name,tuoi):
        #Mong muon ke thua Con nguoi
        # ConNguoi.__init__(self,name,tuoi)
        ConNguoi.Info(self,name,tuoi)
        self.lop = lop
        self.truong = truong
    
    def InfoClass(self):
        print("Lop ",self.lop,"truong ",self.truong)

hs=Student(9,"TDT","DANG",14)
hs.InfoClass()
hs.Test()