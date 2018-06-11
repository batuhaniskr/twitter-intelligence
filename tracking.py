# -*- coding: utf-8 -*-

import sys, getopt, got3
import sqlite3
from geopy.geocoders import Nominatim
from termcolor import colored

conn = sqlite3.connect('TweetAnalysis.db')
conn.row_factory = lambda cursor, row: row[1]
c = conn.cursor()
hash_list = []

c.execute("CREATE TABLE IF NOT EXISTS Location (locationid, place)")
c.execute("CREATE TABLE IF NOT EXISTS User (userid, username, locationid)")
c.execute("CREATE TABLE IF NOT EXISTS Hashtag (hashtagid, content)")
c.execute("CREATE TABLE IF NOT EXISTS HashtagTweet (hashtagid, tweetid)")
c.execute("CREATE TABLE IF NOT EXISTS Tweet (tweetid, text, username, hashtag, date, time, retweet, favorite, mention, userid, locationid)")

def main(argv):
    #graph_data()
    if len(argv) == 0:
        print('You must pass some parameters. Use \"-h\" to help.')
        return

    if len(argv) == 1 and argv[0] == '-h':
        print_color_text()
        print("""
 \n"""+colored("Examples:\n","blue")+"""
  """+colored('# Get tweets by username\n','green')+
        """
 python3 tracking.py --username "HaberSau"\n

 """+colored('# Get tweets by query\n','green')+
        """
 python3 tracking.py --query "sakarya"\n

 """+colored('# Get twit at a specific date range\n','green')+"""
 python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10\n


 """+colored('# Get the last 10 top tweets by username\n','green')+"""
 python3 tracking.py --username "HaberSau" --maxtweets 10 --toptweets\n""")
        return

    try:
        opts, args = getopt.getopt(argv, "", ("username=", "since=", "until=", "query=", "toptweets=", "maxtweets="))

        tweetCriteria = got3.manager.TweetCriteria()

        for opt, arg in opts:
            if opt == '--username':
                tweetCriteria.username = arg

            elif opt == '--since':
                tweetCriteria.since = arg

            elif opt == '--until':
                tweetCriteria.until = arg

            elif opt == '--query':
                tweetCriteria.querySearch = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = True

            elif opt == '--maxtweets':
                tweetCriteria.maxTweets = int(arg)
        #print_color_text()
        print('\n'+colored('Searching...','green')+'\n')

        def receiveBuffer(tweets):
            locationid = 1;
            hashtagid= 1;
            for t in tweets:
                hashtagstring = t.hashtags
                #userchefck = t.username
                str = hashtagstring.split()
                #print(usercheck)
                #serstr=usercheck.split()


                #print("text",str)
                for hash in str:
                    hash_list.append(hash)
                    paramsHashtag = (hashtagid, hash)
                    paramsHashagTweet = (hashtagid, t.id)
                    if hash != "":
                        hashtagid = hashtagid + 1
                        c.execute("SELECT * FROM hashtag where content = '%s'" % hash)
                        #aynı içeriğin olup olmama kontrolü
                        exits = c.fetchone()
                        if exits is None:
                            c.execute("SELECT hashtag FROM tweet ")

                            c.execute("INSERT OR IGNORE INTO HashtagTweet VALUES (?,?)", paramsHashagTweet)
                            c.execute("INSERT OR IGNORE INTO Hashtag  VALUES (?,?)", paramsHashtag)

                a=t.date.strftime('%H:%M')

                paramsTweet = (t.id, t.text, t.username,t.hashtags, t.date.strftime('%Y-%m-%d'),t.date.strftime('%H:%M'), t.retweets, t.favorites, t.mentions,t.user_id, locationid)

                c.execute("SELECT * FROM Tweet where tweetid ='%s'" % t.id)
                userexist = c.fetchone()
                if userexist is None:
                    c.execute("INSERT INTO Tweet VALUES (?,?,?,?,?,?,?,?,?,?,?)", paramsTweet)
                # aynı içeriğin olup olmama kontrolü
                if(t.geo!=""):
                    geolocator = Nominatim()
                    location = geolocator.geocode("")
                    #print(location)
                paramsLocation = (locationid, t.geo)
                c.execute("SELECT * FROM location where place = '%s'" % t.geo)
                locationexist = c.fetchone()
                if locationexist is None and t.geo!='':

                        c.execute("INSERT INTO Location VALUES(?,?)", paramsLocation)
                        locationid = locationid + 1

                c.execute("SELECT *FROM location where place = '%s'" % t.geo)
                locatuid = c.fetchone()
                paramsUser = (t.user_id, t.username, locatuid)
                c.execute("SELECT * FROM user where username ='%s'" % t.username)
                userexist = c.fetchone()
                if userexist is None:
                    c.execute("INSERT OR IGNORE INTO User VALUES(?,?,?)", paramsUser)

                conn.commit()
            print('More %d saved on file...\n' % len(tweets))

        got3.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

    except arg:
        print('You must pass some parameters. Use \"-h\" to help.' + arg)

    finally:
        print('Succesfully saved in the database.')
        conn.close()
        # Counter

def print_color_text():
    print(colored('''\n\t\t\033[1m
                      __            _       _       __     _                      _
                     / _\ ___   ___(_) __ _| |   /\ \ \___| |___      _____  _ __| | __
                     \ \ / _ \ / __| |/ _` | |  /  \/ / _ \ __\ \ /\ / / _ \| '__| |/ /
                     _\ \ (_) | (__| | (_| | | / /\  /  __/ |_ \ V  V / (_) | |  |   <
                     \__/\___/ \___|_|\__,_|_| \_\ \/ \___|\__| \_/\_/ \___/|_|  |_|\_\

            _____                _    _                               _     _               _           _
           /__   \_ __ __ _  ___| | _(_)_ __   __ _    __ _ _ __   __| |   /_\  _ __   __ _| |_   _ ___(_)___
             / /\/ '__/ _` |/ __| |/ / | '_ \ / _` |  / _` | '_ \ / _` |  //_\\| '_ \ / _` | | | | / __| / __|
            / /  | | | (_| | (__|   <| | | | | (_| | | (_| | | | | (_| | /  _  \ | | | (_| | | |_| \__ \ \__ \\
            \/   |_|  \__,_|\___|_|\_\_|_| |_|\__, |  \__,_|_| |_|\__,_| \_/ \_/_| |_|\__,_|_|\__, |___/_|___/
                                              |___/                                           |___/



                   ''', 'blue'))
if __name__ == '__main__':
    main(sys.argv[1:])

