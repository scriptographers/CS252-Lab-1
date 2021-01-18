import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt 

sns.set_theme()

path = "part_d.csv"
df = pd.read_csv(path, delimiter = ";")

ax = sns.lineplot(
    x = df["report"], 
    y = df["rssi"],
)

ax.set(
    xlabel = "Time (s)", 
    ylabel = "RSRP (dBm)", 
    title = "RSRP Variation at a Fixed Location"
)

plt.savefig("plots/part_d.jpg", dpi = 150)