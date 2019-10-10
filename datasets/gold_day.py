import csv
import pandas as pd
from datetime import datetime, date,timedelta
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
print(result.tail())
