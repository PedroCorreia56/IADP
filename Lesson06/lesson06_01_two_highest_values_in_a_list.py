"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:

In a list of N values ​​determine the two elements of higher value. Assume that these values ​​are distinct.

# Variables:
n       Number of values ​​in the list
value   Values ​​in the list
k       Loop index
max1    Maximum value
max2    Second Maximum value
"""

n = int(input('Number of values = '))
'''
Reads the first two values ​​in the list and set max1 equal to the greater of the two 
and max2 equal to the smaller of the two values
'''
value = int(input('Value = '))
max1 = value
value = int(input('Value = '))
if value> max1:
    max2 = max1
    max1 = value
else:
    max2 = value
# Loop through the list
for k in range(3, n+1):
    value = int(input('Value = '))
    if value > max1:
        # If value is higher than the current maximum then 
        # the current maximum becomes the second largest and 
        # the new value becomes the maximum
        max2 = max1
        max1 = value
    elif value > max2:
        # If value is greater than the second largest value
        # the new value becomes the second largest
        max2 = value
print ("Highest value =", max1, "2nd. Highest value =", max2)