    ## Import necessary library
import pandas as pd # For data manipulation
from datetime import datetime, date, timedelta # For comparing dates

# Reading each dataframe from its respective csv file
df_gold = pd.read_csv("../../datasets/modified/gold_mod.csv", index_col = False)

# Reversing the order such that the row are in chronological order
df_gold = df_gold[::-1]
df_gold = df_gold.reset_index(drop = True) # Re-ordering the indices


    ## Ensuring that each day exists and dealing with missing dates

'''
Creating a function that returns a time object given a string of the date in the format
"YYYY-MM-DD"
'''
def string_to_date(date_string):
    date_splitted = date_string.split("-")
    year, month, day = date_splitted
    return date(year = int(year) , month = int(month), day = int(day))

one_day = timedelta(days = 1) # Finding time between days 

# Initialising a new dataframe with the same columns
df_gold_complete = pd.DataFrame(columns = ["date", "value"])

# Iterating through the date column in the gold dataframe
for i in range(len(df_gold["date"])):
    # Retrieving the date at index i as a date object
    current_date = string_to_date(df_gold["date"][i])
    value = df_gold["value"][i] # Retrieving the value at index i
    row_len = df_gold_complete.shape[0] # Finding the updated number of rows in the new dataframe
    
    '''
    If not at the first date, compare the difference
    between the current and previous date
    '''
    if i != 0:
        while (current_date - prev_date).days != 1: # While there are missing dates
            next_day = prev_date + one_day # Increment the next day one more than the previous day
            
            df_gold_complete.loc[row_len] = [next_day, prev_value] # Add this to the dataframe
            
            prev_date = next_day # Update the previous day
            row_len = df_gold_complete.shape[0] # Update the row length variable
    
    df_gold_complete.loc[row_len] = [current_date, value]
    prev_date = current_date # Update the previous day to the current day
    prev_value = value # Update the previous value to the current value
        
# Testing
print(df_gold)
print(df_gold_complete)
print(df_gold_complete.dtypes)

df_gold_complete.to_csv("../../datasets/modified/gold_mod.csv", index = None)
