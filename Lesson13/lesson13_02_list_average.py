"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
    Write a function that returns de average of a list of real values.
"""

#%%

def average(lista):
    return sum(lista) / len(lista)

n = int(input("Number of values="))
list1 = [0] * n
for i in range(n):
    list1[i] = float(input("Value="))
print (average(list1))

        

    
    
    


