    ## Importing necessary libraries
import pandas as pd # For working with the datasets

# Reading each dataframe from modified csv files 
df_gold = pd.read_csv("../../datasets/final/gold_final.csv", index_col = False)
df_boston_crimes = pd.read_csv("../../datasets/final/boston_crimes_final.csv", index_col = False)
df_bitcoin_tweets = pd.read_csv("../../datasets/final/bitcoin_tweets_final.csv", index_col = False)

# Combining the dataframes on the common column "date"
df_combined = pd.merge(df_bitcoin_tweets, df_gold, on = "date")
df_combined = pd.merge(df_combined, df_boston_crimes, on = "date")

# Renaming the "value" column to "gold_value"
df_combined = df_combined.rename(columns = {"value": "gold_value"})

# Testing
print(df_combined.dtypes)
print(df_combined)

df_combined.to_csv("../../datasets/final/df_combined.csv", index = None)
