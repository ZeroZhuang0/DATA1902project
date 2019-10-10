    ## Import necessary library
import pandas as pd # For data manipulation 

# Reading each dataframe from its respective csv file
df_gold = pd.read_csv('datasets/modified/gold_mod.csv', index_col = False)



    ## Changing the types of each column to an appropriate type for computation.

df_gold["value"] = pd.to_numeric(df_gold["value"]) # Value column in gold to numeric

