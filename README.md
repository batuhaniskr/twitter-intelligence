# Twitter Intelligence

A project written in Python to twitter tracking and analysis without using Twitter API.

## Prerequisites
  <ul>
  <li>This project is a Python 3.x application.</li>
  
  <li>The package dependencies are in the file requirements.txt. Run that command to install the dependencies.</li>
  <br>
  <pre>pip3 install -r requirements.txt</pre>
  
</ul>

## Database

<ul>
  <li>SQLite is used as the database.</li>

  <li>Tweet data are stored on the Tweet, User, Location, Hashtag, HashtagTweet tables.</li>

  <li>The database is created automically.</li>
</ul>

## Usage Example

<b>Application work view:</b>

![screen shot 2018-07-06 at 12 18 51](https://user-images.githubusercontent.com/17202632/42370978-d4ea95a6-8116-11e8-97c9-bd8bf0ac7299.png)

<ul>
  
<li>Get help</li>

<pre> python3 tracking.py -h </pre>

<li>Get tweets by username </li>
<br>
<pre> python3 tracking.py --username "HaberSau" </pre>

<li>Get tweets by query</li>

<br>

<pre> python3 tracking.py --query "sakarya" </pre>

<li>Get tweet at a specific date range</li>
<br>
<pre> python3 tracking.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 10 </pre>

<li> If you get location of tweets, add --location "True" param but application will be slower due to new response times.
<br><br>
<pre> python3 tracking.py --query "sakarya" --location "True"</pre>

</ul>

<ul>
  <li>If you want you can run the application on the docker. </li>
  <br>
  <pre>docker build . -t twitter-intelligence</pre>
  <br>
  <pre>docker run -it -p 5000:5000 --rm -v "images:/usr/src/app/images" twitter-intelligence</pre>
 </ul>

## Analysis

 analysis.py performs analysis processing. User, hashtag and location analyzes are performed.

<li>Get help:</li>
<br>
<pre>python3 analysis.py -h</pre> 

<li>for location analysis </li>
<br>
<pre>python3 analysis py --location</pre>

![map](https://user-images.githubusercontent.com/17202632/41524483-5baf98be-72e6-11e8-9130-c6db7380ae5d.png)

location analysis runs through address http://localhost:5000/locations

You must write Google Map Api Key in setting.py to display google map.

<pre>GOOGLE_MAP_API_KEY='YOUR_GOOGLE_MAP_API_KEY'</pre>

<li>Runs hashtag analysis.</li>
<br>
<pre>python3 analysis.py --hashtag</pre> 

![hashtag](https://user-images.githubusercontent.com/17202632/43121336-135e21e6-8f26-11e8-93bd-16fe966f8aeb.png)

<li>Runs user analysis.</li>
<br>
<pre>python3 analysis.py --user</pre> 


## Graphical User Interface
 If you want run gui application, you should change "#PyQt5==5.11.2" to "PyQt5==5.11.2" in requirements.txt and you can run the that command.
 <pre>pip3 install -r requirements.txt</pre>
 
 socialgui.py used for gui application
 
