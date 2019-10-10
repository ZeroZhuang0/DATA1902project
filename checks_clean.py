def check_type(column, type): #checks whether values in column have correct type
    i = 1
    no_error = True
    for value in column:
        if type(value) != type:
            print('Expected type: {}'.format(type))
            print('Row: {}'.format(i))
            print('Value: {}'.format(value))
            print()
            no_error = False
        i += 1
    if no_error:
        print('{} column has correct type {}.'.format(column.name, type))

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

def check_tweets(total, positive, negative, neutral): #checks whether total tweets is equal to sum of positive, negative and neutral tweets
    i = 1
    no_errors = True
    while i < len(total):
        if total[i] != positive[i] + negative[i] + neutral[i]:
            print("Total number of tweets in row {} doesn't add up.".format(i))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('Number of tweets in each row add up')

def check_greater_than_zero(column): #check if values are positive
    no_errors = True
    i = 1
    for value in column:
        if value < 0:
            print('Row {} in {} column has negative value.'.format(i, column.name))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All values in {} column are positive'.format(column.name))

def less_than_one(column): #check if values are between -1 and 1
    no_errors =  True
    i = 1
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
    i = 1
    for value in column:
        if value > 2000:
            print('Gold price {} in row {} is too large.'.format(value, i))
            print()
            no_errors = False
        i += 1
    if no_errors:
        print('All gold prices are in correct range.')
