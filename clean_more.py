import pandas as pd
import time

df_gold = pd.read_csv('datasets/modified/gold_mod.csv', index_col = False)
df_boston_crimes = pd.read_csv('datasets/modified/boston_crimes_mod.csv', index_col = False,
        error_bad_lines = False, dtype = "unicode")
df_bitcoin_tweets = pd.read_csv('datasets/modified/bitcoin_tweets_mod.csv', index_col = False)

# Changing the types of each column to an appropriate type
df_gold["value"] = pd.to_numeric(df_gold["value"])

for col in df_bitcoin_tweets.columns[1:16]:
    df_bitcoin_tweets[col] = df_bitcoin_tweets[col].apply(lambda x: float(str(x).replace(',','.')))

print(df_bitcoin_tweets.columns.to_series().groupby(df_bitcoin_tweets.dtypes).groups)

## Aggregating each day into one row for the bitcoin tweets dataframe
df_bitcoin_tweets["compound_score_weighted"] = df_bitcoin_tweets.compound_score * df_bitcoin_tweets.total_volume_of_tweets

df_bitcoin_tweets_agg = df_bitcoin_tweets.groupby("date", as_index = False)["compound_score_weighted"].mean()

df_bitcoin_tweets_agg["total_volume_of_tweets"] = df_bitcoin_tweets.groupby("date", as_index = False)["total_volume_of_tweets"].sum().iloc[:,1]

df_bitcoin_tweets_agg["compound_score_weighted"] = df_bitcoin_tweets_agg["compound_score_weighted"]/df_bitcoin_tweets_agg["total_volume_of_tweets"]

# Summing up columns
for i in [3, 4, 5, 8, 9, 14, 15]:
    col = df_bitcoin_tweets.columns[i]
    df_bitcoin_tweets_agg[col] = df_bitcoin_tweets.groupby("date", as_index = False)[col].sum().iloc[:,1]

# Taking the mean of the columns "sent_negatives" and "sent_positives"
for i in [6, 7]:
    col = df_bitcoin_tweets.columns[i]
    df_bitcoin_tweets_agg.insert(i, col, df_bitcoin_tweets.groupby("date", as_index = False)[col].mean().iloc[:,1])

# Creating a column for the open price
df_bitcoin_tweets_agg.insert(10, "open", df_bitcoin_tweets.groupby("date", as_index = False)["open"].first().iloc[:,1])

# Creating a column for the closing price
df_bitcoin_tweets_agg.insert(11, "close", df_bitcoin_tweets.groupby("date", as_index = False)["close"].last().iloc[:,1])

# Creating a column for the highest price
df_bitcoin_tweets_agg.insert(12, "high", df_bitcoin_tweets.groupby("date", as_index = False)["high"].max().iloc[:,1])

# Creating a column for the lowest price
df_bitcoin_tweets_agg.insert(13, "low", df_bitcoin_tweets.groupby("date", as_index = False)["low"].min().iloc[:,1])

# Testing
print(df_bitcoin_tweets_agg.columns)
print(df_bitcoin_tweets_agg)

df_bitcoin_tweets_agg.to_csv("datasets/aggregated/bitcoin_tweets_agg.csv", index = None)
