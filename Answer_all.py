#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

#Question 1
data = open('CO-OPS__8729108__wl.csv')
part_1 = data.readlines()[1:424]
data = open('CO-OPS__8729108__wl.csv')
part_2 = data.readlines()[425:]
data_merged = part_1 + part_2

water_level_list = []
for line in data_merged:
    delimiter = ','
    water_level = line.split(delimiter)
    floats=float(water_level[1])
    water_level_list.append(floats)

largest = None
for i in water_level_list:
    if largest is None or i > largest:
        largest = i
print('Highest_Water_Level',largest)

for line in data_merged:
    if line.find(str(largest)) == -1: continue
    delimiter = ','
    date_time = line.split(delimiter)
print('Date_time',date_time[0])


#Question 2
df = pd.read_csv("CO-OPS__8729108__wl.csv")
df = df.rename(columns=lambda x: x.replace(" ",""))
print('Highest_Water_Level',df['WaterLevel'].max())
print ('Date_Time',df.ix[df.WaterLevel.idxmax(), 'DateTime'])


#Question 3
df = pd.read_csv("CO-OPS__8729108__wl.csv")
df = df.rename(columns=lambda x: x.replace(" ",""))
df['Difference'] = df['WaterLevel'] - df['WaterLevel'].shift(+1)
print ('Highest_Rise',df.Difference.max().round(3))
Line_Number = df.Difference.idxmax()
print('Date_Time_Before_Rise',df.ix[Line_Number-1,[0]].values[0])
print('Water_Level_Before_Rise',round(float(df.ix[Line_Number-1,[1]].values[0]),3))
print ('Date_Time_After_Rise',df.ix[Line_Number,'DateTime'])
print ('Water_Level_After_Rise',df.ix[Line_Number,'WaterLevel'])


#Question 4
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


#Extra-credit-question
import urllib.request
import datetime

timepoint = datetime.datetime.now().strftime("%Y%m%d")
url='https://tidesandcurrents.noaa.gov/api/datagetter?begin_date='+timepoint+'%2000:00&end_date='+timepoint+'&station=8729108&product=water_level&datum=mllw&units=metric&time_zone=lst&application=web_services&format=csv'
data = urllib.request.urlopen(url)
datafile = data.read()
with open('Data.csv', 'wb') as file:
            file.write(datafile)
