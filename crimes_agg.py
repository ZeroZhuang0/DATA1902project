    ## Import necessary library
import pandas as pd # For data manipulation 

# Reading the bitcoin dataset from its respective csv file
df_boston_crimes = pd.read_csv('datasets/modified/boston_crimes_mod.csv', index_col = False,
        error_bad_lines = False, dtype = "unicode")
