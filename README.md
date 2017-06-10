# Social-Network-Tracking-And-Analysis

A project written in Python to get old tweets and tweet analysis

## Prerequisites

  Project written for Python 3.x.

  PyQuery is required for HTML parsing.

  Matplotlib is required for analysis.

  PyQt is required for GUI application.

## Database

  SQLite is used as the database.

  Tweet data are stored on the Tweet, User, Location, Hashtag, HashtagTweet tables.

  The database is created automically.

## Command-line usage

<li>Get help</li>


<pre> python3 tracking.py -h </pre>


<li>Get tweets by username </li>


<pre> python3 tracking.py --username "HaberSau" </pre>


<li>Get tweets by query</li>


<pre> python3 tracking.py --query "sakarya" </pre>


<li>Get twit at a specific date range</li>


<pre> python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10 </pre>

# Graphical User Interface

 socialgui.py used for gui application
