# -*- coding: utf-8 -*-
"""LVADSUSR_176_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ozHcwtGeLEzj9gtqSiDUE6pm1lJlBPpx
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler,StandardScaler , LabelEncoder
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

from numpy import loadtxt


from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score

df = pd.read_csv('/content/winequality-red.csv')
df.head()

data = df.dropna()
data = data.drop_duplicates()

data.head()

data['quality'].unique()

def func(x):
  if x <=6:
    return 0
  else:
    return 1


data["Class"] = data['quality'].apply(func)
data[["quality", "Class"]].head()

df.select_dtypes(include = ['object']).columns
# No categorical columns

X = data.drop(columns = ['quality','Class'])
y = data["Class"]

X_train , X_test , y_train , y_test = train_test_split(X,y,random_state=40)

scaler = MinMaxScaler()
xt_scaled = scaler.fit_transform(X_train)
xtest_scaled = scaler.transform(X_test)

model = RandomForestClassifier()
model.fit(xt_scaled,y_train)
y_pred = model.predict(xtest_scaled)
accuracy = accuracy_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)

print("Accuracy: ", accuracy)
print("Recall: ", recall)
print("Accuracy: ", accuracy)
print("Accuracy: ", accuracy)

