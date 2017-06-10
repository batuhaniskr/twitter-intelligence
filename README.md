# Social-Network-Tracking-And-Analysis

A project written in Python to get old tweets and tweet analysis

## Prerequisites

<li>Project written for Python 3.x </li>

<li>PyQuery is required for HTML parsing</li>

<li>Matplotlib is required for analysis</li>

<li>PyQt is required for GUI application</li>

## Database

<li>SQLite is used as the database.</li>

<li>Tweet data are stored on the Tweet, User, Location, Hashtag, HashtagTweet tables.</li>

<li>The database is created automically.</li>

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

<li> socialgui.py used for gui application</li>
