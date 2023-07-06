"""
Created on  2022

@author: António Brito / Carlos Bragança

#objective: 
    Determine the greatest common divisor (GCD) of two integers.
"""

value1 = int(input ('Value1 = '))
value2 = int(input ('value2 = '))
for gdc in range(min(value1,value2), 0, -1):
    if value1 % gdc == 0 and value2 % gdc == 0:
        break
print ('the greatest common divisor of',value1, 'and', value2, 'is', gdc)