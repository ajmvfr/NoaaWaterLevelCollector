import feedparser
import pandas as df
import xmltojson 
import json 
import re
from datetime import datetime

date_format = '%a, %d %b %Y %H:%M:%S %z'
# Thu, 19 Oct 2023 02:53:07 +0000

def GetWaterStats(ListOfStats):
    category = None
    level = None
    flow = None

    for l in ListOfStats:
        if "Latest Observation Category:" in l:
            category = l.split(":")[1].strip()

        if "Latest Observation:" in l:
            level = re.findall(r'[+-]?\d+(?:\.\d+)?', l)[0]

        if "Latest Observation (Secondary):" in l:
            flow = re.findall(r'[+-]?\d+(?:\.\d+)?', l)[0]         
            # flow = re.findall(r'[+-]?([0-9]*\.[0-9]+|[0-9]+)', l)[0]         

    return category,level,flow

def GetTitleElements(Title):
    station = None
    name = None

    tempElements = Title.split("-")
    station = tempElements[1].strip()
    name = tempElements[2].strip()
    return station, name




url = "https://water.weather.gov/ahps2/rss/obs/beap1.rss"
# url = "https://water.weather.gov/ahps2/rss/obs/mgyp1.rss"
feed = feedparser.parse(url)



print(feed.keys())



print('===========================================')
results = json.loads(xmltojson.parse(f'<?xml version="1.0"?><summary>{feed.entries[0].summary}</summary>'))
lst = results['summary']['div']
published = feed.entries[0].published
geo_lat = feed.entries[0].geo_lat
geo_long = feed.entries[0].geo_long
dt = datetime.strptime(published, date_format)

station, name = GetTitleElements(feed.entries[0].title)
category,level,flow = GetWaterStats(lst)

print(f"station: {station}, Name: {name}")
print(f'Published: {published} reformated: {dt}')
print(f"category: {category}, height: {level}, Speed: {flow}")
print(f"geo_lat: {geo_lat}, geo_long: {geo_long}")

print('===========================================')

detail = json.loads(xmltojson.parse(f'<?xml version="1.0"?><summary_detail>{feed.entries[0].summary_detail}</summary_detail>'))
# lst = feed.entries[0].summary_detail.value
print(detail)
print('========')
print(f"h2  0:{detail['summary_detail']['h2'][0]}    1:{detail['summary_detail']['h2'][1]}")
print(f"h4  0:{detail['summary_detail']['h4'][0]['u']}    1:{detail['summary_detail']['h4'][1]['u']}")

lires = detail['summary_detail']['ul']
lires0 = lires[0]['li']
lires1 = lires[1]['li']

print(f"0 {lires0}")
print(f"array0 0:{lires0[0]}   1:{lires0[1]}   2:{lires0[2]}")

print(f"1 {lires1}")
print(f"array1 0:{lires1[0]}   1:{lires1[1]}   2:{lires1[2]}")

# print(f"lires {lires}")
# for l in lires:
#     print(l['li'])
#     # for r in l:
#     #     print(r)

