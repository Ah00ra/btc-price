import matplotlib.pyplot as plt
import mysql.connector

# read data from the database and save a chart as JEPG
cnx = mysql.connector.connect(user='root', password='root', database='test')

query = ("SELECT * FROM btc")

cursor = cnx.cursor()
cursor.execute(query)

prices = []
dates = []

for price, date in cursor:
    prices.append(price), dates.append(date)

cnx.close()
cursor.close()

# create chart and insert data.
plt.title('BTC price chart')
plt.xlabel("date")
plt.ylabel('prices')

plt.grid(True)
plt.plot(dates, prices, 'bo--', linewidth=2, markersize=10)

fig = plt.gcf()
fig.set_size_inches((19, 10))

# Increasing the DPI helps you get a large figure, except format like PNG which doesn't know about inches.
fig.savefig('./btc-chart.jpg', bbox_inches='tight')

