"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%%
i = 1
while i <= 10:
    print(i)
    i = i + 1
print("End")

#%% ex mean of a list of n values
n = int(input("Number of values = "))
sumv = 0
i = 1
while i <= n:
    value = float(input("value="))
    sumv = sumv + value
    i = i + 1
mean = sumv / n
print("Mean = ", mean)