"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
   Given a matrix calculate the transpose matrix.
"""

#%% option 1

n = int(input("Number of rows ="))
m = int(input("Number of columns ="))
a = [[0] * m for i in range(n)]
b = [[0] * n for i in range(m)]
for i in range(n):
    for j in range(m):
        a[i][j] = float(input("a[" + str(i) + "][" + str(j) + "]="))  
for i in range(n):
    for j in range(m):
        b[j][i] = a[i][j]
for i in range(n):
    print(a[i])
print("Matrix transpose:")
for i in range(m):
    print(b[i])
    
#%% Option 2 Square matrix whithout using a second matrix

n = int(input("Number of rows ="))
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = float(input("a[" + str(i) + "][" + str(j) + "]="))
        
for i in range(n):
    for j in range(i):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp
        
for i in range(n):
    print(a[i])