from matmul import  readfile,matmul

A = readfile('A.csv')
b = readfile('B.csv')

print(matmul(A,b))

