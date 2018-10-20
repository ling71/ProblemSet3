#!/usr/bin/env python3

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
