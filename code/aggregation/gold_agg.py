    ## Import necessary library
import pandas as pd # For data manipulation

# Reading each dataframe from its respective csv file
df_gold_agg = pd.read_csv('../../datasets/modified/gold_mod.csv', index_col = False)

# Creating a new column the percentage change in gold value for each day
df_gold_agg['gold_change'] = df_gold_agg['value'].pct_change() * 100

# Testing
print(df_gold_agg.dtypes)
print(df_gold_agg)

# Writing the changes to the gold csv
df_gold_agg.to_csv("../../datasets/aggregated/gold_agg.csv", index = None)
