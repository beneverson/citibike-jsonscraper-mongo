#!/usr/bin/python2.7
# Author Ben Everson

import requests
import time
from time import sleep, time, strftime, strptime
import datetime
from sched import scheduler
from pymongo import MongoClient

STATIONS_ENDPOINT = 'http://citibikenyc.com/stations/json'

s = scheduler(time, sleep)

# set up mongo db stuff
client = MongoClient()
db = client.citibike
collection = db.archive

def run_periodically(start, end, interval, func):
    event_time = start
    while event_time < end:
        s.enterabs(event_time, 0, func, ())
        event_time += interval
    s.run()

def get_stations():
    """Returns a list where each element of that list is a station
    retreived from the endpoint passed in above"""
    all_stations = []
    _stations = requests.get(STATIONS_ENDPOINT).json()
    _datetime = datetime.datetime.utcnow()
    for _station in _stations['stationBeanList']:
        if _station['statusKey'] == 1: # go through all the stations
            _station['date'] = _datetime # tag with the date and time
            all_stations.append(_station) # 
    # now insert the record into the mongo database
    stations_id = collection.insert(all_stations)

run_periodically(time()+5, time()+(7*24*60*60), 600, get_stations)