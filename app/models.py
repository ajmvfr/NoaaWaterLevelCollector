from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base, SessionLocal

import datetime

class Station(Base):
    __tablename__ = "station"
    id = Column(Integer, primary_key=True, nullable=False)
    station_no = Column(Integer, nullable=True)
    station_code = Column(String, nullable=False, unique=True)
    station_description = Column(String, nullable=True)
    ActionLevel = Column(Float, nullable=True)
    ActionLevelUnits = Column(String, nullable=True)
    MinorLevel = Column(Float, nullable=True)
    MinorLevelUnits = Column(String, nullable=True)
    ModerateLevel= Column(Float, nullable=True)
    ModerateLevelUnits = Column(String, nullable=True)
    MajorLevel = Column(Float, nullable=True)
    MajorLevelUnits = Column(String, nullable=True)
    ActionFlow = Column(Float, nullable=True)
    ActionFlowUnits = Column(String, nullable=True)
    MinorFlow = Column(Float, nullable=True)
    MinorFlowUnits = Column(String, nullable=True)
    ModerateFlow = Column(Float, nullable=True)
    ModerateFlowUnits = Column(String, nullable=True)
    MajorFlow = Column(Float, nullable=True)
    MajorFlowUnits = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    created_on = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    modified_on = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    def __init__(self, 
                 station_no: int, 
                 station_code: str, 
                 station_description: str,
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

        self.station_no = station_no
        self.station_code = station_code
        self.station_description = station_description
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
        return f"{self.__class__.__name__}({self.id}, {self.station_no}, '{self.station_code}', '{self.station_description}', {self.ActionLevel},'{self.ActionLevelUnits}', {self.MinorLevel}, '{self.MinorLevelUnits}',{self.ModerateLevel},'{self.ModerateLevelUnits}',{self.MajorLevel},'{self.MajorLevelUnits}',{self.ActionFlow},'{self.ActionFlowUnits}',{self.MinorFlow},'{self.MinorFlowUnits}',{self.ModerateFlow},'{self.ModerateFlowUnits}',{self.MajorFlow},'{self.MajorFlowUnits}',{self.latitude}, {self.longitude}, {self.created_on}, {self.modified_on})"
    


class WaterReport(Base):
    __tablename__ = "water_report"
    id = Column(Integer, primary_key=True, nullable=False)
    station_code = Column(String, nullable=False)
    published_date = Column(TIMESTAMP(timezone=True), nullable=False)
    observed_date = Column(TIMESTAMP(timezone=True), nullable=False)
    water_category = Column(String, nullable=True)
    water_level = Column(Float, nullable=True)
    water_level_units = Column(String, nullable=True)
    water_flow = Column(Float, nullable=True)
    water_flow_units = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    station_id = Column(Integer, ForeignKey(
        "station.id", ondelete="CASCADE"), nullable=False)
    # raw = Column(String, nullable=True)
    
    def __init__(self, 
                 station_code: str, 
                 published_date: datetime, 
                 observed_date: datetime,
                 water_category: str,
                 water_level: float,
                 water_level_units: str,
                 water_flow: float,
                 water_flow_units: str,
                 station_id: int):


        # Assign to self object
        self.station_code = station_code
        self.published_date = published_date
        self.observed_date = observed_date
        self.water_category = water_category
        self.water_level = water_level
        self.water_level_units = water_level_units
        self.water_flow = water_flow
        self.water_flow_units = water_flow_units
        self.station_id = station_id


    def __repr__(self):
        return f"{self.__class__.__name__}({self.id},'{self.station_code}', {self.published_date}, {self.observed_date}, '{self.water_category}', {self.water_level}, '{self.water_level_units}', {self.water_flow}, '{self.water_level_units}', {self.created_at}, {self.station_id})"
    


