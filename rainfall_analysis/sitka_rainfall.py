import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '../data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)

    rainfalls = []
    dates = []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        rainfall = float(row[3])
        dates.append(date)
        rainfalls.append(rainfall)


fig, ax = plt.subplots()
ax.plot(dates, rainfalls)

plt.title("Sitka rainfall in 2018", fontsize = 20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Amount (ml)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

