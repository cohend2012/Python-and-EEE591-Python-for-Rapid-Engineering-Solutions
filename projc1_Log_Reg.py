# Dan cohen

from m5_plotdr import plot_decision_regions            # plotting function
import matplotlib.pyplot as plt                        # so we can add to plot
from sklearn import datasets                           # read the data sets
                                    # needed for arrays
from sklearn.model_selection import train_test_split   # splits database
from sklearn.preprocessing import StandardScaler       # standardize data
from sklearn.linear_model import Perceptron            # the algorithm
from sklearn.linear_model import LogisticRegression    # the algorithm
from sklearn.metrics import accuracy_score             # grade the results


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

for c_val in [0.0001,0.001,0.1,0.25,0.50,1,10,100,200,300,500,700,1000]:
    print('C value',c_val)

    lr = LogisticRegression(C=c_val, solver='liblinear', \
                            multi_class='ovr', random_state=0)
    lr.fit(X_train_std, y_train)  # do the training

    print('Number in test ', len(y_test))
    y_pred = lr.predict(X_test_std)  # now try with the test data



# Note that this only counts the samples where the predicted value was wrong
    print('Misclassified samples: %d' % (y_test != y_pred).sum())  # how'd we do?
    print('Accuracy: %.7f' % accuracy_score(y_test, y_pred))

    # vstack puts first array above the second in a vertical stack
    # hstack puts first array to left of the second in a horizontal stack
    # NOTE the double parens!
    X_combined_std = np.vstack((X_train_std, X_test_std))  # doing combo
    y_combined = np.hstack((y_train, y_test))
    print('Number in combined ', len(y_combined))

# we did the stack so we can see how the combination of test and train data did
    y_combined_pred = lr.predict(X_combined_std)
    print('Misclassified combined samples: %d' % \
                                    (y_combined != y_combined_pred).sum())
    print('Combined Accuracy: %.7f' % accuracy_score(y_combined, y_combined_pred))



#print('combo test',X_combined_std[:,0:2])
# now visualize the results







