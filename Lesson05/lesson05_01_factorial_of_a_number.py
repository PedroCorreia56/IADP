"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective: 
    Calculate the factorial of a positive integer
    
# Variables:
     n -> Value given
     n_factorial -> Factorial of the given value
"""

n = int (input ("Value:"))
n_factorial = 1

# Factorial N calculation cycle
while n > 1:
     n_factorial = n_factorial * n
     n = n - 1

print ("Factorial =", n_factorial)