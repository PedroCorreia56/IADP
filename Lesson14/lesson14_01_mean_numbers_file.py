"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
    Calculate the mean of a list of numbers in a text file.
"""
filename = input("Filename:")
fh = open(filename)
count = 0
sum_values = 0.0
for line in fh:
    value = float(line)
    sum_values += value
    count += 1
mean = sum_values / count    
print(f"Mean = {mean:0.2f}")
fh.close()