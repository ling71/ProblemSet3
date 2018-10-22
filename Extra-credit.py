#!/usr/bin/env python3

import urllib.request
import datetime

timepoint = datetime.datetime.now().strftime("%Y%m%d")
url='https://tidesandcurrents.noaa.gov/api/datagetter?begin_date='+timepoint+'%2000:00&end_date='+timepoint+'&station=8729108&product=water_level&datum=mllw&units=metric&time_zone=lst&application=web_services&format=csv'
data = urllib.request.urlopen(url)
datafile = data.read()
with open('Data.csv', 'wb') as file:
	file.write(datafile)
