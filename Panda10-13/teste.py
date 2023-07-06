#%%
import pandas as pd
df=pd.read_csv('gym2_q1_nan.csv',sep=';',index_col='id',parse_dates=['date'])

#%%
# Calculate and print the mean age and fill the NaN values with 0 and print the mean age again
def solve():
    age1=df['age'].mean().round(2)
    print(age1)
    df['age']=df['age'].fillna(0)
    age2=df['age'].mean().round(2)
    print(age2)

solve()
# %%
# Print a numpy array with the number of rows that have no NaN values and the number of rows that have at least one NaN value
def solve():
    print(df.isna().any(axis=1).value_counts().to_numpy())

solve()
# %%

# Delete the rows that have all NaN values and print the number of rows and columns
def solve():
    rows=df.shape[0]
    cols=df.shape[1]
    print(f"({rows}, {cols})")
    df.dropna(how="any",inplace=True)
    df.dropna(axis=1,inplace=True)
    rows=df.shape[0]
    cols=df.shape[1]
    print(f"({rows}, {cols})")


solve()
# %%
# Convert the city name to uppercase. Print the first 3 rows of the dataframe
def solve():
    df['city']=df['city'].str.upper()
    print(df.head(3))
    
solve()
# %%

def get_rank(years):
    if years < 5:
        return 'fair'
    elif years < 10:
        return 'good'
    elif years < 15:
        return 'very good'
    else:
        return 'excellent'
# Create a new column called rank with the following values:
# Number of years of membership between:
# 0-5 years: fair
# 5-10 years: good
# 10-15 years: very good
# 15+ years: excellent
# Print the first 5 rows of the dataframe
def solve():
    #com ifs
    #df['rank'] = df['years'].apply(get_rank)
    #com cut
    df['rank'] = pd.cut(df['years'], [0, 5, 10, 15, 100], right=False, labels=['fair','good','very_good','excellent'])
    print(df.head(5))

solve()

# %%
# Change the rank name from old_cat to new_cat and convert the rank column to a category
def solve(old_cat, new_cat):
    df['rank']=df['rank'].astype('category')
    df['rank']=df['rank'].replace(old_cat,new_cat)

solve('fair','poor')
print(pd.unique(df['rank']))
# %%
# Convert column col_name to type col_type and print the dataframe dtypes
def solve(col_name,col_type):
    df[col_name]=df[col_name].astype(col_type)
    print(df.dtypes)

solve('height',float)
# %%
# Print the number of rows for each rank
def solve():
    print(df['rank'].value_counts())

solve()
# %%
# Count the number of occurrences of the last_name in the dataframe
def solve(last_name):
    names=df['name'].str.split(' ',expand=True)
    print("Number of occurrences of {}:".format(last_name),names[1].value_counts()[last_name])
    #or
    ct = df['name'].str.count(last_name).sum()
    print(f'Number of ocurrences of {last_name}: {ct}')
    return ct
    
solve('Martins')
# %%
# Given a name, print the number of days from registration to 1/1/2022
def solve(name):
    print((pd.Timestamp('1/1/2022') - df.loc[df['name']==name,'date']).to_string(header=False, index=False))

solve('Marisa Martins')
# %%
#Calculate and print the number of registratiosn per year (sorted in ascending order)
def solve():
    print(df['date'].dt.year.value_counts().sort_index())

solve()


# %%
def solve():
    print(df.shape)
    df.dropna(how='all', inplace=True)
    print(df.shape)

solve()
# %%
