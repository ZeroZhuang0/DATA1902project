    ## Importing necessary modules and libraries
import checks_clean as clean # For cleaning checks
import pandas as pd # For working with the datasets

# Reading each dataframe from modified csv files
df_gold = pd.read_csv("../../datasets/aggregated/gold_agg.csv", index_col = False)
df_chicago_crimes = pd.read_csv("../../datasets/aggregated/chicago_crimes_agg.csv", index_col = False)
df_bitcoin_tweets = pd.read_csv("../../datasets/aggregated/bitcoin_tweets_agg.csv", index_col = False)

df_list = [df_gold, df_chicago_crimes, df_bitcoin_tweets] # List of dfs for later use

    ## Checking types of each column

clean.check_type(df_gold["date"], str)
clean.check_type(df_gold["value"], float)
clean.check_type(df_gold["gold_change"], float)

clean.check_type(df_chicago_crimes["date"], str)
clean.check_type(df_chicago_crimes["total_crimes"], int)
clean.check_type(df_chicago_crimes["computer_related"], int)
clean.check_type(df_chicago_crimes["financial_crimes"], int)
clean.check_type(df_chicago_crimes["num_arrests"], int)
clean.check_type(df_chicago_crimes["num_domestic"], int)
clean.check_type(df_chicago_crimes["avg_latitude"], float)
clean.check_type(df_chicago_crimes["avg_longitude"], float)

clean.check_type(df_bitcoin_tweets["date"], str)
for col in list(df_bitcoin_tweets.columns[i] for i in [1, 6, 7, 10, 11, 12, 13, 14, 15, 16]):
    clean.check_type(df_bitcoin_tweets[col], float)
for col in list(df_bitcoin_tweets.columns[i] for i in [2, 3, 4, 5, 8, 9]):
    clean.check_type(df_bitcoin_tweets[col], int)

for df in df_list:
    clean.check_date(df["date"])

# Retrieving necessary columns for checking the columns sum correctly
total = df_bitcoin_tweets["total_volume_of_tweets"]
positive = df_bitcoin_tweets["count_positives"]
negative = df_bitcoin_tweets["count_negatives"]
neutral = df_bitcoin_tweets["count_neutrals"]
bots = df_bitcoin_tweets["count_bots"]

error, bad_rows = clean.check_tweets(total, positive, negative, neutral, bots)

# If the error is small change the wrong columns
if error < 3:
    for i in range(len(df_bitcoin_tweets["total_volume_of_tweets"])):
        if i in bad_rows:
            df_bitcoin_tweets.iloc[i, 2] = \
            df_bitcoin_tweets.iloc[i, 3] + \
            df_bitcoin_tweets.iloc[i, 4] + \
            df_bitcoin_tweets.iloc[i, 5]+ \
            df_bitcoin_tweets.iloc[i, 9]
            print("Row {} changed successfully".format(i))

# Checking again now that cells have been changed accordingly
total = df_bitcoin_tweets["total_volume_of_tweets"]
positive = df_bitcoin_tweets["count_positives"]
negative = df_bitcoin_tweets["count_negatives"]
neutral = df_bitcoin_tweets["count_neutrals"]
bots = df_bitcoin_tweets["count_bots"]

clean.check_tweets(total, positive, negative, neutral, bots)


# Checking if certain columns are larger than 0

for col in list(df_bitcoin_tweets.columns[i] for i in [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16]):
    clean.check_greater_than_zero(df_bitcoin_tweets[col])

for col in list(df_chicago_crimes.columns[i] for i in range(1,6)):
    clean.check_greater_than_zero(df_chicago_crimes[col])

clean.check_greater_than_zero(df_gold["value"])

# Checking if certain columns are within 1 and -1
for col in list(df_bitcoin_tweets.columns[i] for i in [1, 6, 7]):
    clean.abs_less_than_one(df_bitcoin_tweets[col])

# Checking the gold price
clean.check_gold_price(df_gold["value"])

# Checking the bitcoin price
for col in list(df_bitcoin_tweets.columns[i] for i in range(10, 14)):
    clean.check_bitcoin_price(df_bitcoin_tweets[col])

# Checking the range of latitude and longitude is correct
clean.check_latitude(df_chicago_crimes["avg_latitude"])
clean.check_longitude(df_chicago_crimes["avg_longitude"])

# Checking for missing values
clean.check_null(df_gold.iloc[1:,:], "Gold df")
clean.check_null(df_bitcoin_tweets.iloc[1:,:], "Bitcoin tweets df")
clean.check_null(df_chicago_crimes, "Chicago crimes df")

# Checking all dates are used
for df in df_list:
    clean.check_no_missing_days(df["date"])

# Writing the dataframe to their respective files
df_gold.to_csv("../../datasets/final/gold_final.csv", index = None)
df_chicago_crimes.to_csv("../../datasets/final/chicago_crimes_final.csv", index = None)
df_bitcoin_tweets.to_csv("../../datasets/final/bitcoin_tweets_final.csv", index = None)
