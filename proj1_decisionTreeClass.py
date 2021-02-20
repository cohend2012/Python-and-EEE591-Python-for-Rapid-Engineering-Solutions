

 # needed for arrays
from sklearn.model_selection import train_test_split   # splits database
from sklearn.preprocessing import StandardScaler       # standardize data
from sklearn.linear_model import Perceptron            # the algorithm
from sklearn.linear_model import LogisticRegression    # the algorithm
from sklearn.metrics import accuracy_score             # grade the results
from sklearn.tree import DecisionTreeClassifier         # the algorithm
from sklearn.tree import export_graphviz

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
print('Number in test ', len(y_test))

for depth in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
# create the classifier and train it
    tree = DecisionTreeClassifier(criterion='entropy',max_depth=depth ,random_state=0)
    tree.fit(X_train,y_train)

    y_pred = tree.predict(X_test)  # now try with the test data


    print('*************')
    print("Results for depth =",depth)
# Note that this only counts the samples where the predicted value was wrong
    print('Misclassified samples: %d' % (y_test != y_pred).sum())  # how'd we do?
    print('Accuracy: %.7f' % accuracy_score(y_test, y_pred))

    # vstack puts first array above the second in a vertical stack
    # hstack puts first array to left of the second in a horizontal stack
    # NOTE the double parens!
    X_combined = np.vstack((X_train, X_test))  # doing combo
    y_combined = np.hstack((y_train, y_test))
    print('Number in combined ', len(y_combined))

# we did the stack so we can see how the combination of test and train data did
    y_combined_pred = tree.predict(X_combined)
    print('Misclassified combined samples: %d' % \
                                    (y_combined != y_combined_pred).sum())
    print('Combined Accuracy: %.7f' % accuracy_score(y_combined, y_combined_pred))
    export_graphviz(tree,out_file='tree1.dot',
                feature_names=['Age','Gender','Polyuria','Polydipsia','sudden weight loss','weakness','Polyphagia','Genital thrush',\
                    'visual blurring',	'Itching',	'Irritability'	,'delayed healing',	'partial paresis',	'muscle stiffness','Alopecia','Obesity'])
    #testing = input()
    print('*************')




