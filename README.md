# Social-Network-Tracking-And-Analysis

A project written in Python to get old tweets and tweet analysis

# Prerequisites

Project written for Python 3.x 

PyQuery is required for HTML parsing

Matplotlib is required for analysis

# Database

SQLite is used as the database.

Tweet data are stored on the Tweet, User, Location, Hashtag, HashtagTweet tables.

The database is created automically.

# Command-line usage

Get help

<pre> python3 tracking.py -h </pre>

Get tweets by username 

<pre> python3 tracking.py --username "HaberSau" </pre>

Get tweets by query

<pre> python3 tracking.py --query "sakarya" </pre>

Get twit at a specific date range

<pre> python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10 </pre>

