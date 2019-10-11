    ## Import necessary library
import pandas as pd # For data manipulation 
from datetime import datetime, date,timedelta

# Reading each dataframe from its respective csv file
df_gold = pd.read_csv("../../datasets/modified/gold_mod.csv", index_col = False)

# Reversing the order such that the row are in chronological order
df_gold = df_gold[::-1]
df_gold = df_gold.reset_index(drop = True) # Re-ordering the indices


    ## Ensuring that each day exists and dealing with missing dates

# Defining a function that converts a string to a date object
def string_to_date(date_string):
    date_splitted = date_string.split("-")
    year = date_splitted[0]
    month = date_splitted[1]
    day = date_splitted[2] 
    return date(year = int(year) , month = int(month), day = int(day))

i = 0
pre = None # Initialising a flag
result = pd.DataFrame(columns = ["date", "value"])
one_day = timedelta(days = 1)

# Iterating through the dates 
while i < len(df_gold["date"]):
    if pre == None:
        pre = df_gold["date"][i]
        value = df_gold["value"][i]
        result.loc[len(result["date"])] = [pre, value]
        pre = string_to_date(pre)
    
    else:
        current_date = string_to_date(df_gold["date"][i])
        if (current_date - pre).total_seconds() == -86400:
            result.loc[len(result["date"])] = [df_gold["date"][i], df_gold["value"][i]]
            pre = current_date
            value = df_gold["value"][i]
        else:
            pre = pre - one_day
            result.loc[len(result["date"])] = [pre.isoformat(), value]
            pre = pre - one_day
            result.loc[len(result["date"])] = [pre.isoformat(), value]
    i += 1

n = len(df_gold["date"])
result.loc[len(result["date"])] = [df_gold["date"][n-1], df_gold["value"][n-1]]

# Testing
print(df_gold)
print(result)

    
    ## Changing the types of each column to an appropriate type for computation.
df_gold["value"] = pd.to_numeric(df_gold["value"]) # Value column in gold to numeric
