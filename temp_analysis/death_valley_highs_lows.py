import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    highs = []
    lows = []
    dates = []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {date}")

        highs.append(high)
        lows.append(low)


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
