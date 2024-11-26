# Monday 18th November 2024 

# ---- Activity 1 ---- Create a dateframe to store information on the planets of the solar system ----

import pandas as pd

# names = pd.DataFrame(["Earth", "Jupiter", "Saturn", "Mercury", "Venus", "Mars", "Neptune", "Uranus"])
# average_temp = pd.DataFrame([15, -110, -140, 167, 464, -65, -200, -195])
# radius_km = pd.DataFrame([6371, 69911, 58232, 2440, 6052, 3390, 24622, 25362])
# colour = pd.DataFrame(["Blue", "Beige", "Cream", "Grey", "Golden Brown", "Red", "Blue", "Cyan"])
# interesting_features = pd.DataFrame(["You can see Earth's magnetic field at work during light shows.", "Jupiter is a great comet catcher.", "No one knows how old Saturn’s rings are.", "Mercury is hot, but not too hot for ice.", "Venus doesn’t have any moons.", "Mars had a thicker atmosphere in the past.", "Neptune has supersonic winds.", "Uranus is more stormy than we thought."])

# df = pd.concat([names, average_temp, radius_km, colour, interesting_features], axis = 1)
# df.columns = ["Names", "Average Temp", "Radius in KM", "Colour", "Interesting Features"]

# print(df)

# df.insert(3, "Elements of its composition", ["Rock", "Gas", "Gas", "Rock", "Rock", "Rock", "Gas", "Gas"])
# print(df)

# Tuesday 19th November 2024

# ---- Activity 1 ----

df = pd.read_csv("results.csv")

# print(df["tournament"].value_counts())

# Friendly                                17773
# FIFA World Cup qualification             8016
# UEFA Euro qualification                  2815
# African Cup of Nations qualification     1998
# FIFA World Cup                            964
#                                         ...
# FIFA 75th Anniversary Cup                   1
# Real Madrid 75th Anniversary Cup            1
# TIFOCO Tournament                           1
# The Other Final                             1
# Copa Confraternidad                         1

# print(df["home_team"].mode())
# Brazil

# print(df["away_team"].mode())
# Uruguay

print(df.sort_values(by=["home_team"]))

