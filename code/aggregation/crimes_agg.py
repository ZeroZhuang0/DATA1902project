    ## Import necessary library
import pandas as pd # For data manipulation 

# Reading the bitcoin dataset from its respective csv file
df_boston_crimes = pd.read_csv("../../datasets/modified/boston_crimes_mod.csv", index_col = False,
        error_bad_lines = False, dtype = "unicode")

# Changing the type of all boolean columns from string to boolean
df_boston_crimes = df_boston_crimes.replace({"true": True, "false": False})


    ## Aggregating each day into one row for the Boston crimes dataframe

# Counting the number of crimes for each day and renaming it "total_crimes"
df_boston_crimes_agg = df_boston_crimes.groupby("date", as_index = False)["id"] \
                                        .count().rename(columns = {"id":"total_crimes"})

# Adding a boolean computer related column for the crimes descriptions which contain "COMPUTER"
df_boston_crimes["computer_related"] = df_boston_crimes["description"].str.contains("COMPUTER")

# Adding a computer related column for the number of computer related crimes on each day
df_boston_crimes_agg["computer_related"] = df_boston_crimes.groupby("date", as_index = False)["computer_related"].sum().iloc[:,1]

# Adding a column for the number of arrests and domestic crimes per day
df_boston_crimes_agg["num_arrests"] = df_boston_crimes.groupby("date", as_index = False)["arrest"].sum().iloc[:,1]
df_boston_crimes_agg["num_domestic"] = df_boston_crimes.groupby("date", as_index = False)["domestic"].sum().iloc[:,1]

# Changing the types of each column to their appropriate type
convert_dict = {"date": str,
                "total_crimes": int,
                "computer_related": int,
                "num_arrests": int,
                "num_domestic": int}
df_boston_crimes_agg = df_boston_crimes_agg.astype(convert_dict)

# Testing
print(df_boston_crimes_agg.dtypes)
print(df_boston_crimes_agg)

# Writing the aggregated dataset to a readable csv file
df_boston_crimes_agg.to_csv("../../datasets/aggregated/boston_crimes_agg.csv", index = None)
