"""
'reated on 2020

@author: António Brito / Carlos Bragança

#objective:
Write a program that given three filenames reads the contents of the first two 
files and writes to the third file

Variables:
 fiche1 - Name of the first input file
 fiche2 - Name of the second input file
 fiche3 - Name of the output file
 line   - File lines
"""
#%%

#fiche1 = input('First filename:')
#fiche2 = input('Second filename:')
fiche3 = input('output filename:')

f1 = open("14_02A.txt","r")
f2 = open("14_02B.txt","r")
f3 = open(fiche3,"w")

for line in f1:
    f3.write(line.strip() + '\n')

for line in f2:
    f3.write(line.strip() + '\n')

f1.close()
f2.close()
f3.close()
