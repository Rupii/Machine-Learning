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

# categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
X_cat = LabelEncoder()
X[:, 0] = X_cat.fit_transform(X[:, 0])
# labels in ordered way
# i.e., france 3 germany 0
# hot encoding / dummy variables 

onehot = OneHotEncoder(categorical_features = [0])
X = onehot.fit_transform(X).toarray()

y_cat = LabelEncoder()
y = y_cat.fit_transform(y)

# train testt split

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)



# preprocessing 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

