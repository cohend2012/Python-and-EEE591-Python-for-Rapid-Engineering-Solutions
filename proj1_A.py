

import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd


# step 1 read in data as a df
# can we read it back in?
diabetes_df = read_csv('diabetes_data_upload.csv')
print('\n\nRead the data back in...')
print(type(diabetes_df))
print(diabetes_df)

# data has been read in so far

# check for missing data


print(diabetes_df.dtypes)

print(diabetes_df.info())

# no missing data
print(diabetes_df.isnull().sum(),"\n")

# data is not 100% ready, we must text should become numeric values

diabetes_df = diabetes_df.replace(['Male', 'Female','No','Yes','Positive', 'Negative'],[1,0,0,1,1,0])

print(diabetes_df)

# Changed the values to 1 and 0

# print the top 10 correlations in data base

#print(np.tri(520, 17,1).T)

corr = diabetes_df.corr().abs()

#print(corr)


corr *= np.tri(*corr.values.shape, k=-1).T

print(corr)

corr_unstack = corr.unstack()
print(corr_unstack)

print(type(corr_unstack))

corr_unstack.sort_values(inplace=True,ascending=False)

print("Top 10 database correlation\n",corr_unstack.head(10))

# step 4 print the top 10 correlations with the class in the data base

with_type = corr_unstack.get(key = "class")

print("Top 10 class correlation\n",with_type.head(10))

cov = diabetes_df.cov().abs()


cov *= np.tri(*cov.values.shape, k=-1).T

print(cov)

cov_unstack = cov.unstack()
print(cov_unstack)

print(type(cov_unstack))

cov_unstack.sort_values(inplace=True,ascending=False)

print("Top 10 database covariance\n",cov_unstack.head(10))

# step 4 print the top 10 correlations with the class in the data base

with_type_cov = cov_unstack.get(key = "class")

print("Top 10 class covariance\n",with_type_cov.head(10))

