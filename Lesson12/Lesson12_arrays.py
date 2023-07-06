"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%% Scalar prduct of two vectors
n = int(input("Number of elements = "))
a = [0] * n
b = [0] * n
for i in range(n):
    a[i] = float(input(f"a[{i}]="))
for i in range(n):
    b[i] = float(input(f"b[{i}]="))
scalarprod = 0
for i in range(n):
    scalarprod = scalarprod + a[i] * b[i]
print("Scalar product =", scalarprod)

#%% Sum of two matrices (nxm)
n = int(input("Number of rows ="))
m = int(input("Number of columns ="))
a = [[0] * m for i in range(n)]
b = [[0] * m for i in range(n)]
c = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = float(input(f"a[{i}][{j}]="))
for i in range(n):
    for j in range(m):
        b[i][j] = float(input(f"b[{i}][{j}]="))
for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]
for i in range(n):
    print(c[i])