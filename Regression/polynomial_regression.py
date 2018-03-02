# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 23:44:10 2018

@author: Rupesh
"""



# Multiple  Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
# loading dependies

df = pd.read_csv("Position_Salaries.csv")
df.head()

X = df.iloc[:, 1:2].values # X should be of type matrix
y = df.iloc[:, 2].values


# train test split

#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# it doesn't make any sense if we split the data as the sample is too small

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly =  PolynomialFeatures(degree = 2)
X_poly = poly.fit_transform(X) 

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_poly, y)

plt.scatter(X, y, 'green')
plt.plot(X, reg.predict(poly.fit_transform(X)), color = 'red')











