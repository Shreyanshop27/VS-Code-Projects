import csv
import matplotlib.pyplot as plt
from datetime import datetime 


file='Crash Course\Data visualisation\weather_chart\lucknow_weather.csv'
highs,dates,lows=[],[],[]
with open(file) as f:
    read=csv.reader(f)
    head=next(read)

    for row in read:
        date=datetime.strptime(row[2],'%Y-%m-%d')
        high=row[5]
        low=row[6]

        if high:
            high=int(high)
        else:
            high=None
        if low:
            low=int(low)
        else:
            low=None

        dates.append(date)
        highs.append(high)
        lows.append(low)


fig,wchart=plt.subplots()

wchart.plot(dates,highs,c='red',alpha=0.5)
wchart.plot(dates,lows,c='blue',alpha=0.5)


wchart.tick_params(axis='both',which='major')
wchart.set_title("Lucknow Daily Temperature(1 Jan 2020-Now)")
wchart.set_xlabel("Date")
wchart.set_ylabel("Temprature (F)")

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.show()
