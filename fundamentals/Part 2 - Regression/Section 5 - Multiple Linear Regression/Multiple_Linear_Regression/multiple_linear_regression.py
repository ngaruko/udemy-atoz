# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
#X: all columns but the last one which is the dependent variable
X = dataset.iloc[:, :-1].values
#last column == dependent variable
y = dataset.iloc[:, 4].values

# Encoding categorical data
'''Create dummy variable 0 and 1 for states: California, Florida, New York'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#LabelEncoder :: wighed index
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
#OneHotEncoder ::
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
'''Take all comuns from index one. Remove one columns...
this is normally taken care by the pythobn lib used >>
to avoid redundant dependencies'''
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling >> No need the library will take care of this
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
'''To be compared with our real profit y-test 
to measure how good our model is'''
y_pred = regressor.predict(X_test)