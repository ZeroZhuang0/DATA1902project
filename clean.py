import pandas as pd
import time

df_gold = pd.read_csv('datasets/gold.csv', index_col = False)
df_boston_crimes = pd.read_csv('datasets/boston_crimes.csv', index_col = False,
        error_bad_lines = False, dtype = "unicode")
df_bitcoin_tweets = pd.read_csv('datasets/bitcoin_tweets.csv', sep = ";", index_col = False)

print("Gold dataset")
print(df_gold.head())

print("\nBoston crimes dataset")
print(df_boston_crimes.head())

print("\nBitcoin tweets dataset")
print(df_bitcoin_tweets.head())

print(df_boston_crimes.tail(4)) # Testing
df_boston_crimes = df_boston_crimes.iloc[:-4] # Removing the final 4 lines since they are invalid

date_gold = df_gold["Date"]
date_boston_crimes = df_boston_crimes["Date"]
date_bitcoin_tweets = df_bitcoin_tweets["Date"]

'''
Changing the date format in the Boston crimes data frame 
from MM/DD/YYYY HH:MM:SS AM/PM to YYYY-MM-DD 
which is the ISO 8601 standard 
'''
new_dates = []
#flag = False
for date_string in date_boston_crimes:
    splitted = str(date_string).split()
    splitted = splitted[0].split("/")
    
    #if str(date_string) == "nan":
    #    continue

    #Testing
    #if flag == True:
    #    print(splitted)
    #    print()
    #    flag = False
    
    # Testing
    #if len(splitted) != 3:
    #    print(prev)
    #    print(splitted)
    #    flag = True
    #    prev = splitted
    #    continue
    
    month, day, year = splitted
    splitted[0] = year
    splitted[1] = month
    splitted[2] = day
    
    new_dates.append("-".join(splitted))
    #prev = splitted #Testing

date_boston_crimes = pd.Series(new_dates)
print(date_boston_crimes.tail()) # Testing

df_boston_crimes["Date"] = date_boston_crimes # Changing date column

# Removing the time from the dates in bitcoin tweets data frame
new_dates = []
for date_string in date_bitcoin_tweets:
    date_string = date_string.split()
    new_dates.append(date_string[0])

date_bitcoin_tweets = pd.Series(new_dates)
print(date_bitcoin_tweets.head()) # Testing

df_bitcoin_tweets["Date"] = date_bitcoin_tweets # Chaning date column

def getDate(string):
    return time.strptime(string, "%Y-%m-%d")

# Initialising with default values
oldest_date = getDate("0001-01-01")
newest_date = getDate("3000-01-01")

for date_series in [date_gold, date_boston_crimes, date_bitcoin_tweets]:
    # Initialising with default values
    old_date = getDate(date_series[0])
    new_date = getDate(date_series[0])
    for date in date_series:
        date = getDate(date)
        if date < old_date:
            old_date = date
        elif date > new_date:
            new_date = date

    #print(time.strftime("%Y-%m-%d", old_date))
    #print(time.strftime("%Y-%m-%d", new_date))
    
    if old_date > oldest_date:
        oldest_date = old_date
    if new_date < newest_date:
        newest_date = new_date

print(time.strftime("%Y-%m-%d", oldest_date))
print(time.strftime("%Y-%m-%d", newest_date))


def setNewDates(df):
    new_dates = []
    for date in df["Date"]:
        date = getDate(date)
        if date >= oldest_date and date <= newest_date:
            date_string = time.strftime("%Y-%m-%d", date)
            new_dates.append(date_string)
    df = df[df["Date"].isin(new_dates)]
    return df

df_gold = setNewDates(df_gold)
df_boston_crimes = setNewDates(df_boston_crimes)
df_bitcoin_tweets = setNewDates(df_bitcoin_tweets)

df_boston_crimes = df_boston_crimes.drop(df_boston_crimes.iloc[:, 22:30], axis = 1)
print(df_boston_crimes.columns)

# Testing
print(df_gold.head())
print(df_boston_crimes.head())
print(df_bitcoin_tweets.head())

df_gold.to_csv("datasets/modified/gold_mod.csv", index = None)
df_boston_crimes.to_csv("datasets/modified/boston_crimes_mod.csv", index = None)
df_bitcoin_tweets.to_csv("datasets/modified/bitcoin_tweets_mod.csv", index = None)
