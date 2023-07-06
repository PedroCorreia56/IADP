"""
Created on 2021

@author: António Brito / Carlos Bragança
"""
#%%
fh = open('test.txt', 'w')
for i in range(5):
    fh.write(f'line{i}\n')
fh.close()
#%%
fh = open('test.txt', 'r')
lines = fh.read()
print(lines)
fh.close()
#%%
fh = open('test.txt', 'r')
line = fh.readline().strip()
while line != "":
    print(line)
    line = fh.readline().strip()
fh.close()
#%%
fh = open('test.txt', 'r')
lines = list(map(str.strip, fh.readlines()))
print(lines)
fh.close()
#%%
names = ['antonio', 'joana', 'carlos']
ages = [25,34,45]
phones = [123123,1341234,345345]
fh = open('test.csv', 'w')
for i in range(len(names)):
    fh.write(f'{names[i]};{ages[i]};{phones[i]}\n')
fh.close()
#%%
names = []
ages = []
phones = []
fh = open('test.csv1', 'r')
line = fh.readline()
while line != "":
    f = line.strip().split(';')
    names.append(f[0])
    ages.append(int(f[1]))
    phones.append(int(f[2]))
    line = fh.readline()
print(names)
print(ages)
print(phones)
fh.close()


# %%
