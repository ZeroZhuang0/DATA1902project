    ## Import necessary library
import pandas as pd # For data manipulation 

# Reading the bitcoin dataset from its respective csv file
df_bitcoin_tweets = pd.read_csv("../../datasets/modified/bitcoin_tweets_mod.csv", index_col = False)

'''
Changing the types of each column to an appropriate type for computation.

Replacing each comma in the bitcoin tweets dataframe to a decimal point
and converting each value except for the dates to a float.
'''
for col in df_bitcoin_tweets.columns[1:16]:
    df_bitcoin_tweets[col] = df_bitcoin_tweets[col].apply(lambda x: float(str(x).replace(',','.')))

    ## Aggregating each day into one row for the bitcoin tweets dataframe

# Creating a weighted compound score based on the total volume of tweets in that hour
df_bitcoin_tweets["compound_score_weighted"] = df_bitcoin_tweets["compound_score"] * df_bitcoin_tweets["total_volume_of_tweets"]

# Creating a new aggregated bitcoin tweets dataframe so that each date is a unique day
df_bitcoin_tweets_agg = df_bitcoin_tweets.groupby("date", as_index = False)["compound_score_weighted"].sum()

# Adding a new column to the aggregated bitcoin dataframe for the total number of tweets in each day
df_bitcoin_tweets_agg["total_volume_of_tweets"] = df_bitcoin_tweets.groupby("date", as_index = False)["total_volume_of_tweets"].sum().iloc[:,1]

# Dividing the weighted compound score by the total volume of tweets in each day
df_bitcoin_tweets_agg["compound_score_weighted"] = df_bitcoin_tweets_agg["compound_score_weighted"]/df_bitcoin_tweets_agg["total_volume_of_tweets"]

# Adding the sum of particular columns
for i in [3, 4, 5, 8, 9, 14, 15]:
    col = df_bitcoin_tweets.columns[i] # Retrieving the column to aggregate on
    # Inserting the summed column to the aggregated dataframe
    df_bitcoin_tweets_agg[col] = df_bitcoin_tweets.groupby("date", as_index = False)[col].sum().iloc[:,1]

# Taking the mean of the columns "sent_negatives" and "sent_positives"
for i in [6, 7]:
    col = df_bitcoin_tweets.columns[i] # Retrieving the column to aggregate on
    # Inserting the aggregated column to the aggregated bitcoin dataframe
    df_bitcoin_tweets_agg.insert(i, col, 
            df_bitcoin_tweets.groupby("date", as_index = False)[col].mean().iloc[:,1])

# Creating a column for the opening price
df_bitcoin_tweets_agg.insert(10, "open", df_bitcoin_tweets.groupby("date", as_index = False)["open"].first().iloc[:,1])

# Creating a column for the highest price
df_bitcoin_tweets_agg.insert(11, "high", df_bitcoin_tweets.groupby("date", as_index = False)["high"].max().iloc[:,1])

# Creating a column for the lowest price
df_bitcoin_tweets_agg.insert(12, "low", df_bitcoin_tweets.groupby("date", as_index = False)["low"].min().iloc[:,1])

# Creating a column for the closing price
df_bitcoin_tweets_agg.insert(13, "close", df_bitcoin_tweets.groupby("date", as_index = False)["close"].last().iloc[:,1])

# Changing the types of each column to their appropriate type
convert_dict = {"date": str,
                "compound_score_weighted": float,
                "total_volume_of_tweets": int,
                "count_negatives": int,
                "count_positives": int,
                "count_neutrals": int,
                "sent_negatives": float,
                "sent_positives": float,
                "count_news": int,
                "count_bots": int,
                "open": float,
                "high": float,
                "low": float,
                "close": float,
                "volume_btc": float,
                "volume_currency": float}
df_bitcoin_tweets_agg = df_bitcoin_tweets_agg.astype(convert_dict)

# Testing
print(df_bitcoin_tweets_agg.dtypes)
print(df_bitcoin_tweets_agg)

# Writing the aggregated dataset to a readable csv file
df_bitcoin_tweets_agg.to_csv("../../datasets/aggregated/bitcoin_tweets_agg.csv", index = None)
