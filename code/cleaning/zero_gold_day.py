import csv
import pandas as pd
from datetime import datetime, date,timedelta
df = pd.read_csv("https://raw.githubusercontent.com/ZeroZhuang0/DATA1902project/master/datasets/gold.csv")
def string_to_date(s):
  year=s.split("-")[0]
  month=s.split("-")[1]
  day=s.split("-")[2] 
  return date(year = int(year) , month = int(month), day = int(day))
i=0
pre=None
result = pd.DataFrame(columns=["Date","Value"])
one_day=timedelta(days=1)
while i < len(df["Date"]):
  if pre == None:
    pre=df["Date"][i]
    value=df["Value"][i]
    result.loc[len(result['Date'])]=[pre,value]
    pre=string_to_date(df["Date"][i])
  else:
    current_date=string_to_date(df["Date"][i])
    if(current_date-pre).total_seconds()==-86400:
      result.loc[len(result['Date'])]=[df["Date"][i],df["Value"][i]]
      pre=current_date
      value=df["Value"][i]
    else:
      pre=pre-one_day
      result.loc[len(result['Date'])]=[pre.isoformat(),value]
      pre=pre-one_day
      result.loc[len(result['Date'])]=[pre.isoformat(),value]
  i+=1
n=len(df["Date"])
result.loc[len(result['Date'])]=[df["Date"][n-1],df["Value"][n-1]]
result2 = pd.DataFrame(columns=["Date","Value"])
j=0
while j< len(result["Date"]):
  result2.loc[(len(result["Date"])-j)]=[result["Date"][j],result["Value"][j]]
  j+=1
result2=result2.iloc[::-1]
print(result2)



#-----------------------------------------------------------------------------------------


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
