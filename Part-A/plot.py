import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt 

sns.set_theme()

path = "part_a.csv"
df = pd.read_csv(path, delimiter = ";")

mask = df["rssi"] <= 0

ax = sns.lineplot(
    x = df["report"], 
    y = df["rssi"][mask],
)

print(df["rssi"][mask].describe())

ax.set(
    xlabel = "Time (s)", 
    ylabel = "RSRP (dBm)", 
    title = "RSRP Variation over the path"
)

plt.savefig("plots/part_a.jpg", dpi = 150)
