

from m5_plotdr import plot_decision_regions            # visualize results
import matplotlib.pyplot as plt                        # update the plot
from sklearn import datasets                           # read the data
import numpy as np                                     # for arrays
from sklearn.model_selection import train_test_split   # split the data
from sklearn.preprocessing import StandardScaler       # scale the data
from sklearn.neighbors import KNeighborsClassifier     # the algorithm
from sklearn.metrics import accuracy_score

# load data set

# get the X data

# get the y data
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


# data is not 100% ready, we must text should become numeric values

diabetes_df = diabetes_df.replace(['Male', 'Female','No','Yes','Positive', 'Negative'],[1,0,0,1,1,0])

print(diabetes_df)

X = diabetes_df[['Age','Gender','Polyuria','Polydipsia','sudden weight loss','weakness','Polyphagia','Genital thrush',\
   'visual blurring',	'Itching',	'Irritability'	,'delayed healing',	'partial paresis',	'muscle stiffness','Alopecia','Obesity']]


print(X)

#diabetes_df.reset_index(inplace=True,drop=True)

#print(diabetes_df)

# you can use a df right into sk learn train_test_split

y = diabetes_df.loc[:,'class'].values
print('y values',y)

X_train, X_test, y_train, y_test = \
         train_test_split(X,y,test_size=0.3,random_state=0)

sc = StandardScaler()                    # create the standard scalar
sc.fit(X_train)                          # compute the required transformation
X_train_std = sc.transform(X_train)      # apply to the training data
X_test_std = sc.transform(X_test)        # and SAME transformation of test data

print('X train std',X_train_std)

print('y test looks like',y_test)

print('y train looks like', y_train)

for neighs in [1,2,3,4,5,6,7,8,9,10,15,20,25,30,50,75,100]:
    print('*******************')
    print(neighs,'neighbors')
    knn = KNeighborsClassifier(n_neighbors=neighs,p=2,metric='minkowski')
    knn.fit(X_train_std,y_train)

    # run on the test data and print results and check accuracy
    y_pred = knn.predict(X_test_std)
    print('Number in test ',len(y_test))
    print('Misclassified samples: %d' % (y_test != y_pred).sum())
    print('Accuracy: %.7f ' % accuracy_score(y_test, y_pred))

    # combine the train and test data
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))
    print('Number in combined ',len(y_combined))

    # check results on combined data
    y_combined_pred = knn.predict(X_combined_std)
    print('Misclassified samples: %d' % (y_combined != y_combined_pred).sum())
    print('Combined Accuracy: %.7f' % \
           accuracy_score(y_combined, y_combined_pred))
    print('*******************')
