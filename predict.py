# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TrSNWRt8oaqMIx8rWDVfC6FBFPdFdnZD
"""

from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#Data considered to be in DataFrame Form
#Data in columns TIMESTAMP,CATEGORY,LATITUDE,LONGITUDE
#time date to TIMESTAMP FORM - 2 lines
#HotOneEncode the category column
#pd.get_dummies(df)

def train(data):
  dataset=data.copy()  
  column_1 = data.ix[:,0]
  db=pd.DataFrame({"year": column_1.dt.year,
                "month": column_1.dt.month,
                "day": column_1.dt.day,
                "hour": column_1.dt.hour,
                "dayofyear": column_1.dt.dayofyear,
                "week": column_1.dt.week,
                "weekofyear": column_1.dt.weekofyear,
                "dayofweek": column_1.dt.dayofweek,
                "weekday": column_1.dt.weekday,
                "quarter": column_1.dt.quarter,
               })
  dataset1=dataset.drop('timestamp',axis=1)
  data1=pd.concat([db,dataset1],axis=1)
  data1.dropna(inplace=True)
  X=data1.iloc[:,[1,2,3,4,6,16,17]].values
  y=data1.iloc[:,[10,11,12,13,14,15]].values
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=50)
  knn = KNeighborsClassifier(n_neighbors=11)
  knn.fit(X_train,y_train)
  return knn

def predict(knn,pred):
  pred[0][0]= datetime.datetime.strptime(pred[0][0], '%Y-%m-%d %H:%M:%S.%f')
  week=pred[0][0].dt.week
  month=pred[0][0].dt.month
  hour=pred[0][0].dt.hour
  doy=pred[0][0].dt.dayofyear
  dow=pred[0][0].dt.dayofweek
  col1=pred[0][1:]
  pred[0].insert(0,week)
  pred[0].insert(0,month)
  pred[0].insert(0,hour)
  pred[0].insert(0,doy)
  pred[0].insert(0,dow)
  print (pred)
  result=knn.predict(pred)
  label=list(result[0]).index(1)
  if label==0:
    print ("Physical Abuse")
  elif label==1:
    print("Sexual Abuse")
  elif label==2:
    print("Emotional Abuse")
  elif label==3:
    print("Financial Abuse")
  elif label==4:
    print("Criminal Harassment")
  else:
    print("Other")

k=train(data)

predict(k,[[2018-02-28 10:15:00 , 22.769531,
        75.888772]])

x=[[ 2.      , 59.      , 10.      ,  2.      ,  9.      , 22.769531,
        75.888772]]

x[1].insert(0,3)
x

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data=pd.read_csv('data3.csv')
dataset=pd.read_csv('data3.csv')





data.head()

#data = data.rename(columns={'act379': 'Physical', 'act13': 'Sexual', 'act279': 'Emotional', 'act323': 'Financial', 'act363': 'Criminal', 'act302': 'Other'})

column_1 = data.ix[:,0]

db=pd.DataFrame({"year": column_1.dt.year,
              "month": column_1.dt.month,
              "day": column_1.dt.day,
              "hour": column_1.dt.hour,
              "dayofyear": column_1.dt.dayofyear,
              "week": column_1.dt.week,
              "weekofyear": column_1.dt.weekofyear,
              "dayofweek": column_1.dt.dayofweek,
              "weekday": column_1.dt.weekday,
              "quarter": column_1.dt.quarter,
             })

data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')

data['timestamp'] = pd.to_datetime(data['timestamp'], format = '%d/%m/%Y %H:%M:%S')

#data.to_csv('data3.csv', index=False)

data.head()



dataset1=dataset.drop('timestamp',axis=1)

dataset1.head()

data1=pd.concat([db,dataset1],axis=1)

data1.head()

data1.info()

data1.dropna(inplace=True)

data1.head()

X=data1.iloc[:,[1,2,3,4,6,16,17]].values

len(X)

y=data1.iloc[:,[10,11,12,13,14,15]].values

y[1]

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=50)

len(X_train)

knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X_train,y_train)

knn.score(X_test,y_test)

result=knn.predict([[ 2.      , 59.      , 15.      ,  2.      ,  9.      , 22.723873,
       75.828416]])

result

















label=list(result[0]).index(1)

if label==0:
  print ("Physical Abuse")
elif label==1:
  print("Sexual Abuse")
elif label==2:
  print("Emotional Abuse")
elif label==3:
  print("Financial Abuse")
elif label==4:
  print("Criminal Harassment")
else:
  print("Other")









from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=50, random_state=100)

dt.fit(X_train,y_train)

y_pred=dt.predict(X_test)

len(y_pred)

len(X_test)



y_pred

data1.dtypes.index

#Physical Abuse,Sexual Abuse,Financial Abuse,Emotional Abuse,Criminal Harassment, Other



y_test

knn.score(X_test,y_test)



df = pd.DataFrame({'country': ['russia', 'germany', 'australia','korea','germany']})

df["col2"]=[1,2,34,5,5]

df



df.dtypes

pd.get_dummies(df)

