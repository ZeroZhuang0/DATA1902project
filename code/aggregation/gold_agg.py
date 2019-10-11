    ## Import necessary library
import pandas as pd # For data manipulation

# Reading each dataframe from its respective csv file
df_gold = pd.read_csv('datasets/modified/gold_mod.csv', index_col = False)

# Creating a new column the percentage change in gold value for each day
df_gold['gold_change'] = df_gold['value'].pct_change()*100
