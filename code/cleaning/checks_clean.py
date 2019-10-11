from datetime import datetime, date, timedelta # For comparing dates

def check_type(column, t): #checks whether values in column have correct type
    i = 1
    no_error = True
    for value in column:
        if type(value) != t:
            print('Expected type: {}'.format(t))
            print('Actual type: {}'.format(type(value)))
            print('Row: {}'.format(i))
            print('Value: {}'.format(value))
            print()
            no_error = False
        i += 1
    if no_error:
        print('{} column has correct type {}.'.format(column.name, t))

def check_date(column): #checks whether date has correct format
    no_error = True
    for value in column:
        ls = value.split('-')
        if len(ls) != 3: #checks if date has 3 fields
            print("Date doesn't have correct format.")
            print(ls)
            no_error = False
        try:
            ls = [int(x) for x in ls]
        except TypeError:
            print('Date does not have correct type.')
            print(ls)
            print()
            no_error =  False
            continue
        if ls[0] < 2017 or ls[0] > 2019:
            print('Year {} is not correct'.format(ls[0]))
            print()
            no_error =  False
        if ls[1] < 1 or ls[1] > 12:
            print('Month {} is not correct'.format(ls[1]))
            print()
            no_error =  False
        if ls[2] < 1 or ls[2] > 31:
            print('Day {} is not correct'.format(ls[2]))
            print()
            no_error =  False
    if no_error:
        print('All dates have correct format.')

#checks whether total tweets is equal to sum of positive, negative and neutral tweets
def check_tweets(total, positive, negative, neutral, bots): 
    i = 0
    no_errors = True
    largest_error = 0
    bad_rows = []
    while i < len(total):
        expected_sum = positive[i] + negative[i] + neutral[i] + bots[i]
        if total[i] != expected_sum:
            error = abs(expected_sum - total[i])
            if error > largest_error:
                largest_error = error
            print("Total number of tweets for row {} is different by {}".format(i, error))
            bad_rows.append(i)
            no_errors = False
        i += 1
    if no_errors:
        print('Number of tweets in each row add up')
    elif largest_error > 3:
        print("The max error of {} is large. Investigate further.".format(bad_rows))
    return largest_error, bad_rows

def check_greater_than_zero(column): #check if values are positive
    no_errors = True
    i = 0
    for value in column:
        if value < 0:
            print('Row {} in {} column has negative value.'.format(i, column.name))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All values in {} column are positive'.format(column.name))

def check_longitude(column): #check if values are positive
    no_errors = True
    i = 0
    for value in column:
        if value > 180 or value < -180:
            print('Row {} in {} column has wrong longitude value of {}.'.format(i, column.name, value))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All longitude values in {} column within correct range'.format(column.name))

def check_latitude(column): #check if values are positive
    no_errors = True
    i = 0
    for value in column:
        if value > 90 or value < -90:
            print('Row {} in {} column has wrong latitude value of {}.'.format(i, column.name, value))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All latitude values in {} column within correct range'.format(column.name))

def abs_less_than_one(column): #check if values are between -1 and 1
    no_errors =  True
    i = 0
    for value in column:
        if abs(value) > 1:
            print('Value in row {} in {} column is not between -1 and 1.'.format(i, column.name))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All values in column {} are between -1 and 1'.format(column.name))

def check_gold_price(column): #checks if there is a value which is too large
    no_errors =  True
    i = 0
    for value in column:
        if value > 2000:
            print('Gold price {} in row {} is too large.'.format(value, i))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All gold prices are in correct range.')

def check_bitcoin_price(column): #checks if there is a value which is too large
    no_errors =  True
    i = 0
    for value in column:
        if value > 20000: # highest bitcoin price ever recorded around 19800
            print('Bitcoin price {} in row {} is too large.'.format(value, i))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All bitcoin prices are in correct range.')

def check_null(df, name):
    if df.isnull().values.any():
        null_sum = df.isnull().sum()
        print("{} has {} missing values".format(name, null_sum))
    else:
        print("{} has no missing values".format(name))

'''
Creating a function that returns a time object given a string of the date in the format
"YYYY-MM-DD"
'''
def string_to_date(date_string):
    date_splitted = date_string.split("-")
    year, month, day = date_splitted
    return date(year = int(year) , month = int(month), day = int(day))

one_day = timedelta(days = 1) # Finding the time between days 

def check_no_missing_days(date_series):
    no_missing_days = True
    first_day = True
    for date in date_series:
        date = string_to_date(date)
        if first_day:
            prev_day = date
            first_day = False
            continue
        if (date - prev_day).days != 1:
            print("There is/are missing days between {} and {}".format(prev_day, date))
            no_missing_days = False
        prev_day = date
    if no_missing_days:
        print("Success: The df has no missing days")

