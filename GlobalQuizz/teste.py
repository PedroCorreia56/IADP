#%%
import pandas as pd
df=pd.read_csv('supermarket1.csv',sep=';')

#%%
# Replace the space in column names with underscore
def solve():
    df.columns = df.columns.str.replace(' ', '_')
    print(df)
    

solve()
# %%
# Calculate the total number of units(Quantity) sold by 'Product line' and 
def solve():
    print(df.pivot_table(index='Product line',values='Quantity',aggfunc='sum',margins=True))
    

solve()
#
# %%
# Calculate the number of lines by 'Product line'
def solve():
    print(df['Product line'].value_counts())

solve()
# %%
# Calculate the number of Invoices in each of the following 'Total' classes:
# 0-220: low
# 220-440: fair
# 440-660: good
# 660-880: very good
# 880-1100: excellent
def solve():
    df['Total']=pd.cut(df['Total'],[0,220,440,660,880,1100],right=False,labels=['low','fair','good','very_good','excellent'])
    print(df['Total'].value_counts())

solve()
# %%
# Calculate the percentage of Female and Male customers
def solve():
    print(df['Gender'].value_counts().astype(float).div(len(df))*100)

solve()
# %%
def solve():
    df.drop(df[df['City'] == 'Yangon'].index, inplace=True)

solve()

# %%
# Print the 'City', the 'Product line' and the value 'Total' (rounded to two decimal places) corresponding to the maximum sum of the 'Total' by 'City' and 'Product line'
def solve():
    pr=df.groupby(['City','Product line'])['Total'].sum().round(2)
    max=pr.max()
    city=pr.idxmax()[0]
    product=pr.idxmax()[1]
    print(f"{city}, {product}, {max}")

solve()
# %%
def solve():
    smax=df['fastest_lap_speed'].max()
    print(round(df.loc[df['fastest_lap_speed']==smax,['name','race','fastest_lap_speed']],1))

# %%
# Change the 'Customer type' in the third row from 'Normal' to 'Member'
def solve():
    df.loc[2,'Customer type']='Member'
    print(df)

solve()
# %%
# delete column 'Customer type'
def solve():
    df.drop(columns='Customer type',inplace=True)
    print(df)

# %%
# Print the columns 'customer type' to 'Unit price' of the rows where the 'Customer type' is 'Member' and the 'Gender' is 'Male' or the 'Customer type' is 'Normal' and the 'Gender' is 'Female' and the 'Unit price' is greater than 99 
def solve():
    df.loc[((df['Customer type']=='Member')& (df['Gender']=='Male') | (df['Customer type']=='Normal')& (df['Gender']=='Female')) & (df['Unit price']>99),['Customer type','Gender','Product line','Unit price']]
    print(df)
    
solve()
# %%
# Print the rows between labels 0 and 2 and between columns 'Total' and 'Payment'.
def solve():
    print(df.loc[0:2,'Total':'Payment'])

solve()

# %%
# Calculate the invoices 'Total' by 'City' and type of 'Payment'. (rounded to two decimal places)
def solve():
    pf=df.pivot_table(index='City',columns='Payment',values='Total',aggfunc='sum')
    print(pf.round(2))

solve()
# %%
def solve():
    print(df.loc[df['Total']>1030,['Product line','Unit price','Quantity','Tax 5%','Total']])
    

solve()
# %%
# Calculate a summary statistics of the column 'Total'. (rounded to two decimal places)
def solve():
    print(df['Total'].describe().round(2))

solve()

# %%
# Calculate the mean of the Invoice 'Total' for Female customers. (rounded to one decimal place)
def solve():
    print(round(df.loc[df['Gender']=='Female','Total'].mean(),1))

solve()
# %%
# Print the values from columns 'Invoice ID' and 'Total' from row 0 and 2.
def solve():
    print(df.loc[[0,2],['Invoice ID','Total']])

solve()

# %%

# Create a table with the number of invoices by 'City' and 'Customer type' with totals by row and by column.
def solve():
    df2=df.pivot_table(index='City',columns='Customer type',values='Invoice ID',aggfunc='count',margins=True)
    print(df2)

solve()
# %%
def solve():
    df.insert(7, 'QxPrice', df['Unit price'] * df['Quantity'])

#solve()
print(df.loc[0:2,'Unit price':'Total'])

