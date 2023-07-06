"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
    Calculate the maximum element of a matrix and its position (row, column)
"""
#%% option 1


n = int(input("Number of rows ="))
m = int(input("Number of columns ="))
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = float(input("a[" + str(i) + "][" + str(j) + "]="))   
for i in range(n):        
     print(a[i])
pos_lin = 0
pos_col = 0
max_val = a[pos_lin][pos_col]
for i in range(n):
    for j in range(m):
        if a[i][j] > max_val:
            max_val = a[i][j]
            pos_lin = i
            pos_col = j          
print ('the maximum =',max_val, 'in row', pos_lin,'column',pos_col)
