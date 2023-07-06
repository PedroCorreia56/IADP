#%%
import numpy as np
file=input("Filename:")
info=np.genfromtxt(file, delimiter=";")

cmax=0
lmax=0
cmin=0
lmin=0
k=0
for i in range(info.shape[0]):
    for j in range(info.shape[1]):
        if k==info.argmin():
            cmin=j
            lmin=i
        if k==info.argmax():
            cmax=j
            lmax=i
        k+=1
    
print("Max: {}, ({},{})".format(info.max(),lmax,cmax))
print("Min: {}, ({},{})".format(info.min(),lmin,cmin))




# %%
import numpy as np

nr=int(input("Number of elements:"))

a=[]
b=[]
for i in range(nr):
    a.append(float(input("a[{}]:".format(i))))

for i in range(nr):
    b.append(float(input("b[{}]:".format(i))))

array1=np.array(a)
array2=np.array(b)
print("Scalar product = {}".format(array1 @ array2))







# %%
import numpy as np
info=input()
helper=info
read=helper.replace(" ",",").split(",")
size=len(read)
for i in range(size):
    info=info+" "+input()


info=info.replace(" ",",").split(",")

a=np.zeros((size,size),dtype=int)
b=np.zeros(size,dtype=int)

i=0
for k in range(size):
    for j in range(size):
        a[k][j]=info[i]
        i+=1

for k in range(size):
    b[k]=info[i]
    i+=1

c=np.linalg.solve(a, b)
print("solution:")
print(c)
# %%
