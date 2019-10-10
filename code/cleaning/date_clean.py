    ## Importing necessary libraries
import pandas as pd # For data manipulation
import time # For comparing dates

# Reading each dataframe from its original csv file 
df_gold = pd.read_csv('datasets/gold.csv', index_col = False)
df_boston_crimes = pd.read_csv('datasets/boston_crimes.csv', index_col = False,
        error_bad_lines = False, dtype = "unicode")
df_bitcoin_tweets = pd.read_csv('datasets/bitcoin_tweets.csv', sep = ";", index_col = False)

df_boston_crimes = df_boston_crimes.iloc[:-4] # Removing the final 4 lines since they are invalid

    ## Creating a common date format between the datasets

# Extracting the date column from each dataframe
date_gold = df_gold["Date"]
date_boston_crimes = df_boston_crimes["Date"]
date_bitcoin_tweets = df_bitcoin_tweets["Date"]

'''
Changing the date format in the Boston crimes data frame 
from MM/DD/YYYY HH:MM:SS AM/PM to YYYY-MM-DD 
which is the ISO 8601 standard 
'''
new_dates = [] # Creating an empty list to store the new date format
for date_string in date_boston_crimes:
    splitted = str(date_string).split()
    splitted = splitted[0].split("/")
    
    month, day, year = splitted
    splitted[0] = year
    splitted[1] = month
    splitted[2] = day
    
    new_dates.append("-".join(splitted)) # Appending the new date string to the list

date_boston_crimes = pd.Series(new_dates) # Turning the formatted date list into a pandas Series
df_boston_crimes["Date"] = date_boston_crimes # Changing date column to the new format

# Removing the time from the dates in the bitcoin tweets data frame
new_dates = [] # Creating an empty list to store the new date format
for date_string in date_bitcoin_tweets:
    date_string = date_string.split()
    new_dates.append(date_string[0]) # Appending only the date and ignoring the time

date_bitcoin_tweets = pd.Series(new_dates) # Turning the formatted date list into a pandas Series
df_bitcoin_tweets["Date"] = date_bitcoin_tweets # Changing date column to the new format

'''
Creating a function that returns a time object given a string of the date in the format
"YYYY-MM-DD"
'''
def getDate(string):
    return time.strptime(string, "%Y-%m-%d")

# Initialising with default values
oldest_date = getDate("0001-01-01") # An arbitrary old date
newest_date = getDate("3000-01-01") # An arbitrary date in the future

# Iterating through the three date series
for date_series in [date_gold, date_boston_crimes, date_bitcoin_tweets]:

    # Initialising with default values by taking the first value Series
    old_date = getDate(date_series[0])
    new_date = getDate(date_series[0])
    
    # Iterating through each date in the Series
    for date in date_series:
        date = getDate(date) # Extracting the date object

        # Finding the oldest and newest dates in the Series
        if date < old_date:
            old_date = date
        elif date > new_date:
            new_date = date
    
    '''
    Finding the most recent old date and the oldest new date 
    in order to restrict all datasets to common dates
    '''
    if old_date > oldest_date:
        oldest_date = old_date
    if new_date < newest_date:
        newest_date = new_date

# Function that returns a datasets containing only the rows restricted to the common date range
def setNewDates(df):
    new_dates = [] # Declaring an empty list to hold the new dates
    
    # Iterating through each date in the "Date" column
    for date in df["Date"]: 
        date = getDate(date) # Retrieving the date object
        if date >= oldest_date and date <= newest_date: # If the date is within the bounds
            date_string = time.strftime("%Y-%m-%d", date) # Extract the date as a string
            new_dates.append(date_string) # Append the date_string to the new dates list
    
    '''
    Restricting the rows to only those for which the "Date" column
    contains the values in the new dates list
    '''
    df = df[df["Date"].isin(new_dates)]
    return df

# Restricting each dataset to their common date range
for df in [df_gold, df_boston_crimes, df_bitcoin_tweets]:
    df = setNewDates(df)

# Removing the last 8 columns due to redundancy
df_boston_crimes = df_boston_crimes.drop(df_boston_crimes.iloc[:, 22:30], axis = 1)

# Function that turns all column names in a df to lowercase
def column_names_tolower(df):
    df.columns = map(str.lower, df.columns)

# Iterating through each dataset to make lowercase each column name 
for df in [df_gold, df_boston_crimes, df_bitcoin_tweets]:
    column_names_tolower(df)

# Renaming column names to snakecase
df_boston_crimes = df_boston_crimes.rename(columns = {
    "case number":"case_number",
    "primary type":"primary_type",
    "location description":"location_description",
    "community area":"community_area",
    "fbi code":"fbi_code",
    "x coordinate":"x_coordinate",
    "y coordinate":"y_coordinate",
    "updated on":"updated_on"})
        
df_bitcoin_tweets = df_bitcoin_tweets.rename(columns = {
    "total volume of tweets":"total_volume_of_tweets",
    "volume (btc)":"volume_btc",
    "volume (currency)":"volume_currency"})

# Testing
print(df_gold.head())
print(df_boston_crimes.head())
print(df_bitcoin_tweets.head())

df_gold.to_csv("datasets/modified/gold_mod.csv", index = None)
df_boston_crimes.to_csv("datasets/modified/boston_crimes_mod.csv", index = None)
df_bitcoin_tweets.to_csv("datasets/modified/bitcoin_tweets_mod.csv", index = None)
