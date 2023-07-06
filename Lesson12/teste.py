""" 
Pergunta 3
n = int(input())
a = [[0] * n for i in range(n)]

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        a[i][j] = float(input())  

for i in a:
    print(i) """

""" n=int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        num=float(input())
        if j>0:
            if a[i][j-1]<num:
                temp=a[i][j-1]
                a[i][j-1]=num
                a[i][j] = temp
            else:
                a[i][j]=num
        else:
            a[i][j]=num


for i in a:
    print(i) """

""" 
Problema1
n=int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = float(input())

c=0

for i in range(n):
    maxvalue=a[i][0]
    for j in range(n):
        if maxvalue<a[j][i]:
            maxvalue=a[j][i]
            c=j
    if a[i][i]!=a[c][i]:
        for m in range(n):
            temp=a[i][m]
            a[i][m]=a[c][m]
            a[c][m]=temp

for i in a:
    print(i) """

n=int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = float(input())


minvalue=9999999999999999999999
minL=0
minC=0
maxvalue=-99999999999999999999
maxL=0
maxC=0

for i in range(n):
    for j in range(n):
        if minvalue>a[i][j]:
            minvalue=a[i][j]
            minL=i
            minC=j
        if maxvalue<a[i][j]:
            maxvalue=a[i][j]
            maxL=i
            maxC=j

temp=a[minL][minC]
a[minL][minC]=a[maxL][maxC]
a[maxL][maxC]=temp


for i in a:
    print(i) 