# %%
import pandas as pd
df=pd.read_csv('gym2_q1.csv',sep=';', parse_dates=['date'])

#df_gym.pivot_table(index='city',columns='status',values='name',aggfunc='count').count()
#print(round(df.groupby('class')['age'].agg(['min','max','mean']),2))

#print(pd.DataFrame(df_gym.groupby('class')['age'].mean().round(2)).rename(columns={'age':'avg_age'}))
#print(df_gym.groupby('class').agg(age=('age','mean')).round(2).rename(columns={'age':'avg age'}))

df['month'] = df['date'].apply(lambda x: x.month)
df1=df.groupby('month')[['name']].count()
df1.rename(columns={'name':'clients'},inplace=True)
#print(df1)

pt=df.pivot_table(index='city', columns='rank', values='name', aggfunc='count')
r = pt.max().idxmax()
c = pt[r].idxmax()
print(pt)
print(c)
#print(f'rank: {r} city: {c}')




# %%
import pandas as pd
df = pd.read_csv('gym_q1.csv', sep = ";", index_col = 'id', parse_dates = ['date'])
filename = 'gym_cols_q1.csv'

def solve(df, filename):
    df2=pd.read_csv(filename, sep = ";", index_col = 'id')
    return pd.merge(df,df2, on='id', how='left')

df = solve(df, filename)
print(df.shape)
print(df.head(3))

print("[3 rows x", df.shape[1], "columns]")



def solve():
    print(df[df['date'] > pd.Timestamp('2014-12-31')].pivot_table(index='status',columns='sex',values='name',aggfunc='count'))


# %%

import pandas as pd
df = pd.read_csv('gym2_q1.csv', sep = ";", index_col = 'id', parse_dates = ['date'])
def solve():
    df1=df.groupby('city')
    print(df1)


solve()

# %%
