import matplotlib.pyplot as pl
from collections import Counter
import sqlite3, os
import os.path
import pandas as pd
#import pylab as pl
from geopy.geocoders import Nominatim
import json

# Tweets are stored in "fname"


def analysis_graph():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "TweetAnalysis.db")
    locxy = []

    with sqlite3.connect(db_path) as db:

        conn = db

        c = conn.cursor()
        c.execute("Select place from location")
        loc_array=c.fetchall()
        c.execute("Select text from Tweet")
        tweet = c.fetchall()
        #print(tweet)



        # mapping
        geo_data = {

            "features": []
        }

        for x in range(len(loc_array)):

          #  print("adres",loc_array[x])
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

    with open('geo_data.json', 'w') as fout:
        fout.write(json.dumps(geo_data, indent=4))
        c.execute("Select text from tweet")
        tweet_data = c.fetchall()
        # print(tweet_data)
        c.execute("SELECT  username, count(*) as tekrar FROM Tweet  group by username order by tekrar desc LIMIT 10")
        data = c.fetchall()
        ilk=[]
        y=[]
        xTicks=[]
        i=0
        for row in data:
            ilk.append(row[0])
            y.append(row[1])
            i=i+1
            pl.figure(1)
            x = range(i)

        pl.bar(x, y, align='center',alpha=1.5)
        pl.xticks(x, ilk)
        #pl.plot(x, y, "-")
        pl.title('En fazla twit atan kullanıcılar')
        pl.xlabel('Kullanıcı Adı')
        pl.ylabel('Twit Sayısı')
        pl.show()



analysis_graph()
