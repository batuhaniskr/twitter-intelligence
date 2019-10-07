import datetime
import http.cookiejar as cookielib
import json
import re
import sys
import urllib
import urllib.request as urllib2

import requests
from lxml import html
from pyquery import PyQuery
from termcolor import colored

from .. import model


class TweetManager:

    def __init__(self):
        pass

    @staticmethod
    def get_tweets(tweet_criteria, receive_buffer=None, location_search=False, buffer_length=100, proxy=None):
        refresh_cursor = ''
        results = []
        results_aux = []
        cookiejar = cookielib.CookieJar()

        if hasattr(tweet_criteria, 'username') and (
                tweet_criteria.username.startswith("\'") or tweet_criteria.username.startswith("\"")) and (
                tweet_criteria.username.endswith("\'") or tweet_criteria.username.endswith("\"")):
            tweet_criteria.username = tweet_criteria.username[1:-1]

        active = True

        while active:
            try:
                json = TweetManager.get_json_response(tweet_criteria, refresh_cursor, cookiejar, proxy)
                if len(json['items_html'].strip()) == 0:
                    break

                refresh_cursor = json['min_position']
                scraped_tweets = PyQuery(json['items_html'])
                # Remove incomplete tweets withheld by Twitter Guidelines
                scraped_tweets.remove('div.withheld-tweet')
                tweets = scraped_tweets('div.js-stream-tweet')

                if len(tweets) == 0:
                    break

                for tweet_html in tweets:
                    tweetPQ = PyQuery(tweet_html)
                    tweet = model.Tweet()

                    username_tweet = tweetPQ("span:first.username.u-dir b").text()
                    txt = re.sub(r"\s+", " ", tweetPQ("p.js-tweet-text").text())
                    txt = txt.replace('# ', '#')
                    txt = txt.replace('@ ', '@')

                    print(colored("@" + username_tweet + ": ", "red") + colored(txt, "green") + "\n")

                    retweets = int(tweetPQ("span.ProfileTweet-action--retweet span.ProfileTweet-actionCount").attr(
                        "data-tweet-stat-count").replace(",", ""))
                    favorites = int(tweetPQ("span.ProfileTweet-action--favorite span.ProfileTweet-actionCount").attr(
                        "data-tweet-stat-count").replace(",", ""))
                    dateSec = int(tweetPQ("small.time span.js-short-timestamp").attr("data-time"))
                    id = tweetPQ.attr("data-tweet-id")
                    permalink = tweetPQ.attr("data-permalink-path")
                    user_id = int(tweetPQ("a.js-user-profile-link").attr("data-user-id"))

                    if location_search == True:
                        page = requests.get('https://twitter.com/tubiity/status/' + id)
                        script_geo = html.fromstring(page.content)
                        location = script_geo.xpath('//a[@class="u-textUserColor js-nav js-geo-pivot-link"]/text()')
                        sp_location = ','.join(location)
                        tweet.geo = sp_location
                    else:
                        geo = ''
                        tweet.geo = geo

                        # user-information
                        ''' If this code block is uncommented, application will be slower due to response time'''
                        '''result = requests.get("https://twitter.com/" + username_tweet)
                        c = result.content

                        soup = BeautifulSoup(c, "html.parser")
                        liste = []
                        samples = soup.find_all("a",
                                                    "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor")
                            # Follower, Follow and number of likes in list
                        for a in samples:
                            liste.append(a.attrs['title'])
                        '''

                    tweet.id = id
                    tweet.permalink = 'https://twitter.com' + permalink
                    tweet.username = username_tweet
                    tweet.text = txt
                    tweet.date = datetime.datetime.fromtimestamp(dateSec)
                    tweet.retweets = retweets
                    tweet.favorites = favorites
                    tweet.mentions = " ".join(re.compile('(@\\w*)').findall(tweet.text))
                    tweet.hashtags = " ".join(re.compile('(#\\w*)').findall(tweet.text))
                    tweet.user_id = user_id

                    results.append(tweet)
                    results_aux.append(tweet)

                    if receive_buffer and len(results_aux) >= buffer_length:
                        receive_buffer(results_aux)
                        results_aux = []

                    if tweet_criteria.maxTweets > 0 and len(results) >= tweet_criteria.maxTweets:
                        active = False
                        break

            except:
                receive_buffer(results_aux)
                return

        if receive_buffer and len(results_aux) > 0:
            receive_buffer(results_aux)

        return results

    @staticmethod
    def get_json_response(tweet_criteria, refresh_cursor, cookiejar, proxy):
        url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&max_position=%s"

        url_data = ''

        if hasattr(tweet_criteria, 'username'):
            url_data += ' from:' + tweet_criteria.username

        if hasattr(tweet_criteria, 'query'):
            url_data += ' ' + tweet_criteria.query

        if hasattr(tweet_criteria, 'since'):
            url_data += ' since:' + tweet_criteria.since

        if hasattr(tweet_criteria, 'until'):
            url_data += ' until:' + tweet_criteria.until

        if hasattr(tweet_criteria, 'topTweets'):
            if tweet_criteria.topTweets:
                url = "https://twitter.com/i/search/timeline?q=%s&src=typd&max_position=%s"

        url = url % (urllib.parse.quote(url_data), urllib.parse.quote(refresh_cursor))

        headers = [
            ('Host', "twitter.com"),
            ('User-Agent',
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', url),
            ('Connection', "keep-alive")
        ]

        if proxy:
            opener = urllib2.build_opener(urllib2.ProxyHandler({'http': proxy, 'https': proxy}),
                                          urllib2.HTTPCookieProcessor(cookiejar))
        else:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
            opener.addheaders = headers

        try:
            response = opener.open(url)
            json_response = response.read()
        except:
            print
            "Twitter weird response. Try to see on browser: https://twitter.com/search?q=%s&src=typd" % urllib.parse.quote(
                url_data)
            sys.exit()
            return

        data = json.loads(json_response)

        return data
