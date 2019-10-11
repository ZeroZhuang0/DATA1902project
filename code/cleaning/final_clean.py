    ## Importing necessary modules and libraries
import checks_clean # For cleaning checks
import pandas as pd # For working with the datasets

# Reading each dataframe from modified csv files 
df_gold = pd.read_csv("../../datasets/modified/gold_mod.csv", index_col = False)
df_boston_crimes = pd.read_csv("../../datasets/modified/boston_crimes_agg.csv", index_col = False)
df_bitcoin_tweets = pd.read_csv("../../datasets/modified/bitcoin_tweets_agg.csv", index_col = False)
