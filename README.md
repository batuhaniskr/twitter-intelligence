# Social Network Tracking And Analysis

A project written in Python to get old tweets and tweet analysis.

## Prerequisites
  <ul>
  <li>Project written for Python 3.x.</li>

  <li>PyQuery is required for HTML parsing.</li>

  <li>Matplotlib is required for analysis.</li>

  <li>PyQt is required for GUI application.</li>  
  
  <li>The package dependencies are in the file requirements.txt. Run that command to install the dependencies.</li>
  <pre>pip install -r requirements.txt</pre>
</ul>

## Database

<ul>
  <li>SQLite is used as the database.</li>

  <li>Tweet data are stored on the Tweet, User, Location, Hashtag, HashtagTweet tables.</li>

  <li>The database is created automically.</li>
</ul>

## Command-line usage

<ul>
<li>Get help</li>

<pre> python3 tracking.py -h </pre>

<li>Get tweets by username </li>

<pre> python3 tracking.py --username "HaberSau" </pre>


<li>Get tweets by query</li>


<pre> python3 tracking.py --query "sakarya" </pre>


<li>Get twit at a specific date range</li>


<pre> python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10 </pre>

Application work view:

![screenshot from 2017-06-11 22-23-16](https://user-images.githubusercontent.com/17202632/27014790-793342d0-4f08-11e7-951e-5bc374504a48.png)
</ul>

## Graphical User Interface

 socialgui.py used for gui application
