# Data Preprocessing Template

import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder


# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


# taking care of missing data
'''The imputation strategy.
 
    - If "mean", then replace missing values using the mean along
      the axis.
    - If "median", then replace missing values using the median along
      the axis.
    - If "most_frequent", then replace missing using the most frequent
      value along the axis.
 '''
imputer= Imputer(missing_values= 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
#To categorise values that are not numeric for better maths
labelEncoder_X= LabelEncoder()
X[:,0] = labelEncoder_X.fit_transform(X[:,0])

oneHotEncoder = OneHotEncoder(categorical_features= [0])
X = oneHotEncoder.fit_transform(X).toarray()


labelEncoder_y= LabelEncoder()
y = labelEncoder_y.fit_transform(y)