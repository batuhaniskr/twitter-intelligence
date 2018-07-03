# Social Network Tracking And Analysis

A project written in Python to get old tweets and tweet analysis.

## Prerequisites
  <ul>
  <li>This project is a Python 3.x application.</li>
  
  <li>The package dependencies are in the file requirements.txt. Run that command to install the dependencies.</li>
    <br>

  <pre>pip install -r requirements.txt</pre>
  
</ul>

## Database

<ul>
  <li>SQLite is used as the database.</li>

  <li>Tweet data are stored on the Tweet, User, Location, Hashtag, HashtagTweet tables.</li>

  <li>The database is created automically.</li>
</ul>

## Usage Example

<ul>
  
<li>Get help</li>

<pre> python3 tracking.py -h </pre>

<li>Get tweets by username </li>

<pre> python3 tracking.py --username "HaberSau" </pre>


<li>Get tweets by query</li>


<pre> python3 tracking.py --query "sakarya" </pre>


<li>Get tweet at a specific date range</li>


<pre> python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10 </pre>

<li> If you get location of tweets, add --location "True" param but application will be slower due to new response times.

<pre> python3 tracking.py --query "sakarya" --location "True"</pre>
Application work view:

![screenshot from 2017-06-11 22-23-16](https://user-images.githubusercontent.com/17202632/27014790-793342d0-4f08-11e7-951e-5bc374504a48.png)
</ul>

## Analysis

 analysis.py performs analysis processing. User, hashtag and location analyzes are performed.

<li>Get help:</li>
<pre>python3 analysis.py -h</pre> 

<li>for location analysis </li>
<pre>python3 analysis py --location</pre>

![map](https://user-images.githubusercontent.com/17202632/41524483-5baf98be-72e6-11e8-9130-c6db7380ae5d.png)

location analysis runs through address http://localhost:5000/locations

You must write Google Map Api Key in setting.py to display google map.

<pre>GOOGLE_MAP_API_KEY='YOUR_GOOGLE_MAP_API_KEY'</pre>

<li>Runs user analysis.</li>
<pre>python3 analysis.py --user</pre> 
<li>Runs hashtag analysis.</li>
<pre>python3 analysis.py --hashtag</pre> 

## Graphical User Interface

 socialgui.py used for gui application
