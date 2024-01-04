import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    lows = []
    dates = []
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha=0.5)
ax.plot(dates, lows, c = 'blue', alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures, 2018", fontsize=20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temp (f)", fontsize= 16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

