import datetime
import sqlite3
import requests as req

### get BTC price with API and write it in the database ###
def bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = req.get(url)
    btc_price = r.json()["bpi"]["USD"]["rate_float"]
    return int(btc_price)


def w_data(price, date):
    """write in databse"""
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS btc (prices INTEGER, date DATE)""")
    cursor.execute(f"INSERT INTO btc VALUES({price}, '{date}')")
    conn.commit()
    conn.close()


price = bitcoin_price()
date = str(datetime.date.today())

w_data(price, date)
