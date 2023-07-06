"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective: Consider two sequential access files each having a list of values 
            stored. Write a program that builds a third sequential access file
            containing the average of the pair of values in the same line of 
            the two files. If the two files do not have the same number of 
            lines the missing values should be considered zero. 
            (Note: you should not use arrays)
"""
#%% 

def avg_files(file1, file2, file3):
    
    f1 = open(file1,"r")
    f2 = open(file2,"r")
    f3 = open(file3,"w")
    
    line1 = f1.readline()
    line2 = f2.readline()
    while line1 != '' and line2 != '':
        media = (float(line1) + float(line2)) / 2
        f3.write(str(media) + '\n')
        line1 = f1.readline()
        line2 = f2.readline()
    
    while line1 != '':
        f3.write(str(float(line1) / 2))
        line1 = f1.readline()

    while line2 != '':
        f3.write(str(float(line2) / 2))
        line2 = f2.readline()
    
    f1.close()
    f2.close()
    f3.close()
    
avg_files('14_03A.txt','14_03B.txt','14_03C.txt')    

