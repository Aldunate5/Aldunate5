import numpy as np
import pandas as pd
pizza_data=np.array(([[2100,   10,  800],
       [2500,   11,  850],
       [1800,   10,  760],
       [2000,   12,  800],
       [2300,   11,  810]]))

print('{}\n'.format(repr(pizza_data)))

from sklearn.preprocessing import scale, MinMaxScaler

col_standardized = scale(pizza_data) # Standardizing each column of pizza_data
print('{}\n'.format(repr(col_standardized)))
col_means = col_standardized.mean(axis=0)
print(col_means)
col_stds = col_standardized.std(axis=0)
print(col_stds)


data=np.array([[ 1.2,  3.2],
       [-0.3, -1.2],
       [ 6.5, 10.1],
       [ 2.2, -8.4]])
print(data)

default_scaler=MinMaxScaler()
transformed=default_scaler.fit_transform(data) #by column
print(transformed)
costum_scaler=MinMaxScaler(feature_range=(-2,3))
new_transformed=costum_scaler.fit_transform(data)
print(new_transformed)

from sklearn.preprocessing import RobustScaler #scales by the median
data2=np.array([[ 1.2,  2.3],
       [ 2.1,  4.2],
       [-1.9,  3.1],
       [-2.5,  2.5],
       [ 0.8,  3. ],
       [ 6.3,  2.1],
       [-1.5,  2.7],
       [ 1.4,  2.9],
       [ 1.8,  3.2]])
rb=RobustScaler()
transformed=rb.fit_transform(data2)
print('\n',transformed)

#L2 normalized by row
data=np.array([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])
from sklearn.preprocessing import Normalizer
normalizer=Normalizer()
transformed=normalizer.fit_transform(data)
print(data,transformed)

#missing data: mean, median, mode, constant
data=np.array([[ 1.,  2., nan,  2.],
       [ 5., nan,  1.,  2.],
       [ 4., nan,  3., nan],
       [ 5.,  6.,  8.,  1.],
       [nan,  7., nan,  0.]])

from sklearn.impute import SimpleImputer #replace nan with mean as impute per column; strategy allows optoins
imp_mean = SimpleImputer()
transformed = imp_mean.fit_transform(data)
'''
imp_median = SimpleImputer(strategy='median')
transformed = imp_median.fit_transform(data)
imp_frequent = SimpleImputer(strategy='most_frequent')
transformed = imp_frequent.fit_transform(data)
imp_constant = SimpleImputer(strategy='constant',
                             fill_value=-1)
transformed = imp_constant.fit_transform(data)
'''
print('{}\n'.format(repr(transformed)))

#PCA: for dimensionality reduction (only those that matter)
data=np.array([[ 1.5,  3. ,  9. , -0.5,  1. ],
       [ 2.2,  4.3,  3.5,  0.6,  2.7],
       [ 3. ,  6.1,  1.1,  1.2,  4.2],
       [ 8. , 16. ,  7.7, -1. ,  7.1]])

from sklearn.decomposition import PCA
pca_obj = PCA() # The value of n_component will be 4. As m is 5 and default is always m-1, default
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

pca_obj = PCA(n_components=3)
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

pca_obj = PCA(n_components=2)
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))
#measures correlation between columns

