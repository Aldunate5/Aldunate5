import pandas as pd

df = pd.read_csv('data.csv')
# Newline to separate print statements
print('{}\n'.format(df))

df = pd.read_csv('data.csv', index_col=0)
print('{}\n'.format(df))

# Predefined df of MLB stats
print('{}\n'.format(df))

groups = df.groupby('yearID')
for name, group in groups: #name asigned to group (this case year); group collection of info for said group (entry)
    print('Year: {}'.format(name))
    print('{}\n'.format(group))

#options for different groups
print('{}\n'.format(groups.get_group(2016)))
print('{}\n'.format(groups.sum()))
print('{}\n'.format(groups.mean()))

#filtering
#lambda for inner functions
no2015 = groups.filter(lambda x: x.name > 2015)
print(no2015)

#multi columns
# player_df is predefined
groups = player_df.groupby(['yearID', 'teamID']) #creates subsets of groups for each parent group

for name, group in groups:
  print('Year, Team: {}'.format(name))
  print('{}\n'.format(group))

print(groups.sum())

#features: quantitive or categorical (groupby)
df = pd.DataFrame({
    'T1': [10, 15, 8],
    'T2': [25, 27, 25],
    'T3': [16, 15, 10]})

print('{}\n'.format(df)) #arrange by column

print('{}\n'.format(df.sum())) #default for each column
print('{}\n'.format(df.sum(axis=1))) #for row

print('{}\n'.format(df.mean()))
print('{}\n'.format(df.mean(axis=1)))

df_ms = df.multiply([1000, 1], axis=0) #ordena para columna
print('{}\n'.format(df_ms))
df_w = df_ms.multiply([1,0.5,1]) #default axis=1

def col_list_sum(df, col_list, weights=None):
    col_df = df[col_list]
    if weights is not None:
        col_df = col_df.multiply(weights)
    return col_df.sum(axis=1)

mlb_df['BA'] = mlb_df['H'] / mlb_df['AB'] #toma el valor de cada indice y genera nueva columna
other_hits=col_list_sum(mlb_df,['2B','3B','HR'],1)
mlb_df['1B']=mlb_df['H']-other_hits

df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39]})

print('{}\n'.format(df))

cruzne02 = df['playerID'] == 'cruzne02' #return boolean
print('{}\n'.format(cruzne02))
hr40 = df['HR'] > 40
print('{}\n'.format(hr40))
notbos = df['teamID'] != 'BOS'
print('{}\n'.format(notbos))

str_f1 = df['playerID'].str.startswith('c') #string filters also return boolean
print('{}\n'.format(str_f1))
str_f2 = df['teamID'].str.endswith('S')
print('{}\n'.format(str_f2))
str_f3 = ~df['playerID'].str.contains('o') #opposite ~
print('{}\n'.format(str_f3))

isin_f1 = df['playerID'].isin(['cruzne02','ortizda01']) #isin for list for filter
print('{}\n'.format(isin_f1))
isin_f2 = df['yearID'].isin([2015, 2017])
print('{}\n'.format(isin_f2))

#.isna(), notna()

#filtering for rows df[condicion]

hr40_df = df[df['HR'] > 40]
print('{}\n'.format(hr40_df))
not_hr30_df = df[~(df['HR'] > 30)]
print('{}\n'.format(not_hr30_df))
str_df = df[df['teamID'].str.startswith('B')]
print('{}\n'.format(str_df))

#sorting
print('{}\n'.format(df))

#numerical or alphabetical, ascending as default .sort_values()
sort1 = df.sort_values('yearID')
print('{}\n'.format(sort1))
sort2 = df.sort_values('playerID', ascending=False)
print('{}\n'.format(sort2))

sort2 = df.sort_values(['yearID', 'HR'],ascending=[True, False])
#multiple sorting (list) second sorts subgroup of first
print('{}\n'.format(sort2))

#metrics
metrics1 = hr_rbi.describe(percentiles=[.5]) #default 0.25,0.5,0.75
print('{}\n'.format(metrics1))

#for cateogircal
print('{}\n'.format(p_ids.value_counts()))
print('{}\n'.format(p_ids.value_counts(normalize=True)))

print('{}\n'.format(p_ids.value_counts(ascending=True)))

unique_players = df['playerID'].unique() #return list (set)
print('{}\n'.format(repr(unique_players)))


#Indicator feature transform categorical tu numeric (input for ML)
print('{}\n'.format(df))

converted = pd.get_dummies(df) #new dataframe with dummies
print('{}\n'.format(converted.columns)) #list of index indicators

print('{}\n'.format(converted[['teamID_BOS',
                               'teamID_PIT']]))
print('{}\n'.format(converted[['lgID_AL',
                               'lgID_NL']]))
n_matrix = converted.values #return as numpy array
