# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:57:08 2018

@author: Rupesh
"""


# Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
# loading dependies

df = pd.read_csv("Salary_Data.csv")
df.head()
X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

# Ploting the data 
sns.pairplot(df)
plt.show()
"""
Seems like the is a relation between the data 
on Experience and Salary 
which is obvious
"""


# spliting the dataset into train and test sets
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)


# appling the Regression model
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)


pred = lm.predict(X_test)

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, pred, color = 'blue')
plt.title("Salary V Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
lm.score(X_test, y_test)
# gives the accuracy at which the model predicts

