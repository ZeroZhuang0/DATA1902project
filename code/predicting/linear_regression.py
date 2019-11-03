# Importing necessary libraries
import pandas as pd
from math import sqrt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import neighbors
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import numpy as np

raw_data = pd.read_csv("../../datasets/final/df_combined.csv",sep=",")
data = raw_data.drop(raw_data.index[0])

#converting to floating point integers
data["total_crimes"] = data["total_crimes"].astype(float)
data["total_volume_of_tweets"] = data["total_volume_of_tweets"].astype(float)
data["sent_negatives"] = data["sent_negatives"].astype(float)
data["sent_positives"] = data["sent_positives"].astype(float)
data["financial_crimes"] = data["financial_crimes"].astype(float)
data["gold_change"] = data["gold_change"].astype(float)
data["bitcoin_close_change"] = data[["bitcoin_close_change"]].astype(float)

X = data[["total_crimes", "total_volume_of_tweets", "sent_negatives", "sent_positives", \
"financial_crimes","gold_change"]]
y = data[["bitcoin_close_change"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
regr = LinearRegression().fit(X_train, y_train)

print('Coefficients:')
print(regr.coef_)
# Use the model to predict y from X_test
y_pred = regr.predict(X_test)
# Root mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
# R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_test, y_pred))
