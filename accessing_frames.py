import pandas as pd

df = pd.read_excel("dev_rankings.xlsx")

print(df)

df = df.set_index("Languages")
print(df["Ranking 2019"])

print(df[["Ranking 2022", "Ranking 2021"]])

print(df.loc["HTML"])

print(df.loc[:,"Ranking 2020"])