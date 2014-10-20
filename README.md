# Citibike Data Scraper for MongoDB

##### *Retrieve data from Citibike's JSON feed, and insert it into a MongoDB instance.*

This is a simple python script that allows you to periodically scrape [Citibike JSON feed](http://www.citibikenyc.com/system-data) data and store the result in a local MongoDB instance. 

Mongo handling is done entirely through [PyMongo](http://api.mongodb.org/python/current/), and is set up to connect to the default local MongoDB instance on your machine. 

This script runs periodically, so the start time, duration and frequency of the script's execution can be customized by altering the arguments to the `run_periodically` function. For example, `run_periodically(time()+5, time()+(7*24*60*60), 600, get_stations)` starts running the script 5 seconds in the future, finishes running it 7 days in the future, and runs it every 600 seconds (10 minutes). 

###### Usage:
```
python jsonscraper.py

```

