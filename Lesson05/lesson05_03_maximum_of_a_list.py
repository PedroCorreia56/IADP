"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective: 
    In a list of N values determine the maximum value and its position
    
# Variables:
    n           # Number of values in the list
    value       # Values in the list
    k           # List index
    maximum     # Maximum value
    pos_maximum # Position in the list of the maximum value
"""

n = int(input("Number of values in the list: "))

value = int(input("Value: "))  # Reads the first value in the list

# Set the maximum value to the first value in the list
maximum = value
pos_maximum = 1

# Loop through the list
k = 2
while k <= n:
    value = int(input("Value: "))
    if value > maximum:
        # updates the maximum value and its position
        maximum = value
        pos_maximum = k
    k = k + 1

print("Maximum =", maximum, "  position =", pos_maximum)
