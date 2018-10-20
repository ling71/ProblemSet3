#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CO-OPS__8729108__wl.csv")
df = df.rename(columns=lambda x: x.replace(" ",""))
plt.title('Water level observations from Panama City during Hurricane Michael', fontsize=12)
plt.xlabel("Measurement Interval Count (6-min Interval)", fontsize=10)
plt.ylabel('Water Level (Meters)', fontsize=10)
plt.axis([0, 1.1 * len(df.axes[0]), 0, 1.1 * df['WaterLevel'].max()])
counts = df['WaterLevel'].values
plt.scatter(df.index,counts,c =200 * counts, s = 0.5)
plt.show()
plt.savefig("plot.png")
