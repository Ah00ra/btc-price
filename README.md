# btc-price
Get the price of bitcoin and insert it into a database
and make chart with matplotlib.

## requirements

**Packages**

All of packages that you need to use this repository was written in `requirements.txt`
and they will be installed using:

```
pip install -r requirements.txt
```


**Database**
__Mariadb or Mysql__

Create database and table with command below.

```
CREATE DATABASE test; 
Use test;
CREATE TABLE btc(price int, date varchar(10));
```

| Field | Type        |
|-------|-------------|
| price | int(11)     |
| date  | varchar(10) | 

___
## btc-chart
`src/chart.py` output is a JPEG file like the image below.

![btc-chart](https://github.com/imahoora/btc-price/blob/main/image/btc-chart.jpg)
