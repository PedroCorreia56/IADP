"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%% for / range examples
for i in range(1,6):            # 1,2,3,4,5
    print(i)
#%%
for i in range(1,6,2):          # 1,3,5
    print(i)
#%%
for i in range(6):              # 0,1,2,3,4,5
    print(i)
#%%
for i in range(6, 1, -1):       # 6,5,4,3,2,
    print(i)
#%% Check if a number is prime
n = int(input("Number="))
for i in range(2,int(n/2)):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("It is prime")
#%% Print the even numbers
for i in range(6):
    if i % 2 != 0:
        continue
    print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    