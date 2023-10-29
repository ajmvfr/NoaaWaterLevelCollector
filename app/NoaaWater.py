from sqlalchemy.orm import Session
from . import models
from .database import get_db, SessionLocal
from sqlalchemy import func
# import datetime
from datetime import datetime
from .Utilities import compareFloatNumbers

class StationsReadings:
    def __init__(self, 
                 station_code: str, 
                 station_name:str,
                 station_no: str,
                 published_date: datetime,
                 observed_date: datetime, 
                 water_category: str,
                 water_level: float,
                 water_level_units: str,
                 water_flow: float, 
                 water_flow_units: str,
                 ActionLevel: float, 
                 ActionLevelUnits: str, 
                 MinorLevel: float, 
                 MinorLevelUnits: str,
                 ModerateLevel: float,
                 ModerateLevelUnits: str,
                 MajorLevel: float,
                 MajorLevelUnits: str,
                 ActionFlow: float,
                 ActionFlowUnits: str,
                 MinorFlow: float,
                 MinorFlowUnits: str,
                 ModerateFlow: float,
                 ModerateFlowUnits: str,
                 MajorFlow: float,
                 MajorFlowUnits: str,
                 latitude: float,
                 longitude: float):

        # Assign to self object
        self.station_code = station_code
        self.station_name = station_name
        self.station_no = station_no
        self.published_date = published_date
        self.observed_date = observed_date
        self.water_category = water_category
        self.water_level = water_level
        self.water_level_units = water_level_units
        self.water_flow = water_flow
        self.water_flow_units = water_flow_units
        self.ActionLevel = ActionLevel
        self.ActionLevelUnits =  ActionLevelUnits
        self.MinorLevel =  MinorLevel
        self.MinorLevelUnits = MinorLevelUnits
        self.ModerateLevel = ModerateLevel
        self.ModerateLevelUnits = ModerateLevelUnits
        self.MajorLevel = MajorLevel
        self.MajorLevelUnits = MajorLevelUnits
        self.ActionFlow = ActionFlow
        self.ActionFlowUnits = ActionFlowUnits
        self.MinorFlow = MinorFlow
        self.MinorFlowUnits = MinorFlowUnits
        self.ModerateFlow = ModerateFlow
        self.ModerateFlowUnits = ModerateFlowUnits
        self.MajorFlow = MajorFlow
        self.MajorFlowUnits = MajorFlowUnits
        self.latitude = latitude
        self.longitude = longitude


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.station_code}', '{self.station_name}', '{self.station_no}', {self.published_date}, {self.observed_date}, '{self.water_category}', {self.water_level}, '{self.water_level_units}', {self.water_flow}, '{self.water_flow_units}', {self.ActionLevel},'{self.ActionLevelUnits}', {self.MinorLevel}, '{self.MinorLevelUnits}',{self.ModerateLevel},'{self.ModerateLevelUnits}',{self.MajorLevel},'{self.MajorLevelUnits}',{self.ActionFlow},'{self.ActionFlowUnits}',{self.MinorFlow},'{self.MinorFlowUnits}',{self.ModerateFlow},'{self.ModerateFlowUnits}',{self.MajorFlow},'{self.MajorFlowUnits}',{self.latitude}, {self.longitude})"


    def WriteWaterReading(self):


        db = SessionLocal()

        StationReturn = self.MaintainStation()
        print(f'updated station: {StationReturn}')

        Water_Check = db.query(models.WaterReport).filter(models.WaterReport.station_code == self.station_code, models.WaterReport.published_date == self.published_date).first()
        if Water_Check == None: # if record does not exist, add a new one.  othersiwe skip
            New_Water = models.WaterReport(self.station_code, self.published_date, self.observed_date, self.water_category, self.water_level, self.water_level_units, self.water_flow, self.water_flow_units, StationReturn.id)
            # New_Water.WriteDb(db)
            db.add(New_Water)  # insert into DB
            db.commit()  # commit to DB
            db.refresh(New_Water)  # get post that was just written
            print(New_Water)

        db.close()
        return self

    def MaintainStation(self):

        updated = False
        UpdateDict = {}
        db = SessionLocal()

        Station_Query = db.query(models.Station).filter(models.Station.station_code == self.station_code)
        Station_Check = Station_Query.first()

        if Station_Check == None: # if record does not exist, add a new one.  othersiwe skip
            New_Station = models.Station(self.station_no, self.station_code, self.station_name, self.ActionLevel,self.ActionLevelUnits, self.MinorLevel, self.MinorLevelUnits,self.ModerateLevel,self.ModerateLevelUnits,self.MajorLevel,self.MajorLevelUnits,self.ActionFlow,self.ActionFlowUnits,self.MinorFlow,self.MinorFlowUnits,self.ModerateFlow,self.ModerateFlowUnits,self.MajorFlow,self.MajorFlowUnits,self.latitude, self.longitude)
            # New_Water.WriteDb(db)
            db.add(New_Station)  # insert into DB
            db.commit()  # commit to DB
            db.refresh(New_Station)  # get post that was just written
            db.close()
            return New_Station
        else:
            if compareFloatNumbers(Station_Check.station_no, self.station_no) == False and self.station_no != None:
                UpdateDict.update({'station_no' : self.station_no})    
                updated = True     

            if Station_Check.station_description != self.station_name and self.station_name != None:
                UpdateDict.update({'station_description' : self.station_name})    
                updated = True  

            if compareFloatNumbers(Station_Check.ActionLevel, self.ActionLevel) == False and self.ActionLevel != None:
                UpdateDict.update({'ActionLevel' : self.ActionLevel})        
                updated = True       

            if Station_Check.ActionLevelUnits != self.ActionLevelUnits and self.ActionLevelUnits != None:
                UpdateDict.update({'ActionLevelUnits' : self.ActionLevelUnits})  
                updated = True    

            if compareFloatNumbers(Station_Check.ActionFlow, self.ActionFlow)  == False   and self.ActionFlow != None:
                UpdateDict.update({'ActionFlow' : self.ActionFlow})   
                updated = True     
                      
            if Station_Check.ActionFlowUnits != self.ActionFlowUnits and self.ActionFlowUnits != None:
                Station_Query.update({'ActionFlowUnits' : self.ActionFlowUnits}) 
                updated = True    

            if compareFloatNumbers(Station_Check.MinorLevel, self.MinorLevel) == False and self.MinorLevel != None:
                UpdateDict.update({'MinorLevel' : self.MinorLevel})    
                updated = True      

            if Station_Check.MinorLevelUnits != self.MinorLevelUnits and self.ActionLevel != None:
                Station_Query.update({'MinorLevelUnits' : self.MinorLevelUnits})
                updated = True     

            if compareFloatNumbers(Station_Check.MinorFlow, self.MinorFlow) == False and self.MinorFlow != None:
                UpdateDict.update({'MinorFlow' : self.MinorFlow})      
                updated = True    

            if Station_Check.MinorFlowUnits != self.MinorFlowUnits and self.MinorFlowUnits != None:
                UpdateDict.update({'MinorFlowUnits' : self.MinorFlowUnits})  
                updated = True     

            if compareFloatNumbers(Station_Check.ModerateLevel, self.ModerateLevel) == False and self.ModerateLevel != None:
                UpdateDict.update({'ModerateLevel' : self.ModerateLevel})  
                updated = True     

            if Station_Check.ModerateLevelUnits != self.ModerateLevelUnits and self.ModerateLevelUnits != None:
                UpdateDict.update({'ModerateLevelUnits' : self.ModerateLevelUnits}) 
                updated = True    

            if compareFloatNumbers(Station_Check.ModerateFlow, self.ModerateFlow) == False and self.ModerateFlow != None:
                UpdateDict.update({'ModerateFlow' : self.ModerateFlow})      
                updated = True  

            if Station_Check.ModerateFlowUnits != self.ModerateFlowUnits and self.ModerateFlowUnits != None:
                UpdateDict.update({'ModerateFlowUnits' : self.ModerateFlowUnits}) 
                updated = True 

            if compareFloatNumbers(Station_Check.MajorLevel, self.MajorLevel) == False and self.MajorLevel != None:
                UpdateDict.update({'MajorLevel' : self.MajorLevel})    
                updated = True   

            if Station_Check.MajorLevelUnits != self.MajorLevelUnits and self.MajorLevelUnits != None:
                UpdateDict.update({'MajorLevelUnits' : self.MajorLevelUnits})  
                updated = True  

            if compareFloatNumbers(Station_Check.MajorFlow, self.MajorFlow) == False and self.MajorFlow != None:
                UpdateDict.update({'MajorFlow' : self.MajorFlow})    
                updated = True  

            if Station_Check.MajorFlowUnits != self.MajorFlowUnits and self.MajorFlowUnits != None:
                UpdateDict.update({'MajorFlowUnits' : self.MajorFlowUnits})  
                updated = True  

            if compareFloatNumbers(Station_Check.latitude, self.latitude) == False and self.latitude != None:
                UpdateDict.update({'latitude' : self.latitude})   
                updated = True    

            if compareFloatNumbers(Station_Check.longitude, self.longitude) == False and self.longitude != None:
                UpdateDict.update({'longitude' : self.longitude}) 
                updated = True  

            if len(UpdateDict) > 0:
                UpdateDict.update({'modified_on' : datetime.now()}) 
                updated = True  
                Station_Query.update(UpdateDict, synchronize_session=False)
                db.commit()
                db.close()
                return Station_Query.first()
            else:
                db.close()
                return Station_Check
            
        

        

    @staticmethod
    def GetStations():

        db = SessionLocal()

        stations = db.query(models.Station).all()

        db.close()

        return stations





