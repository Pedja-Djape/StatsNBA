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

    firstPlayer = Column(String(250),primary_key=True)
    secondPlayer = Column(String(250),primary_key=True)
    shotChart = Column(BLOB)

    def __init__(self,firstPlayer=None,secondPlayer=None,shotChart=None):
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer
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

class gameLog(Base):
    __tablename__ = 'gamelog'

    team = Column(String(250),nullable=False)
    gameID = Column(String(250),nullable=False)
    fgPct = Column(Float,primary_key = True)
    pct3 = Column(Float,primary_key = True)
    ftpct = Column(Float,primary_key = True)
    oReb = Column(Integer,primary_key=True)
    dReb = Column(Integer,primary_key=True)
    ast = Column(Integer,primary_key=True)
    stl = Column(Integer,primary_key=True)
    blk = Column(Integer,primary_key=True)
    turnO = Column(Integer,primary_key=True)
    pts = Column(Integer,primary_key=True)
    isHome = Column(Integer,primary_key=True)
    didWin = Column(Integer,primary_key=True)

    def __init__(self,team=None,gameID = None,fgpct=None,pct3=None,ftpct=None,oReb=None,dReb=None,
    ast=None,stl=None,blk=None,turnO=None,pts=None,isHome=None,didWin=None):
        self.team = team
        self.gameID = gameID
        self.fgPct = fgpct
        self.pct3 = pct3
        self.ftpct = ftpct
        self.oReb = oReb
        self.dReb = dReb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.turnO = turnO
        self.pts = pts
        self.isHome = isHome
        self.didWin = didWin






    