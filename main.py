from app import models
from app.database import engine
from app.config import settings
from app.WaterLevelRssParse import WaterLevelRssParse, CollectWaterData
import time

# models.Base.metadata.create_all(bind=engine)

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
