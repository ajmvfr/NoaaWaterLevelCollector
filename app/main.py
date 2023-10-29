from . import models
from .database import engine
from .config import settings
from .WaterLevelRssParse import WaterLevelRssParse, CollectWaterData
import time

models.Base.metadata.create_all(bind=engine)

CollectWaterData()
# WaterLevelRssParse('BEAP1')
# WaterLevelRssParse('PNEP1')
# WaterLevelRssParse('prvp1')
# WaterLevelRssParse('mgyp1')
# WaterLevelRssParse('dshp1')
# WaterLevelRssParse('pttp1')


# BEAP1
# MGYP1
# DSHP1
# PTTP1
