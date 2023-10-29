from sqlalchemy.orm import Session
from . import models
from .database import get_db, SessionLocal
from sqlalchemy import func
from .NoaaWater import StationsReadings

import feedparser
import xmltojson 
import json 
from datetime import datetime
import re

def ParseValues(segment):
    value = None
    units = None

    if "Not Set" not in segment:
        value = re.findall(r'[+-]?\d+(?:\.\d+)?', segment)[0]
        value_array = segment.split()
        units = value_array[len(value_array)-1]

    return value, units


def GetWaterStats(ListOfStats):
    category = None
    level = None
    level_units = None
    flow = None
    flow_units = None
    SiteId = None
    ObservedDateTime = None

    for l in ListOfStats:
        if "Latest Observation Category:" in l:
            category = l.split(":")[1].strip()

        if "Latest Observation:" in l:
            level, level_units = ParseValues(l)

        if "Latest Observation (Secondary):" in l:
            flow, flow_units = ParseValues(l)


        if "site_no=" in str(l):
            SiteId = re.findall(r'[0-9]+',str(l))[0]

        if "Observation Time:" in l:
            # Oct 23, 2023 08:15 PM -0400
            ObservedDateTime = datetime.strptime(l.replace('Observation Time: ','').strip(''),'%b %d, %Y %I:%M %p %z')

    return category, level, level_units, flow, flow_units, SiteId, ObservedDateTime



def GetWaterActionPoints(summary_detail):
    ActionLevel = None
    ActionLevelUnits = None
    MinorLevel = None
    MinorLevelUnits = None
    ModerateLevel = None
    ModerateLevelUnits = None
    MajorLevel = None
    MajorLevelUnits = None
    ActionFlow = None
    ActionFlowUnits = None
    MinorFlow = None
    MinorFlowUnits = None
    ModerateFlow = None
    ModerateFlowUnits = None
    MajorFlow = None
    MajorFlowUnits = None

    print(f"========={summary_detail.get('ul')}")
    #if action section is not in summary detail, there is no data to find
    if summary_detail.get('ul') is not None:
        ListOfActions = summary_detail['ul']
        if type(ListOfActions) == list:
            lires0 = ListOfActions[0]['li']
            for l in lires0:
                if "Action" in l:
                    ActionLevel, ActionLevelUnits = ParseValues(l)
                if "Minor" in l:
                    MinorLevel, MinorLevelUnits = ParseValues(l)
                if "Moderate" in l:
                    ModerateLevel, ModerateLevelUnits = ParseValues(l)
                if "Major" in l:
                    MajorLevel, MajorLevelUnits = ParseValues(l)
            lires1 = ListOfActions[1]['li']
            for l in lires1:
                if "Action" in l:
                    ActionFlow, ActionFlowUnits = ParseValues(l)
                if "Minor" in l:
                    MinorFlow, MinorFlowUnits = ParseValues(l)
                if "Moderate" in l:
                    ModerateFlow, ModerateFlowUnits = ParseValues(l)
                if "Major" in l:
                    MajorFlow, MajorFlowUnits = ParseValues(l)
        else:
            lires = ListOfActions['li']
            for l in lires:
                if "Action" in l:
                    ActionLevel, ActionLevelUnits = ParseValues(l)
                if "Minor" in l:
                    MinorLevel, MinorLevelUnits = ParseValues(l)
                if "Moderate" in l:
                    ModerateLevel, ModerateLevelUnits = ParseValues(l)
                if "Major" in l:
                    MajorLevel, MajorLevelUnits = ParseValues(l)
            


    return ActionLevel, ActionLevelUnits, MinorLevel, MinorLevelUnits,ModerateLevel,ModerateLevelUnits,MajorLevel,MajorLevelUnits,ActionFlow,ActionFlowUnits,MinorFlow,MinorFlowUnits,ModerateFlow,ModerateFlowUnits,MajorFlow,MajorFlowUnits

def GetTitleElements(Title):
    station = None
    name = None

    tempElements = Title.split("-")
    station = tempElements[1].strip()
    name = tempElements[2].strip()
    return station, name


def WaterLevelRssParse(StationCode):
    url = f"https://water.weather.gov/ahps2/rss/obs/{StationCode.lower()}.rss"
    feed = feedparser.parse(url)

    summary = json.loads(xmltojson.parse(f'<?xml version="1.0"?><summary>{feed.entries[0].summary}</summary>'))
    DivList = summary['summary']['div']
    PublishedDate = datetime.strptime(feed.entries[0].published, '%a, %d %b %Y %H:%M:%S %z')

    StationCode, StationName = GetTitleElements(feed.entries[0].title)

    WaterCategory, WaterLevel,WaterLevelUnits, Waterflow, WaterflowUnits, SiteId, ObservedDateTime = GetWaterStats(DivList)

    geo_lat = feed.entries[0].geo_lat
    geo_long = feed.entries[0].geo_long


    summary_detail = json.loads(xmltojson.parse(f'<?xml version="1.0"?><summary_detail>{feed.entries[0].summary_detail}</summary_detail>'))

    ActionLevel, ActionLevelUnits, MinorLevel, MinorLevelUnits,ModerateLevel,ModerateLevelUnits,MajorLevel,MajorLevelUnits,ActionFlow,ActionFlowUnits,MinorFlow,MinorFlowUnits,ModerateFlow,ModerateFlowUnits,MajorFlow,MajorFlowUnits = GetWaterActionPoints(summary_detail['summary_detail'])

    water = StationsReadings(StationCode,StationName,SiteId,PublishedDate,ObservedDateTime,WaterCategory,WaterLevel,WaterLevelUnits,Waterflow,WaterflowUnits,ActionLevel, ActionLevelUnits, MinorLevel, MinorLevelUnits,ModerateLevel,ModerateLevelUnits,MajorLevel,MajorLevelUnits,ActionFlow,ActionFlowUnits,MinorFlow,MinorFlowUnits,ModerateFlow,ModerateFlowUnits,MajorFlow,MajorFlowUnits,geo_lat,geo_long)

    # print(water)

    result = water.WriteWaterReading()

def CollectWaterData():

    stations = StationsReadings.GetStations()

    for station in stations:
        print(station.station_code, station.station_description) 
        WaterLevelRssParse(station.station_code)

    