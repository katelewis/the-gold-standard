#!/usr/bin/python
import csv
import glob
import os
import sys
import datetime
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


r_cols = ["Trans","CarPark","EntryDevice","EntryDateTime","ExitDevice","ExitDateTime","Datetimeoflastpayment","Devicenumbercellentry","Datetimecellentry","Devicenumbercellexit","Datetimeofcellexit","Misuse","Tickettype","SKIDATA","Article","FirstUse","Invoice","DateofProduction","CCNumber","CCCompany","Facility","E1","E2","E3","E4","E5","E6","E7"]

print('loading data')
df = pd.read_csv(sys.argv[1], header=None, names=r_cols)

print('convert to date time values')
df[['EntryDateTime']] = df[['EntryDateTime']].applymap( lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
df[['ExitDateTime']] = df[['ExitDateTime']].applymap( lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

dates = (pd.DatetimeIndex(df["ExitDateTime"].tolist()))

print('getting entry day of week')
df['day_of_week'] = df['EntryDateTime'].dt.dayofweek 

print('removing bad data')
df = df[dates.year != 1994]

print('calculating duration')
df['duration'] = df['ExitDateTime'] - df['EntryDateTime']

dates = matplotlib.dates.date2num(df['EntryDateTime'].tolist())
# duration = matplotlib.dates.date2num(df['duration'].tolist())
#dates = df['EntryDateTime'].tolist()
df[['entry_hour']] = df[['EntryDateTime']].applymap(lambda x: x.hour)

df[['duration_hour']] = df[['duration']].applymap(lambda x: (x.total_seconds() // 3600) % 24)
df[['duration_minutes']] = df[['duration']].applymap(lambda x: (x.total_seconds() // 60) % 60)

df[['duration']] =df[['duration']].applymap(lambda x: ((x.total_seconds() // 3600) % 24)*60 + (x.total_seconds() // 60) % 60) 
df[['ones']] = df[['duration']].applymap(lambda x: 1)


#  duration 29
#  entry hour 39
row = next(df.iterrows())
while(row):
	print(row[1][29], row[1][30])
	row = next(df.iterrows())


# counts = df.groupby(['entry_hour','duration']).count()
# print(counts)


# counts.plot.scatter(x='entry_hour', y='duration', c='ones')

# counts = df.pivot_table(values=['ones'], index = ['entry_hour', 'duration'], aggfunc=np.sum)

# t = counts.unstack(level=0)


# print(t[[0]])
# plt.plot(t[[0]], color='red')
# plt.plot(t[[1]], color='blue')
# plt.plot(t[[2]], color='orange')
# plt.show()
# for i in counts.index.get_level_values(0).unique():
# 	temp = counts.xs(i, level=0)
# 	print(temp.keys)
# fig = plt.figure()

# ax = fig.add_subplot(1,1,1)

