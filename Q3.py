#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("CO-OPS__8729108__wl.csv")
df = df.rename(columns=lambda x: x.replace(" ",""))
df['Difference'] = df['WaterLevel'] - df['WaterLevel'].shift(+1)
print ('Highest_Rise',df.Difference.max().round(3))
Line_Number = df.Difference.idxmax()
print('Date_Time_Before_Rise',df.ix[Line_Number-1,[0]].values[0])
print('Water_Level_Before_Rise',round(float(df.ix[Line_Number-1,[1]].values[0]),3))
print ('Date_Time_After_Rise',df.ix[Line_Number,'DateTime'])
print ('Water_Level_After_Rise',df.ix[Line_Number,'WaterLevel'])
