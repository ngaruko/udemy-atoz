# Data Preprocessing Template

import pandas as pd

from sklearn.cross_validation import train_test_split

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# taking care of missing data removed

# Encoding (removed)

#Splitting the dataset into the Training set and Test set
#20% chosen as our test observations
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature scaling
'''Scaling data for data that are on different scales to avoid calculations discrepencies
 due to the euclidian distance which is based on squares'''
 #comment out cuse not always needed

'''from sklearn.preprocessing import StandardScaler
scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)'''