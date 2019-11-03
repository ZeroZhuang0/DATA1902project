import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split

data = pd.read_csv("../../datasets/final/df_combined.csv")

data["bitcoin_close_change"] = data[["bitcoin_close_change"]].astype(float)
data["gold_change"] = data["gold_change"].astype(float)
data["total_crimes"] = data["total_crimes"].astype(float)
data["total_volume_of_tweets"] = data["total_volume_of_tweets"].astype(float)
data["count_negatives"] = data["count_negatives"].astype(float)
data["count_positives"] = data["count_positives"].astype(float)
data["financial_crimes"] = data["financial_crimes"].astype(float)

X = data[["gold_change", "total_crimes", "total_volume_of_tweets", "count_negatives", "count_positives", "financial_crimes"]]
y = data[["bitcoin_close_change"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
regr = linear_model.LinearRegression().fit(X_train, y_train)

# The coefficients
print('Coefficients:')
print(regr.coef_)
# Use the model to predict y from X_test
y_pred = regr.predict(X_test)
# Root mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
# R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_test, y_pred))
