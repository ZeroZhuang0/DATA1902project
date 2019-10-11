    ## Importing necessary libraries
import pandas as pd # For working with the datasets

# Reading the combined dataframe 
df_combined = pd.read_csv("../../datasets/final/df_combined.csv", index_col = False)

# Creating a new dataframe with the summary statistics
df_stats = pd.DataFrame(columns = df_combined.columns,
        index = ["max", "min", "sd", "mean", "median", "iqr"])

# Creating the date statistics
df_stats["date"]["max"] = df_combined.iloc[-1, 0]
df_stats["date"]["min"] = df_combined.iloc[0, 0]

# Creating the other statistics
for col in list(df_combined.columns[i] for i in range(1,len(df_combined.columns))):
    df_stats[col]["max"] = df_combined[col].max()
    df_stats[col]["min"] = df_combined[col].min()
    df_stats[col]["sd"] = df_combined[col].std()
    df_stats[col]["mean"] = df_combined[col].mean()
    df_stats[col]["median"] = df_combined[col].median()
    df_stats[col]["iqr"] = df_combined[col].quantile(0.75) - df_combined[col].quantile(0.25)

# Testing
print(df_stats)


# Writing it to a csv file
df_stats.to_csv("../../datasets/final/combined_stats.csv", index = None)
