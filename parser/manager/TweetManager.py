import urllib, urllib.request as urllib2, json, re, datetime, sys, http.cookiejar as cookielib

import requests
from lxml import html
from termcolor import colored

from .. import models
from pyquery import PyQuery


class TweetManager:

    def __init__(self):
        pass

    @staticmethod
    def getTweets(tweetCriteria, receiveBuffer=None, location_search=False, bufferLength=100, proxy=None):
        refreshCursor = ''
        results = []
        resultsAux = []
        cookieJar = cookielib.CookieJar()

        if hasattr(tweetCriteria, 'username') and (
                tweetCriteria.username.startswith("\'") or tweetCriteria.username.startswith("\"")) and (
                tweetCriteria.username.endswith("\'") or tweetCriteria.username.endswith("\"")):
            tweetCriteria.username = tweetCriteria.username[1:-1]

        active = True

        while active:
            try:
                json = TweetManager.getJsonReponse(tweetCriteria, refreshCursor, cookieJar, proxy)
                if len(json['items_html'].strip()) == 0:
                    break

                refreshCursor = json['min_position']
                scrapedTweets = PyQuery(json['items_html'])
                # Remove incomplete tweets withheld by Twitter Guidelines
                scrapedTweets.remove('div.withheld-tweet')
                tweets = scrapedTweets('div.js-stream-tweet')

                if len(tweets) == 0:
                    break

                for tweetHTML in tweets:
                    tweetPQ = PyQuery(tweetHTML)
                    tweet = models.Tweet()

                    usernameTweet = tweetPQ("span:first.username.u-dir b").text()
                    txt = re.sub(r"\s+", " ", tweetPQ("p.js-tweet-text").text())
                    txt = txt.replace('# ', '#')
                    txt = txt.replace('@ ', '@')

                    print(colored("@" + usernameTweet, "red") + colored(": ", "red") + txt + "\n")

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
                        '''result = requests.get("https://twitter.com/" + usernameTweet)
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
                    tweet.username = usernameTweet
                    tweet.text = txt
                    tweet.date = datetime.datetime.fromtimestamp(dateSec)
                    tweet.retweets = retweets
                    tweet.favorites = favorites
                    tweet.mentions = " ".join(re.compile('(@\\w*)').findall(tweet.text))
                    tweet.hashtags = " ".join(re.compile('(#\\w*)').findall(tweet.text))
                    tweet.user_id = user_id

                    results.append(tweet)
                    resultsAux.append(tweet)

                    if receiveBuffer and len(resultsAux) >= bufferLength:
                        receiveBuffer(resultsAux)
                        resultsAux = []

                    if tweetCriteria.maxTweets > 0 and len(results) >= tweetCriteria.maxTweets:
                        active = False
                        break

            except:
                receiveBuffer(resultsAux)
                return

        if receiveBuffer and len(resultsAux) > 0:
            receiveBuffer(resultsAux)

        return results

    @staticmethod
    def getJsonReponse(tweetCriteria, refreshCursor, cookieJar, proxy):
        url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&max_position=%s"

        urlGetData = ''

        if hasattr(tweetCriteria, 'username'):
            urlGetData += ' from:' + tweetCriteria.username

        if hasattr(tweetCriteria, 'querySearch'):
            urlGetData += ' ' + tweetCriteria.querySearch

        if hasattr(tweetCriteria, 'since'):
            urlGetData += ' since:' + tweetCriteria.since

        if hasattr(tweetCriteria, 'until'):
            urlGetData += ' until:' + tweetCriteria.until

        if hasattr(tweetCriteria, 'topTweets'):
            if tweetCriteria.topTweets:
                url = "https://twitter.com/i/search/timeline?q=%s&src=typd&max_position=%s"

        url = url % (urllib.parse.quote(urlGetData), refreshCursor)

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
                                          urllib2.HTTPCookieProcessor(cookieJar))
        else:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        opener.addheaders = headers

        try:
            response = opener.open(url)
            jsonResponse = response.read()
        except:
            print
            "Twitter weird response. Try to see on browser: https://twitter.com/search?q=%s&src=typd" % urllib.parse.quote(
                urlGetData)
            sys.exit()
            return

        dataJson = json.loads(jsonResponse)

        return dataJson
