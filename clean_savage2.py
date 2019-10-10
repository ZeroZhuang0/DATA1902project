import pandas as pd

df_boston_crimes = pd.read_csv('datasets/modified/boston_crimes_mod.csv', index_col = False,
        error_bad_lines = False, dtype = "unicode")


c = df_boston_crimes['description'].str.contains('COMPUTER')
print(c)

df_boston_crimes['is_computer_related'] = c

df_boston_crimes['arrest'].replace('true', True, True)
df_boston_crimes['arrest'].replace('false', False, True)

df_boston_crimes['domestic'].replace('true', True, True)
df_boston_crimes['domestic'].replace('false', False, True)

df_boston_crimes_agg = df_boston_crimes.groupby("date", as_index = False)["id"].count()
df_boston_crimes_agg["computer_related"] = df_boston_crimes.groupby("date", as_index = False)["is_computer_related"].sum().iloc[:,1]
df_boston_crimes_agg["num_arrests"] = df_boston_crimes.groupby("date", as_index = False)["arrest"].sum().iloc[:,1]
df_boston_crimes_agg["num_domestic"] = df_boston_crimes.groupby("date", as_index = False)["domestic"].sum().iloc[:,1]




df_boston_crimes_agg = df_boston_crimes_agg.rename(columns = {"id":"count"})
df_boston_crimes_agg.to_csv("datasets/aggregated/boston_crimes_agg.csv", index = None)
