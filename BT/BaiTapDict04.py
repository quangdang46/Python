#ex4: viết chương trình tìm kiếm sách 
mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu",
"Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi",
"Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi",
"Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu",
"Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi",
"Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
def Title():
    title =input("Nhap key can tim: ")
    for dic in mybooks:
        if dic["Title"] == title:
            a=dic["Title"]
            b=dic["Author"]
            c=dic["Publisher"]
            d=dic["Price"]
            print("Title: ",a)
            print("Author: ",b)
            print("Publisher: ",c)
            print("Price: ",d)


def Author():
    author =input("Nhap key can tim: ")
    for dic in mybooks:
        if dic["Author"] == author:
            a=dic["Title"]
            b=dic["Author"]
            c=dic["Publisher"]
            d=dic["Price"]
            print("Title: ",a)
            print("Author: ",b)
            print("Publisher: ",c)
            print("Price: ",d)

def Publisher():
    publisher =input("Nhap key can tim: ")
    for dic in mybooks:
        if dic["Publisher"] == publisher:
            a=dic["Title"]
            b=dic["Author"]
            c=dic["Publisher"]
            d=dic["Price"]
            print("Title: ",a)
            print("Author: ",b)
            print("Publisher: ",c)
            print("Price: ",d)
            print("_"*50)





def main():
    print("""
Chon de tim kiem:
    1.Title
    2.Author
    3.Publisher    
    """)
    chon=int(input("chon (1,2,3):"))
    if chon==1:Title()
    elif chon==2:Author()
    elif chon==3:Publisher()
    else:print("Moi nhap lai!")
main()