import pandas as pd 
df=pd.read_excel("group_results.xlsx")
df = df.drop("Entry", axis=1)
print(df)
print(df.describe())