# -*- coding: utf-8 -*-
"""Rock vs Mine.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17zMK34584iKmf39CnAgg8Mn2ycfQwjoe

Importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Data Processing"""

#loading the dataset to a pandas Dataframe
sonar_data = pd.read_csv('/content/sonar data.csv',header=None)

sonar_data.head()

#number of rows and columns
sonar_data.shape

sonar_data.describe() #describe--> statistical measures of the data

sonar_data[60].value_counts() #60 mention how many coloumn we took for count(there 61 coloumn out there and last one is indicating rock or mine)

"""M --> Mine
R --> Rock
"""

sonar_data.groupby(60).mean()

#separting data and Labels

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Training and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

"""Model Training --> Logistic Regrression"""

model = LogisticRegression()

#training the Logistic Regression Model with training data
model.fit(X_train, Y_train)

"""Model Evaluavtion"""

#accuracy on the training data
X_train_predeiction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_predeiction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)

#accuracy on the test data
X_test_predeiction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_predeiction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)

"""Making a predictive System"""

input_data = (0.0519,0.0548,0.0842,0.0319,0.1158,0.0922,0.1027,0.0613,0.1465,0.2838,0.2802,0.3086,0.2657,0.3801,0.5626,0.4376,0.2617,0.1199,0.6676,0.9402,0.7832,0.5352,0.6809,0.9174,0.7613,0.8220,0.8872,0.6091,0.2967,0.1103,0.1318,0.0624,0.0990,0.4006,0.3666,0.1050,0.1915,0.3930,0.4288,0.2546,0.1151,0.2196,0.1879,0.1437,0.2146,0.2360,0.1125,0.0254,0.0285,0.0178,0.0052,0.0081,0.0120,0.0045,0.0121,0.0097,0.0085,0.0047,0.0048,0.0069) # Remove 'R' from the tuple

#converting input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a Mine')

