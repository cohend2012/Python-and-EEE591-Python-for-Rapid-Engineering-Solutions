                                   # needed for arrays
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split   # splits database
from sklearn.preprocessing import StandardScaler       # standardize data
from sklearn.linear_model import Perceptron            # the algorithm
from sklearn.linear_model import LogisticRegression    # the algorithm
from sklearn.metrics import accuracy_score             # grade the results
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier         # the algorithm
from sklearn.tree import export_graphviz
from pandas.plotting import radviz

# load data set

# get the X data

# get the y data
import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd
plot.figure()

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
print('Number in test ', len(y_test))

for trees in [1,2,3,4,5,6,7,8,9,10,11,12,15, 101]:
    print('*************')
    print("Number of trees: ", trees)
        # create the classifier and train it
        # n_estimators is the number of trees in the forest
        # the entropy choice grades based on information gained
        # n_jobs allows multiple processors to be used
    forest = RandomForestClassifier(criterion='entropy', n_estimators=trees, \
                                                random_state=1, n_jobs=-1)
    forest.fit(X_train, y_train)

    y_pred = forest.predict(X_test)  # see how we do on the test data
    print('Number in test ', len(y_test))
    print('Misclassified samples: %d' % (y_test != y_pred).sum())

    print('Accuracy: %.7f \n' % accuracy_score(y_test, y_pred))

    # combine the train and test data
    X_combined = np.vstack((X_train, X_test))
    y_combined = np.hstack((y_train, y_test))
    print('Number in combined ', len(y_combined))

    # see how we do on the combined data
    y_combined_pred = forest.predict(X_combined)
    print('Misclassified samples: %d' % (y_combined != y_combined_pred).sum())
    print('Combined Accuracy: %.7f' % \
            accuracy_score(y_combined, y_combined_pred))
    diabetes_df(data).T.plot()
    plt.show()
    print('*************')