import pandas as pd

df = pd.read_csv("spotify_songs.csv")

# print(df)

# print(df.shape)

# coffee_order = ["Alex - Latte", "Ben - Tea", "Charlie - Mocha"]

# print(coffee_order)

# print(df.columns)

# df.info()

# print(df["playlist_genre"].value_counts())

# print(df["playlist_genre"].mode()[0])

# Note: This is a series

# print(df["duration_ms"].mean())

# max_ms = df["duration_ms"].max()
# min_ms = df["duration_ms"].min()
# print(max_ms-min_ms)

# print(df["duration_ms"].sum())

# ---- Sorting ----

# print(df.sort_values(by=["duration_ms"]))

# print(df.sort_values(by=["duration_ms"], ascending=False))

# print(df.groupby('playlist_genre')["duration_ms"].min())
# print(df.groupby('playlist_genre')["duration_ms"].max())

# ---- Queries ----

# print(df.query("track_artist=='Ricky Martin'"))

# mean_val = df["duration_ms"].mean()

# print(df.query("duration_ms > @mean val"))

# print(df.query(f"duration_ms >= {mean_val}"))
