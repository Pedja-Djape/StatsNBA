from sqlalchemy import Column, Integer, String, BLOB
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




    