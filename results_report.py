import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("goalscorers.csv")

profile = ProfileReport(df, title = "International Goalscorers")

profile.to_file('goalscorers_report.html')