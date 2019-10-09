import pandas as pd

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

date_gold = df_gold["Date"]
date_boston_crimes = df_boston_crimes["Date"]
date_bitcoin_tweets = df_bitcoin_tweets["Date"]

print(df_boston_crimes.tail())

new_dates = []
flag = False
for date_string in date_boston_crimes:
    splitted = str(date_string).split()
    splitted = splitted[0].split("/")
    
    if flag == True:
        print(splitted)
        print()
        flag = False

    if len(splitted) != 3:
        print(prev)
        print(splitted)
        flag = True
        prev = splitted
        continue

    month, day, year = splitted
    splitted[0] = year
    splitted[1] = month
    splitted[2] = day
    
    new_dates.append("-".join(splitted))
    prev = splitted

date_gold = pd.Series(new_dates)
print(new_dates[0:5])
print(date_gold.head())
