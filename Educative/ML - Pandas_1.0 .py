import pandas as pd
import numpy as np

series = pd.Series([1, 2, 3],index=['a', 'b', 'c'])
print('{}\n'.format(series))

series2 = pd.Series({'b':2, 'a':1, 'c':3})
print('{}\n'.format(series2))

arr = np.array([1, 2])
series = pd.Series(arr, dtype=np.float32)
print('{}\n'.format(series))

df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])
print('{}\n'.format(df))
print(df.T)
print(df.dtypes)

df = pd.DataFrame([[5, 6], [1.2, 3]])
ser = pd.Series([0, 0], name='r3')

df_app = df.append(ser) #no se modifica original, se crea uno nuevo
print('{}\n'.format(df_app))

df_app = df.append(ser, ignore_index=True)
print('{}\n'.format(df_app))

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
print(df)
# Drop row r1
df_drop = df.drop(labels='r1') #labels, index= or column=
print('{}\n'.format(df_drop))

# Drop columns c1, c3
df_drop = df.drop(labels=['c1', 'c3'], axis=1) #default is rows, axis=0
print('{}\n'.format(df_drop))

#concatenate
df1 = pd.DataFrame({'c1':[1,2], 'c2':[3,4]},
                   index=['r1','r2'])
df2 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]},
                   index=['r1','r2'])
df3 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]})

concat = pd.concat([df1, df2], axis=1) #axis=0 is default, rows
# Newline to separate print statements
print('{}\n'.format(concat))

concat = pd.concat([df2, df1, df3])
print('{}\n'.format(concat))

mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})

print('{}\n'.format(mlb_df1))
print('{}\n'.format(mlb_df2))

mlb_merged = pd.merge(mlb_df1, mlb_df2) #merge only things in common
print('{}\n'.format(mlb_merged))


#Indexing
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])
col1 = df['c1'] #first [] retrieves as series
# Newline for separating print statements
print('{}\n'.format(col1))

col1_df = df[['c1']] #second [] allows to retrieve column indexes, list of columns
print('{}\n'.format(col1_df))

col23 = df[['c2', 'c3']]
print('{}\n'.format(col23))


df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(df))

first_two_rows = df[0:2] #integer doesnt include last
print('{}\n'.format(first_two_rows))

last_two_rows = df['r2':'r3'] #does include last
print('{}\n'.format(last_two_rows))

#iloc retrieves rows with integers
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(df))

print('{}\n'.format(df.iloc[1]))

print('aqui','{}\n'.format(df.iloc[[0, 2],0:2])) #mixing row index with column index

bool_list = [False, True, True]
print('{}\n'.format(df.iloc[bool_list]))

#loc retrieves rows with labels
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(df))

print('{}\n'.format(df.loc['r2']))

bool_list = [False, True, True]
print('{}\n'.format(df.loc[bool_list]))

single_val = df.loc['r1', 'c2']
print('Single val: {}\n'.format(single_val))

print('{}\n'.format(df.loc[['r1', 'r3'], 'c2'])) #can mix row index with column index
print(df['c2'].loc[['r1','r3']]) #alternativa

df.loc[['r1', 'r3'], 'c2'] = 0
print('{}\n'.format(df))