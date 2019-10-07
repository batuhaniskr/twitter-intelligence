#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import getopt
import json
import os.path
import sqlite3
import sys
from collections import Counter

import matplotlib.pyplot as pl
import numpy as np
from flask import Flask, render_template
from geopy.geocoders import Nominatim
from termcolor import colored

import settings

ROOT_DIR = os.path.dirname(os.pardir)
db_path = os.path.join(ROOT_DIR, "TweetAnalysis.db")

app = Flask(__name__)


def main(argv):
    if len(argv) == 1 and argv[0] == '-h':
        print("""
                    [Analysis]
                    
 [--location] for location analysis
 [--hashtag]  for hashtag analysis
 [--user]     for user location analysis
        """)

        return

    try:
        opts, args = getopt.getopt(argv, "", ("hashtag", "user", "location", "h"))

        for opt, arg in opts:
            if opt == '--location':
                port = settings.PORT
                app.run('127.0.0.1', port=port)
            elif opt == '--user':
                analysis_user()
            elif opt == '--hashtag':
                analysis_hashtag()
            else:
                print('Invalid selection.')
    except:
        print('You must pass some parameters. Use \"-h\" to help.')


@app.route('/locations')
def map():
    location = location_analysis()
    api_key = settings.GOOGLE_MAP_API_KEY
    url = 'https://maps.googleapis.com/maps/api/js?key=' + api_key + '&libraries=visualization&callback=initMap'

    return render_template('locations.html', location=location, url=url)


def analysis_user():
    with sqlite3.connect(db_path) as db:
        conn = db
        c = conn.cursor()
        c.execute("SELECT  username, count(*) as tekrar FROM Tweet  group by username order by tekrar desc LIMIT 10")
        data = c.fetchall()
        ilk = []
        y = []
        i = 0
        for row in data:
            ilk.append(row[0])
            y.append(row[1])
            i = i + 1
            pl.figure(1)
            x = range(i)

        pl.bar(x, y, align='center')
        pl.xticks(x, ilk)
        # pl.plot(x, y, "-")
        pl.title('User - Tweet Count')
        pl.xlabel('Username')
        pl.ylabel('Tweet Count')
        print(colored("[INFO] Showing graph of user analysis", "green"))
        pl.show()


def analysis_hashtag():
    with sqlite3.connect(db_path) as db:
        conn = db
        c = conn.cursor()
        c.execute("SELECT hashtag from Tweet")
        hashtag_list = []
        for row in c.fetchall():
            if (row != ('',)):
                if " " in ''.join(row):
                    for m in ''.join(row).split(' '):
                        hashtag_list.append(m)
                else:
                    signle_item = ''.join(row)
                    hashtag_list.append(signle_item)

        counter = Counter(hashtag_list).most_common(10)
        pl.rcdefaults()

        keys = []
        performance = []

        for i in counter:
            performance.append(i[1])
            keys.append(i[0])

        pl.rcdefaults()
        y_pos = np.arange(len(keys))
        error = np.random.rand(len(keys))

        pl.barh(y_pos, performance, xerr=error, align='center', alpha=0.4, )
        pl.yticks(y_pos, keys)
        pl.xlabel('quantity')
        pl.title('hashtags')
        print(colored("[INFO] Showing graph of hashtag analysis", "green"))
        pl.show()


def location_analysis():
    with sqlite3.connect(db_path) as db:
        conn = db
        c = conn.cursor()

        locxy = []

        c.execute("Select place from location")
        loc_array = c.fetchall()

        # mapping
        geo_data = {

            "features": []
        }
        for x in range(len(loc_array)):
            if (loc_array[x] != ''):
                geolocator = Nominatim()
                location = geolocator.geocode(loc_array[x])
                locxy.append(location.latitude)
                locxy.append(location.longitude)

                geo_json_feature = {
                    "lat": location.latitude,
                    "lng": location.longitude
                }

                geo_data['features'].append(geo_json_feature)
                locxy.clear()

        json_location = json.dumps(geo_data)
        print(colored("[INFO] Showing graph of location analysis", "green"))
        return json_location


if __name__ == '__main__':
    main(sys.argv[1:])
