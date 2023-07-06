"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%% Calculate the average os a list of n values - version 1
n = int(input("Number of values="))
l1 = []         # Define l1 as an empty list
for i in range(n):
    l1.append(float(input("Value=")))   # Appends the value to the end of the list
sumv = 0.0
for i in range(n):
    sumv += l1[i]
average = sumv / n
print("Average=",average)
#%% Calculate the average os a list of n values - version 2
n = int(input("Number of values="))
l1 = [0] * n        # Define l1 as an list of n zeros [0,0,0,...]
for i in range(n):
    l1[i] = float(input("Value="))
sumv = 0.0
for i in range(n):
    sumv += l1[i]
average = sumv / n
print("Average=",average)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    