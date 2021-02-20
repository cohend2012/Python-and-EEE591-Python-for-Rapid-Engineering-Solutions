
#############################################
#   By: Dan Cohen                           #
#   Data: 2/7/2021                          #
#   ASU ID# 1204831845                      #
#   For class: Rapid Prototyping in python  #
#   Prof. Dr. Steve Millman                 #
#   proj1_B.py                              #
#   Machine learning for  diabetes          #
#                                           #
#############################################
# #start of code


from m5_plotdr import plot_decision_regions            # plotting function
import matplotlib.pyplot as plt                        # so we can add to plot
from sklearn import datasets                           # read the data sets
                                    # needed for arrays
from sklearn.model_selection import train_test_split   # splits database
from sklearn.preprocessing import StandardScaler       # standardize data
from sklearn.linear_model import Perceptron            # the algorithm
from sklearn.linear_model import LogisticRegression    # the algorithm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier     # the algorithm
from sklearn.metrics import accuracy_score             # grade the results'
import matplotlib.pyplot as plt
from sklearn.metrics import plot_roc_curve



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


print('**********************************')
print('Start of Perceptron')
print('**********************************')

ppn = Perceptron(max_iter=10, tol=1e-3, eta0=0.001,
                 fit_intercept=True, random_state=0, verbose=True)
ppn.fit(X_train_std, y_train)  # do the training

print('Number in test ', len(y_test))
y_pred = ppn.predict(X_test_std)  # now try with the test data



# Note that this only counts the samples where the predicted value was wrong
print('Misclassified samples: %d' % (y_test != y_pred).sum())  # how'd we do?
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# vstack puts first array above the second in a vertical stack
# hstack puts first array to left of the second in a horizontal stack
# NOTE the double parens!
X_combined_std = np.vstack((X_train_std, X_test_std))  # doing combo
y_combined = np.hstack((y_train, y_test))
print('Number in combined ', len(y_combined))

# we did the stack so we can see how the combination of test and train data did
y_combined_pred = ppn.predict(X_combined_std)
print('Misclassified combined samples: %d' % \
      (y_combined != y_combined_pred).sum())
print('Combined Accuracy: %.4f' % accuracy_score(y_combined, y_combined_pred))
#print('combo test',X_combined_std[:,0:2])
# now visualize the results

print('**********************************')
print('Start of Log Reg')
print('**********************************')


# cost should be moved
c_val = 0.25



lr = LogisticRegression(C=c_val, solver='liblinear', \
                            multi_class='ovr', random_state=0)
lr.fit(X_train_std, y_train)  # do the training

print('Number in test ', len(y_test))
y_pred = lr.predict(X_test_std)  # now try with the test data



# Note that this only counts the samples where the predicted value was wrong
print('Misclassified samples: %d' % (y_test != y_pred).sum())  # how'd we do?
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

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
print('Combined Accuracy: %.4f' % accuracy_score(y_combined, y_combined_pred))



print('**********************************')
print('SVC')
print('**********************************')
c_val =0.25

svm = SVC(kernel='linear', C=c_val, random_state=0)
svm.fit(X_train_std, y_train)  # do the training

y_pred = svm.predict(X_test_std)  # work on the test data

# show the results
print('*************')
print("Results for C =", c_val)
print('Number in test ', len(y_test))
print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.4f' % accuracy_score(y_test, y_pred))

# combine the train and test sets
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

# and analyze the combined sets
print('Number in combined ', len(y_combined))
y_combined_pred = svm.predict(X_combined_std)
print('Misclassified combined samples: %d' % \
      (y_combined != y_combined_pred).sum())
print('Combined Accuracy: %.4f' % \
      accuracy_score(y_combined, y_combined_pred))



depth =7

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
print('*************')


trees = 5

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
print('*************')

neighs =3

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


ax = plt.gca()
disp0 = plot_roc_curve(ppn,X_test,y_test,ax=ax,alpha=0.7)
disp1 = plot_roc_curve(lr,X_test,y_test,ax=ax,alpha=0.7)
disp2 = plot_roc_curve(svm,X_test,y_test,ax=ax,alpha=0.7)
disp3 = plot_roc_curve(tree,X_test,y_test,ax=ax,alpha=0.7)
disp4 = plot_roc_curve(forest,X_test,y_test,ax=ax,alpha=0.7)
disp5 = plot_roc_curve(knn,X_test,y_test,ax=ax,alpha=0.7)


plt.show()

