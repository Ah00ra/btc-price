import matplotlib.pyplot as plt
import sys
import sqlite3

db_path = sys.argv[1]
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = "SELECT * FROM btc"
cursor.execute(query)
record = cursor.fetchall()
conn.close()

prices = []
dates = []
for price, date in record:
    prices.append(price)
    dates.append(date)

# # create chart and insert data.
plt.title("BTC price chart")
plt.xlabel("date")
plt.ylabel("prices")

plt.grid(True)
plt.plot(dates, prices, "bo--", linewidth=2, markersize=10)

fig = plt.gcf()
# TODO; dynamic figure size instead of fix one
fig.set_size_inches((19, 10))

# Increasing the DPI helps you get a large figure, except format like PNG which doesn't know about inches.
fig.savefig("./btc-chart.jpg", bbox_inches="tight")
