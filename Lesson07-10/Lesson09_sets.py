"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%%
s1 = {1,2,3}
for value in s1:
    print(value)
    
#%% How many distinct element has a list
l1 = [1,2,3,1,1,4,5]
s1 = set(l1)
print("Number of distinct elements=",len(s1))