#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt
import parser
import sqlite3
import sys

from termcolor import colored

conn = sqlite3.connect('TweetAnalysis.db')
conn.row_factory = lambda cursor, row: row[1]
c = conn.cursor()
hash_list = []

c.execute("CREATE TABLE IF NOT EXISTS Location (locationid, place)")
c.execute("CREATE TABLE IF NOT EXISTS User (userid, username, locationid)")
c.execute("CREATE TABLE IF NOT EXISTS Hashtag (hashtagid, content)")
c.execute("CREATE TABLE IF NOT EXISTS HashtagTweet (hashtagid, tweetid)")
c.execute(
    "CREATE TABLE IF NOT EXISTS Tweet (tweetid, text, username, hashtag, date, time, retweet, favorite, mention, userid, locationid)")


def main(argv):
    # graph_data()
    if len(argv) == 0:
        print('You must pass some parameters. Use \"-h\" to help.')
        return

    if len(argv) == 1 and argv[0] == '-h':
        __tool_logo()
        print("""
 \n""" + colored(" Examples:\n", "green") + """
  """ + colored('# Get tweets by username\n', 'green') +
              """
       python3 tracking.py --username "HaberSau"\n
      
  """ + colored('# Get tweets by query\n', 'green') +
              """
       python3 tracking.py --query "sakarya"\n
      
  """ + colored('# Get twit at a specific date range\n', 'green') + """
       python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10\n

 """ + colored(' # Get the last 10 top tweets by username\n', 'green') + """
       python3 tracking.py --username "HaberSau" --maxtweets 10 --toptweets\n""")
        return
    location_value = False

    try:
        opts, args = getopt.getopt(argv, "",
                                   ("username=", "since=", "until=", "query=", "toptweets=", "maxtweets=", "location="))

        tweet_criteria = parser.operation.TweetCriteria()

        for opt, arg in opts:
            if opt == '--username':
                tweet_criteria.username = arg
            elif opt == '--since':
                tweet_criteria.since = arg
            elif opt == '--until':
                tweet_criteria.until = arg
            elif opt == '--query':
                tweet_criteria.query = arg
            elif opt == '--toptweets':
                tweet_criteria.topTweets = True
            elif opt == '--maxtweets':
                tweet_criteria.maxTweets = int(arg)
            elif opt == '--location':
                location_value = bool(arg)
                print(location_value)

        __tool_logo()
        print('\n' + colored('[+] Searching...', 'green') + '\n')

        def receive_buffer(tweets):
            locationid = 1;
            hashtagid = 1;
            for t in tweets:
                hashtagstring = t.hashtags
                str = hashtagstring.split()

                for hash in str:
                    hash_list.append(hash)
                    params_hashtag = (hashtagid, hash)
                    params_hashag_tweet = (hashtagid, t.id)
                    if hash != "":
                        hashtagid = hashtagid + 1
                        c.execute("SELECT * FROM hashtag where content = '%s'" % hash)
                        exits = c.fetchone()
                        if exits is None:
                            c.execute("SELECT hashtag FROM tweet ")

                            c.execute("INSERT OR IGNORE INTO HashtagTweet VALUES (?,?)", params_hashag_tweet)
                            c.execute("INSERT OR IGNORE INTO Hashtag  VALUES (?,?)", params_hashtag)

                params_tweet = (
                    t.id, t.text, t.username, t.hashtags, t.date.strftime('%Y-%m-%d'), t.date.strftime('%H:%M'),
                    t.retweets,
                    t.favorites, t.mentions, t.user_id, locationid)

                c.execute("SELECT * FROM Tweet where tweetid ='%s'" % t.id)
                userexist = c.fetchone()
                if userexist is None:
                    c.execute("INSERT INTO Tweet VALUES (?,?,?,?,?,?,?,?,?,?,?)", params_tweet)

                params_location = (locationid, t.geo)
                c.execute("SELECT * FROM location where place = '%s'" % t.geo)
                locationexist = c.fetchone()
                if locationexist is None and t.geo != '':
                    c.execute("INSERT INTO Location VALUES(?,?)", params_location)
                    locationid = locationid + 1

                c.execute("SELECT * FROM location where place = '%s'" % t.geo)
                locatuid = c.fetchone()
                params_user = (t.user_id, t.username, locatuid)
                c.execute("SELECT * FROM user where username ='%s'" % t.username)
                userexist = c.fetchone()
                if userexist is None:
                    c.execute("INSERT OR IGNORE INTO User VALUES(?,?,?)", params_user)

                conn.commit()
            print(colored('\n[+] %d tweet received...\n' % len(tweets), 'green'))

        parser.operation.TweetManager.get_tweets(tweet_criteria, receive_buffer, location_search=location_value)

    except arg:
        print('You must pass some parameters. Use \"-h\" to help.' + arg)

    finally:
        print(colored('[+] Succesfully saved to the database.', 'green'))
        conn.close()


def __tool_logo():
    print(colored('''\n\t\t\033[1m        
             ___________       .__.__  __                                          
             \__    ___/_  _  _|__|__|/  |_  ___________                           
               |    |  \ \/ \/ /  |  \   __\/ __ \_  __ \                          
               |    |   \     /|  |  ||  | \  ___/|  | \/                          
               |____|    \/\_/ |__|__||__|  \___  >__|                             
            .___        __         .__  .__  .__\/                                 
            |   | _____/  |_  ____ |  | |  | |__| ____   ____   ____   ____  ____  
            |   |/    \   __\/ __ \|  | |  | |  |/ ___\_/ __ \ /    \_/ ___\/ __ \ 
            |   |   |  \  | \  ___/|  |_|  |_|  / /_/  >  ___/|   |  \  \__\  ___/ 
            |___|___|  /__|  \___  >____/____/__\___  / \___  >___|  /\___  >___  >
                     \/          \/            /_____/      \/     \/     \/    \/ 
       /.\                          
       Y  \                  
      /   "L                 
     //  "/                  
     |/ /\_==================
     / /            
    / /     
    \/''', 'green'))


if __name__ == '__main__':
    main(sys.argv[1:])
