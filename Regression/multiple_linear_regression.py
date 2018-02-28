# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:18:54 2018

@author: Rupesh
"""



# Multiple  Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
# loading dependies

df = pd.read_csv("50_Startups.csv")
df.head()
X = df.iloc[:, :-1].values
y = df.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
X_cat = LabelEncoder()
X[:, 3] = X_cat.fit_transform(X[:, 3])

onehot = OneHotEncoder(categorical_features = [3])
X = onehot.fit_transform(X).toarray()
# avoiding the dummy variable trap
X = X[:, 1:]


# train test split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# model
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, y_train)

# predict

y_pred = reg.predict(X_test)
import skl