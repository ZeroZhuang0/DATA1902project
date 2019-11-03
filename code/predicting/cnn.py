    ## Importing necessary libraries

import math

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import random
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.preprocessing import sequence
from keras.utils import np_utils

random.seed(10)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

raw_data = pd.read_csv("../../datasets/final/df_combined.csv",sep=",")

data = raw_data.drop(raw_data.index[0]) # Since the first entry for bitcoin_close_change is NaN
data = data.reindex() # Reindex the dataset

# Dependent variable
bitcoin_change = data["bitcoin_close_change"].astype(float)

# Indepedent variables to type float
data["gold_change"] = data["gold_change"].astype(float)
data["total_crimes"] = data["total_crimes"].astype(float)
data["total_volume_of_tweets"] = data["total_volume_of_tweets"].astype(float)
data["sent_negatives"] = data["sent_negatives"].astype(float)
data["sent_positives"] = data["sent_positives"].astype(float)
data["financial_crimes"] = data["financial_crimes"].astype(float)

# Setting up the input and output arrays
x = data[["gold_change","total_crimes","total_volume_of_tweets","sent_negatives","sent_positives","financial_crimes"]].to_numpy()
y = (data["bitcoin_close_change"].astype(int) // 2).to_numpy()
y = np_utils.to_categorical(y, 28) # Categorising the output into 28 nodes

# Splitting the dataset into training and testing datasets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

model = Sequential() # Defining a new classification model
model.add(Dense(64, activation = "tanh", input_shape = (6,)))
model.add(Dense(128, activation = "tanh"))
model.add(Dense(64, activation = "tanh"))
model.add(Dense(32, activation = "tanh"))
model.add(Dense(28, activation = "softmax"))

# Compiling the model using the appropriate loss function and optimiser
model.compile(loss = "categorical_crossentropy",
        metrics = ["accuracy"],
        optimizer = "adam")
model.summary() # Printing a summary of the model
model.fit(x_train, y_train,
        batch_size = 64, 
        epochs = 16)

# Evaluating its performance
performance = model.evaluate(x_test, y_test)

print(
'''
On the Test Data:
Loss -> %.3f
Accuracy -> %.3f
'''
% tuple(performance))
