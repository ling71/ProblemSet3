#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("CO-OPS__8729108__wl.csv")
df = df.rename(columns=lambda x: x.replace(" ",""))
print('Highest_Water_Level',df['WaterLevel'].max())
print ('Date_Time',df.ix[df.WaterLevel.idxmax(), 'DateTime'])
