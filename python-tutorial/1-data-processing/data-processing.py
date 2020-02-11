# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('./res/data.csv')
z = dataset.iloc[:, :-1]
X= pd.DataFrame(dataset.iloc[:, :-1].values)
y = pd.DataFrame(dataset.iloc[:, 3].values)
