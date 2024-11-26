import pandas as pd 

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])

# print(languages)

# numbers = pd.Series([3, 1, 2, 4])

# print(numbers)

# df = pd.DataFrame([("Anne", 30),("Bill", 27),("Charlie", 55)], columns=["Name", "Age"])

# print(df)

# df = pd.DataFrame({
#     "Languages": languages,
#     "Numbers": numbers
# })

# print(df)

# df = pd.concat([languages, numbers], axis = 1)
# df.columns = ["Languages", "Numbers"]

# print(df)

# df = pd.read_csv("speeds.csv")

# print(df)

df = pd.read_excel("speeds.xlsx")

print(df)