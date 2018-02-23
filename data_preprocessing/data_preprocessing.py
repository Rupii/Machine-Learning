# common libraries for preprocessing

#numerical libraries
import numpy as np
import pandas as pd

#ploting libraries
import matplotlib.pyplot as plt

#importing dataset
df = pd.read_csv('Data.csv')
print(df)

#features
X = df.iloc[:, :-1].values
#labels
y = df.iloc[:, 3].values

# missing data
from sklearn .preprocessing import Imputer
impute = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
impute = impute.fit(X[:, 1:3])
X[:, 1:3] = impute.transform(X[:, 1:3])

print(X)