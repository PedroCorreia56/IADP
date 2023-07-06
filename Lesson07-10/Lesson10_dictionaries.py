"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
#%% Update the stock of products stored in a dictionary 
stock = {'p1':35,'p2':12,'p3':25,'p4':20}

n = int(input("Number of movements="))

for i in range(n):
    prod = input("Product=")
    quant = int(input("Quantity="))
    stock[prod] = stock[prod] + quant

print(stock)

#%% Access to the dictionary keys (products)
stock = {'p1':35,'p2':12,'p3':25,'p4':20}
for prod in stock:
    print(prod)
#%% Access to the dictionary values (products stock)
stock = {'p1':35,'p2':12,'p3':25,'p4':20}
for prod in stock:
    print(stock[prod])
#%% Access to the dictionary values (products stock)
stock = {'p1':35,'p2':12,'p3':25,'p4':20}
for value in stock.values():
    print(value)
#%% Access to the dictionary key, values (products, products stock)
stock = {'p1':35,'p2':12,'p3':25,'p4':20}
for prod,st in stock.items():
    print(prod, st)