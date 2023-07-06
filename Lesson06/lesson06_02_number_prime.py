"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
 Determines whether a number is prime using the - for loop

# Variables:
value       -> Given value
i           -> Dividers
"""

value = int (input ('value = '))
lim = int(value/2) 
for i in range(2, lim+1):
    if value % i == 0:
        break

if i >= lim: # If there are no dividers other than 1 
     print (f"{value} is prime")
else:
     print (f"{value} is not prime")
     