# Social-Network-Tracking-And-Analysis

A project written in Python to get old tweets and tweet analysis

# Prerequisites

Project written for Python3 

Database

SQLite is used as the database.

Tweet data are stored on the tables.

The database is created automically.

# Command-line usage

Get help

python3 tracking.py -h

Get tweets by username 

python3 tracking.py --username "HaberSau"

Get tweets by query

<pre> python3 tracking.py --query "sakarya" </pre>

Get twit at a specific date range

python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10

