# Twitter Web app (Lab 2-3)
## Description
After recieving a valid Twitter username, this app generates a map with locations of all those
who follow given user, them included.<br>
The procedure may take some time (up to a minute), because of geopy module ratelimits.<br>
### Dependencies used
+ FastAPI - which was our app built on. Great framework for both writing, and testing endpoints.
+ TwitterAPI (v2) - second version gave better and simpler working experience.
+ Folium - used to visualise geodata. A wrapper of Leaflet.js
+ geopy - was causing some troubles with ratelimits, but so far the best available service for retieving coordinates.
---
[App](https://op-twitter-app.herokuapp.com) is up and running, hosted on Heroku.<br>
Sadly, had to decrease number of followers processed for each request (100 -> 50) on cloud.<br><br>
Generated map is interactive, can be zoomed in and out. Markers are also interactive and display username and more precise location (city/county) about each user.


