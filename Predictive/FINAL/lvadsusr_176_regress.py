# -*- coding: utf-8 -*-
"""LVADSUSR_176_REGRESS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U-iOdouO9TEXkmrXukmmxqOuH68XKe91
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler,StandardScaler , LabelEncoder
from sklearn.ensemble import RandomForestRegressor

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

from numpy import loadtxt
from sklearn.model_selection import train_test_split

from sklearn.metrics import r2_score,mean_squared_error , silhouette_score
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score , confusion_matrix

import pandas as pd
fare = pd.read_csv('/content/Fare prediction.csv')
fare.head()

from datetime import datetime
fare["year"] = pd.to_datetime(fare['pickup_datetime']).dt.year
fare['month'] = pd.to_datetime(fare['pickup_datetime']).dt.month
fare['hour'] = pd.to_datetime(fare['pickup_datetime']).dt.hour
fare.head()

x=[]
for i in fare['hour']:
  x.append(int(i))
fare['hour'] = x
fare.head()

fare.describe()

fare["dist"] = np.sqrt(  (fare["pickup_latitude"] - fare["dropoff_latitude"])**2 +
                          (fare["pickup_longitude"] - fare["dropoff_longitude"])**2
                         )
fare.head()

fd = fare.drop(columns = ['pickup_datetime'])
fd.head()

for i in fd.columns:
  sns.boxplot(fd[i])
  plt.show()

for i in fd.columns:
  plt.hist(fd[i])
  plt.title(i)
  plt.show()

# outliers
print(fd.shape)
q1 = fd['dist'].quantile(0.25)
q3 = fd['dist'].quantile(0.75)
iqr = q3-q1
lower = q1-1.5*iqr
upper = q3+1.5*iqr
mask =  (fd['dist'] >lower ) & (fd['dist'] < upper )
new_df = fd[mask]
print(new_df.shape)

print(new_df.shape)
new_df = new_df.dropna()
new_df = new_df.drop_duplicates()
print(new_df.shape)

numeric = new_df.select_dtypes(include = ['int64','float64']).columns
heat = new_df[numeric].corr()

sns.heatmap(heat)

data = new_df.drop(columns = ['key','dropoff_longitude','dropoff_latitude'])
# dropping correlated columns
data.head()

X = data.drop(columns = ['fare_amount'])
y = data["fare_amount"]
y.head()

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 0.2,random_state=42)

scaler = StandardScaler()
xtrain_s = scaler.fit_transform(X_train)
xtest_s = scaler.transform(X_test)

model = RandomForestRegressor()
model.fit(xtrain_s,y_train)
y_pred = model.predict(xtest_s)
r2 = r2_score(y_test,y_pred)
MSE = mean_squared_error(y_test,y_pred)
RMSE = mean_squared_error(y_test,y_pred,squared=False)
print("MSE: ",MSE)
print("RMSE: ",RMSE)
print("R2 Score: ", r2)

model = LinearRegression()
model.fit(xtrain_s,y_train)
y_pred = model.predict(xtest_s)
r2 = r2_score(y_test,y_pred)
MSE = mean_squared_error(y_test,y_pred)
RMSE = mean_squared_error(y_test,y_pred,squared=False)
print("MSE: ",MSE)
print("RMSE: ",RMSE)
print("R2 Score: ", r2)

# Random Forest regressor works best