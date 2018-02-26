import matplotlib.pyplot as pl
from collections import Counter
import sqlite3, os
import os.path
import pandas as pd
import matplotlib.pyplot as plt
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
        pl.title('User - Tweet Count')
        pl.xlabel('Username')
        pl.ylabel('Tweet Count')
        pl.show()
analysis_graph()
