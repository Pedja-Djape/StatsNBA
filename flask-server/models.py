from sqlalchemy import Column, Integer, String, BLOB, Float
from database import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id
""""""

class individualSC(Base):
    __tablename__ = 'individualsc'

    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    shotChart = Column(BLOB)

    def __init__(self, id=None, shotChart = None, name=None):
        self.id = id
        self.shotChart = shotChart
        self.name = name
""""""
class playerLeagueSC(Base):
    __tablename__ = 'playerleaguesc'

    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    shotChart = Column(BLOB) 

    def __init__(self, id=None, shotChart = None, name=None):
        self.id = id
        self.shotChart = shotChart
        self.name = name


class twoSC(Base):
    __tablename__ = 'twosc'

    firstID = Column(Integer,primary_key=True)
    secondID = Column(Integer,primary_key=True)
    shotChart = Column(BLOB)

    def __init__(self,firstID=None,secondID=None,shotChart=None):
        self.firstID = firstID
        self.secondID = secondID
        self.shotChart = shotChart
""""""
class playerShotStats(Base):
    __tablename__ = 'playershotstats'

    name = Column(String(250), nullable=False)
    shot_zone_basic = Column(String(250), nullable=False)
    shot_zone_area = Column(String(250), nullable=False)
    shot_zone_range = Column(String(250), nullable=False)
    fg_pct = Column(Float,primary_key=True)


    def __init__(self, name=None,shot_zone_basic=None,shot_zone_area=None,shot_zone_range=None,fg_pct=None):
        self.name = name
        self.shot_zone_basic = shot_zone_basic
        self.shot_zone_area = shot_zone_area
        self.shot_zone_range = shot_zone_range
        self.fg_pct = fg_pct

    




    