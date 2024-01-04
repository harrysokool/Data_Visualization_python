import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red')

plt.title("Daily high temperatures, 2018", fontsize=24)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temp (f)", fontsize= 16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

