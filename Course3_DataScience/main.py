import pandas as pd
pd.options.mode.chained_assignment = None
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
max_gold = df[df['Gold'] == df['Gold'].max()]
return_val = max_gold.index #country that has max gold medal
#print(return_val[0])
df['SumWin'] = df['Gold'] - df['Gold.1']
max_diff = df[df['SumWin'] == df['SumWin'].max()]
return_val_1 = max_diff.index #contry that has max diff btw summer and winter gold
#print(return_val_1[0])
above_one = df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]
above_one['max'] = (above_one['Gold'] - above_one['Gold.1'])/above_one['Gold']
return_val_2 = above_one['max'].idxmax()
#print((return_val_2))
df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
Points = pd.Series(df['Points'], index=df.index)
#print(Points)
census_df = pd.read_csv('census.csv')
census_df1 = census_df.groupby(['STNAME']).sum()
return_val_3 = census_df1['COUNTY'].idxmax()
#print(return_val_3)
census_df = census_df[census_df.COUNTY != 0]
census_df2 = census_df.sort_values(by = ['CENSUS2010POP'],ascending=False)
series = census_df2['STNAME'].head(3)
print(series.tolist())
census_df['MAXPOP'] = census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
census_df['MINPOP'] = census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
census_df['CHANGE'] = census_df['MAXPOP'] - census_df['MINPOP']
census_df3 = census_df.set_index('CTYNAME')
return_val_4 = census_df3['CHANGE'].idxmax()
#print(return_val_4)


