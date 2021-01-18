import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt 

sns.set_theme()

path = "measurements.csv"
df = pd.read_csv(path)

print("Unique eNodeBIDs")
print(df["nodeid"].unique())
print("")

mask = df["rssi"] <= 0

print(df["rssi"][mask].describe())