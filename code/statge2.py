from __future__ import print_function

import math

from IPython import display
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import linear_model
from keras import *
from sklearn.model_selection import train_test_split
import random
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.preprocessing import sequence
from keras.utils import np_utils

random.seed(10)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format
raw_data = pd.read_csv("https://raw.githubusercontent.com/ZeroZhuang0/DATA1902project/master/submitted/df_combined.csv",sep=",")
data = raw_data.drop(raw_data.index[0])
data = data.reindex()
#denpendent
bit_change = data["bitcoin_close_change"].astype(float)

#indenpedent
data["gold_change"] = data["gold_change"].astype(float)
data["total_crimes"] = data["total_crimes"].astype(float)
data["total_volume_of_tweets"] = data["total_volume_of_tweets"].astype(float)
data["count_negatives"] = data["count_negatives"].astype(float)
data["count_positives"] = data["count_positives"].astype(float)
data["financial_crimes"] = data["financial_crimes"].astype(float)
x=data[["gold_change","total_crimes","total_volume_of_tweets","count_negatives","count_positives","financial_crimes"]].to_numpy()
data["bitcoin_change_level"]=data["bitcoin_close_change"].astype(int)//3
y=data["bitcoin_change_level"].to_numpy()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
y_train = np_utils.to_categorical(y_train, 20)
y_test = np_utils.to_categorical(y_test,20)
model = Sequential()
model.add(Dense(1, input_shape=(6,)))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('relu'))
model.add(Dense(20))
model.add(Activation("softmax"))
model.compile(loss="categorical_crossentropy",metrics=["accuracy"],optimizer="adam")
model.summary()
model.fit(x_train,y_train,batch_size=536, epochs=16, validation_data=(x_test, y_test)) 
regr = linear_model.LinearRegression().fit(x_train,y_train)
