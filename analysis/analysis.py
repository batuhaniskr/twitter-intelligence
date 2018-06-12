import matplotlib.pyplot as pl
from collections import Counter
import sqlite3, os
import os.path
import numpy as np

def analysis_graph():
    ROOT_DIR = os.path.dirname(os.pardir)
    db_path = os.path.join(ROOT_DIR, "TweetAnalysis.db")

    with sqlite3.connect(db_path) as db:

        conn = db
        c = conn.cursor()

        #username - tweet analysis
        c.execute("SELECT  username, count(*) as tekrar FROM Tweet  group by username order by tekrar desc LIMIT 10")
        data = c.fetchall()
        ilk=[]
        y=[]
        i=0
        for row in data:
            ilk.append(row[0])
            y.append(row[1])
            i=i+1
            pl.figure(1)
            x = range(i)

        pl.bar(x, y, align='center')
        pl.xticks(x, ilk)
        #pl.plot(x, y, "-")
        pl.title('User - Tweet Count')
        pl.xlabel('Username')
        pl.ylabel('Tweet Count')
        pl.show()

        #Hashtag Analysis
        c.execute("SELECT hashtag from Tweet")
        hashtag_list = []
        for i in c.fetchall():
            if " " in ''.join(i):
                for m in ''.join(i).split(' '):
                    hashtag_list.append(m)
            else:
                signle_item  = ''.join(i)
                hashtag_list.append(signle_item)

        print(Counter(hashtag_list))
        counter = Counter(hashtag_list)

        pl.rcdefaults()
        # Counter data, counter is your counter object
        keys = counter.keys()
        y_pos = np.arange(len(keys))
        # get the counts for each key, assuming the values are numerical
        performance = [counter[k] for k in keys]
        print(performance)
        # not sure if you want this :S
        error = np.random.rand(len(keys))

        pl.barh(y_pos, performance, xerr=error, align='center', alpha=0.4, )
        pl.yticks(y_pos, keys)
        pl.xlabel('quantity')
        pl.title('hashtags')
        pl.show()

analysis_graph()

