
from nba_api.stats.static.players import find_players_by_full_name
from database import init_db,db_session
from models import individualSC, Player, playerLeagueSC
from lib.rawStatsNBA import plotPlayerSC, effplot
import base64
import os


class Update:

    def __init__(self,player_name):
        self.name, self.shortenedName, self.id = self.getPlayerInfo(player_name)
        self.image = 'C:/Users/pedja/Documents/Programming/StatsNBA/Application/flask-server/lib/images/playerSC/'+ self.shortenedName + '.jpeg'

    
    def getPlayerInfo(self,player_name):
        playerInfo = find_players_by_full_name(player_name)[0]
        name = playerInfo['full_name']
        id = playerInfo['id']
        shortenedName = name.replace(" ","")
        return name,shortenedName,id 

    def imageTo64(self,pathToFile):
        with open(pathToFile, 'rb') as image:
            im64 = base64.b64encode(image.read())
        return im64

    def addPlayer(self):
        newPlayer = Player(name=self.name,id=self.id)
        db_session.add(newPlayer)
        db_session.commit()
    
    def addPlayerSoloSC(self):
        plotPlayerSC(self.name)
        shotChart = self.imageTo64(pathToFile=self.image)
        newShotChart = individualSC(name=self.name,id=self.id,shotChart=shotChart)
        db_session.add(newShotChart)
        db_session.commit()
        os.remove(str(self.image))

    def addPlayerLeagueSC(self):
        effplot(self.name)
        sc = self.imageTo64(pathToFile=self.image)
        newSC = playerLeagueSC(name=self.name,id=self.id,shotChart=sc)
        db_session.add(newSC)
        db_session.commit()
        os.remove(str(self.image))

        






    




