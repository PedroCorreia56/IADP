""" n1=int(input("Number of elements in first list = "))
l1=[]

for i in range(n1):
    l1.append(int(input(f'l1[{i}]=')))


n2=int(input("Number of elements in second list = "))
l2=[]*n2
for i in range(n2):
    l2.append(int(input(f'l2[{i}]=')))
 """
"""
Pergunta 1
l3=[]
for i in range(n1):
    for k in range(n2):
        if l1[i]==l2[k]:
            if l1[i] not in l3:
                l3.append(l1[i])

"""

""" 
Pergunta 2
l3=[]
for i in range(n1):
    if l1[i] not in l2:
        l3.append(l1[i])
 """

n=int(input("Number of elements in the list = "))
l=[]

for i in range(n):
    l.append(int(input(f'l[{i}]=')))

l.sort()
l.reverse()
lfinal=[]
great=int(input("Number of greatest elements = "))

for i in range(great):
    lfinal.append(l[i])
print(lfinal)

