Noaa Water Level collector

I started writting this app to collect data of the river level.  This data is publicly available through NOAA.

I have an interest in how the water and flow increase based on weather.

This app is the first stage in an experiment based on curiosity.

Currelty this collects data from the NOAA river stations around Pittsburgh, PA.

Where a lot of weather.gov is based on API's, these monitoring stations are only accessible from RSS feeds

This RSS feed is a little wonky.  They are easily accessable by with the python feedparser library,  
however there are imbedded snippits of HTML that I had to parse to extract the values.

The collected data is written into a Postgres database.

The entire app and DB runs on a Ubuntu server I have hosted on the web.  

This appliation is executed by a cron job every 3 hours.  

The stations I intend to monitor are pulled from the DB and then iterated.  The RSS feed for each 
is parsed and the station readings are written to the DB.
