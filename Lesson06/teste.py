
n=int(input("N:"))
c = 2
for i in range(1000,0,-1):
    flag=0
    for i in range(2,c):
        if c%i==0:
            break
    else:  
        print(c)
        flag=1  
        n-=1
    if flag==0:
        i+=1
    c+=1  





"""
PErgunta 2
sumvalues = 0.0
for i in range(n):
    value = float(input ("value {}:".format(i+1)))
    sumvalues = sumvalues + value

mean = sumvalues / n

print("Arithmetic mean = %.2f" %mean)
 """
"""
Pergunta 3
for i in range(1,11):
    print("{} x {} = {}".format(n,i,n*i))"""