from random import randrange
matrix =[
            [100, 14, 8, 22, 71],
            [ 0, 243, 68, 1, 30],
            [ 90, 21, 7, 67, 112],
            [115, 200, 70, 150, 8]
    ]
print (matrix)
for row in matrix: # duyệt từng dòng
    for elem in row: # Lấy từng phần tử trên mỗi dòng
        print ('{:>4}'.format(elem), end='')
    print ()

arr2D = []
rowsize = 5
columnsize = 3
for i in range(rowsize):
    onerow = []
    for j in range(columnsize):
        onerow.append(randrange(-100, 100))
    arr2D.append(onerow)

for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j], end='\t')
    print()
for row in arr2D:
    for column in row:
        print(column, end='\t')
print()