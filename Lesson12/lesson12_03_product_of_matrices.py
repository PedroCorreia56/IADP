"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
  Compute the product of two matrices with dimensions NxM e MxP. 
"""
#%% option 1
n1 = int(input('Number of rows of the first matrix [a] = '))
m1 = int(input('Number of columns of the first matrix [a] = '))

n2 = m1
m2 = int(input('Number of columns of the second matrix [b] = '))
a = [[0] * m1 for i in range(n1)]
for i in range(n1):
    for j in range(m1):
            a[i][j] = float(input(f'a[{i},{j}]='))

b = [[0] * m2 for i in range(n2)]
for i in range(n2):
    for j in range(m2):
            b[i][j] = float(input(f'b[{i},{j}]='))

c = [[0] * m2 for i in range(n1)]

for i in range(n1):
    for j in range(m2):
        s = 0
        for k in range(m1):
            s = s +  a[i][k] * b[k][j]
        c[i][j] = s

for i in range(n1):
    print(c[i])