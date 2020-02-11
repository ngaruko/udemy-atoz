# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#for missing data
from sklearn.impute import SimpleImputer

dataset=pd.read_csv('./res/data.csv')
X= pd.DataFrame(dataset.iloc[:, :-1].values)
y = pd.DataFrame(dataset.iloc[:, 3].values)

#missing data


imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean',verbose=0)

imputer = imputer.fit(X.iloc[:, 1:3])

X.iloc[:, 1:3] = imputer.transform(X.iloc[:, 1:3])