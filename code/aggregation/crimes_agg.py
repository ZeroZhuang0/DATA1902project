    ## Import necessary library
import pandas as pd # For data manipulation

# Reading the bitcoin dataset from its respective csv file
df_chicago_crimes = pd.read_csv("../../datasets/modified/chicago_crimes_mod.csv", index_col = False,
        error_bad_lines = False, dtype = "unicode")

# Changing the type of all boolean columns from string to boolean
df_chicago_crimes = df_chicago_crimes.replace({"true": True, "false": False})

# Changing two columns to float for computation
df_chicago_crimes = df_chicago_crimes.astype({"latitude": float,
                                            "longitude": float})

    ## Aggregating each day into one row for the Chicago crimes dataframe

# Counting the number of crimes for each day and renaming it "total_crimes"
df_chicago_crimes_agg = df_chicago_crimes.groupby("date", as_index = False)["id"] \
                                        .count().rename(columns = {"id": "total_crimes"})

# Adding a boolean computer related column for the crimes descriptions which contain "COMPUTER"
df_chicago_crimes["computer_related"] = df_chicago_crimes["description"].str.contains("COMPUTER")

# Adding a computer related column for the number of computer related crimes on each day
df_chicago_crimes_agg["computer_related"] = df_chicago_crimes.groupby("date", as_index = False) \
                                                ["computer_related"].sum().iloc[:,1]

# Adding a boolean financial related crime column for the crimes descriptions which contain "FINANCIAL"
df_chicago_crimes["financial_crimes"] = df_chicago_crimes["description"].str.contains("FINANCIAL")

# Adding a computer related column for the number of computer related crimes on each day
df_chicago_crimes_agg["financial_crimes"] = df_chicago_crimes.groupby("date", as_index = False) \
                                                ["financial_crimes"].sum().iloc[:,1]

# Adding a column for the number of arrests and domestic crimes per day
df_chicago_crimes_agg["num_arrests"] = df_chicago_crimes.groupby("date", as_index = False) \
                                                ["arrest"].sum().iloc[:,1]
df_chicago_crimes_agg["num_domestic"] = df_chicago_crimes.groupby("date", as_index = False) \
                                                ["domestic"].sum().iloc[:,1]

# Finding the average location of crime for each day
df_chicago_crimes_agg["avg_latitude"] = df_chicago_crimes.groupby("date", as_index = False) \
                                                ["latitude"].mean().iloc[:,1]
df_chicago_crimes_agg["avg_longitude"] = df_chicago_crimes.groupby("date", as_index = False) \
                                                ["longitude"].mean().iloc[:,1]


# Changing the types of each column to their appropriate type
convert_dict = {"date": str,
                "total_crimes": int,
                "computer_related": int,
                "financial_crimes": int,
                "num_arrests": int,
                "num_domestic": int,
                "avg_latitude": float,
                "avg_longitude": float}
df_chicago_crimes_agg = df_chicago_crimes_agg.astype(convert_dict)

# Testing
print(df_chicago_crimes_agg.dtypes)
print(df_chicago_crimes_agg)

# Writing the aggregated dataset to a readable csv file
df_chicago_crimes_agg.to_csv("../../datasets/aggregated/chicago_crimes_agg.csv", index = None)
