import datetime
import json
import mysql.connector
import requests as req

### get BTC price with API and write in database ###

def bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = req.get(url)
    btc_price = r.json()['bpi']['USD']['rate_float']
    return int(btc_price)


def w_mysql(price, date):
    cnx = mysql.connector.connect(user='root', password='root', database='test')

    cursor = cnx.cursor()

    cursor.execute(f"INSERT INTO btc VALUES('{price}', '{date}')")
    cnx.commit()

    cursor.close()
    cnx.close()


price = bitcoin_price()
date = str(datetime.date.today())

w_mysql(price, date)

