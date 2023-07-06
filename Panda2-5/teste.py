# %%

n=int(input())

fact=1
for i in range(n,0,-1):
    fact=fact*i

fact
# %%

l=input()

p=l.replace(":","").replace(" ","")
p
# %%
import pandas as pd
df = pd.read_csv('gym.csv',sep=';', parse_dates=['date'])

def solve():
    print(df.loc[df['age']>=55,'children'].sum())



solve()
# %%
import pandas as pd
df = pd.read_csv('gym.csv',sep=';', parse_dates=['date'])

def solve():
    print(df['age'].min())


solve()
# %%
import pandas as pd
df = pd.read_csv('gym.csv',sep=';', parse_dates=['date'])

def solve():
    avg=df['weight'].mean()
    print(df.loc[(df['weight']>avg*1.3) & (df['sex']=="M") ,['name','weight','age','children']])



solve()
# %%
import pandas as pd
df = pd.read_csv('gym.csv',sep=';', parse_dates=['date'])

def solve():
    print(df.loc[(df['height']<150) | (df['height']>177) ,['name','weight','children']])



solve()
# %%
import pandas as pd
df = pd.read_csv('gym.csv',sep=';', parse_dates=['date'])

def solve():
    print(df.loc[(df['id']%100==13) & (df['age']>=50) ,['id','name','weight','height','age']])



solve()
# %%
