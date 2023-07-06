"""
Created on  2022

@author: António Brito / Carlos Bragança

#objective: 
    Given a list of N values calculate the arithmetic mean.

      # Variables:
          n -> number of values in the list
          value -> values in the list
          k -> list index
          sumvalues -> Sum of the values in the list
          mean -> arithmetic mean of the values in the list
"""

n = int (input ("Number of values in the list:"))
sumvalues = 0.0     # Initializes the sumValues variable

# Loop to sum the list of values
k = 1
while k <= n:
     value = float(input ("Value:"))
     sumvalues = sumvalues + value
     k = k + 1

mean = sumvalues / n        # Calculates the arithmetic mean

print ("Arithmetic mean =", mean)