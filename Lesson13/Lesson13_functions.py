"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%% Factorial of n
def fact(n):
    f = 1
    for i in range(2,n+1):
        f = f * i
    return f

# Combinations of n, p at a time
def comb(n,p):
    cb = fact(n) / (fact(p) * fact(n - p))
    return cb

m = int(input("n="))
p = int(input("p="))

mf = fact(m)
print("Factorial =", mf)
c = comb(m, p)
print("Combinations =", c)