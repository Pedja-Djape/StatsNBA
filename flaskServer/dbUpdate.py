
from nba_api.stats.static.players import find_players_by_full_name
from nba_api.stats.endpoints.leaguegamefinder import LeagueGameFinder
from database import init_db,db_session
from models import individualSC, Player, playerLeagueSC, playerShotStats, twoSC, gameLog
from lib.rawStatsNBA import plotPlayerSC, effplot, genEffPlayerShotDF, getShotsDFs, getCareerShotDF,playerShotComp
import base64
import os
from numpy import arange

leagueDF = getShotsDFs('luka doncic','dallas mavericks')[1]


class Update:

    def __init__(self,player_name):
        self.name, self.shortenedName, self.id = self.getPlayerInfo(player_name)
        self.soloImage = 'C:/Users/pedja/Documents/Programming/StatsNBA/Application/flask-server/lib/images/playerSC/'+ self.shortenedName + '.jpeg'
        self.duoImage = 'C:/Users/pedja/Documents/Programming/StatsNBA/Application/flask-server/lib/images/twoPlayerSCs/' + self.shortenedName
    
    def getPlayerInfo(self,player_name):
        if player_name == 'League':
            name = 'League'
            id = 0
            shortenedName = 'League'
        else:
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
        shotChart = self.imageTo64(pathToFile=self.soloImage)
        newShotChart = individualSC(name=self.name,id=self.id,shotChart=shotChart)
        db_session.add(newShotChart)
        db_session.commit()
        os.remove(str(self.soloImage))

    def addPlayerLeagueSC(self):
        effplot(self.name)
        sc = self.imageTo64(pathToFile=self.soloImage)
        newSC = playerLeagueSC(name=self.name,id=self.id,shotChart=sc)
        db_session.add(newSC)
        db_session.commit()
        os.remove(str(self.soloImage))
    
    def addPlayerComp(self,otherPlayer):
        second = find_players_by_full_name(otherPlayer)[0]['full_name']
        playerShotComp(self.name,second)
        tmp = second.replace(" ", "")
        self.duoImage += tmp + '.jpeg'
        dualSC = self.imageTo64(pathToFile=self.duoImage)
        addition = twoSC(firstPlayer=self.name,secondPlayer=second,shotChart=dualSC)
        db_session.add(addition)
        db_session.commit()
        os.remove(str(self.duoImage))

    def addPlayerShotStats(self):
        if self.name == 'League':
            for i in range(0,len(leagueDF)):
                basic = (leagueDF['SHOT_ZONE_BASIC'].values)[i]
                area = (leagueDF['SHOT_ZONE_AREA'].values)[i]
                rng = (leagueDF['SHOT_ZONE_RANGE'].values)[i]
                pct = (leagueDF['FG_PCT'].values)[i]
                statsForLoc = playerShotStats(name=self.name,shot_zone_area=area,shot_zone_basic=basic,shot_zone_range=rng,fg_pct=pct)
                db_session.add(statsForLoc)
                db_session.commit()
        else:
            pdf = genEffPlayerShotDF(getCareerShotDF(self.name),leagueDF)
            for i in range(0, len(pdf)):
                basic = (pdf['SHOT_ZONE_BASIC'].values)[i]
                area = (pdf['SHOT_ZONE_AREA'].values)[i]
                rng = (pdf['SHOT_ZONE_RANGE'].values)[i]
                pct = (pdf['FG_PCT'].values)[i]
                statsForLoc = playerShotStats(name=self.name,shot_zone_area=area,shot_zone_basic=basic,shot_zone_range=rng,fg_pct=pct)
                db_session.add(statsForLoc)
                db_session.commit()

    def addGametoLog(self,teamID):
        games = LeagueGameFinder(team_id_nullable=teamID).get_data_frames()[0]
        idxToDrop = [None]*3
        for idx,row in games.iterrows():
            if (row['GAME_DATE'] == '2019-10-22'):
                idxToDrop[0] = ['2019-10-22',idx]
            elif (row['GAME_DATE'] == '2019-10-23'):
                idxToDrop[1] = ['2019-10-23',idx]
            elif (row['GAME_DATE'] == '2019-10-24'):
                idxToDrop[2] = ['2019-10-24',idx]
        found = False
        i = 0
        while not found:
            if idxToDrop[i] == None:
                i +=1
                continue
            elif idxToDrop != None:
                found = True
        games = games.iloc[0:idxToDrop[i][1]+1]
        games = games.reindex(index=games.index[::-1])
        games = games.iloc[0:40]
        games.index = arange(0,40,1)
        # print(games)
        for i in range(0,len(games)):
            team = (games['TEAM_NAME'].values)[i]
            gameID = (games['GAME_ID'].values)[i]
            fgPct = (games['FG_PCT'].values)[i]
            pct3  = (games['FG3_PCT'].values)[i]
            ftpct = (games['FT_PCT'].values)[i]
            oReb = (games['OREB'].values)[i]
            dReb = (games['DREB'].values)[i]
            ast = (games['AST'].values)[i]
            stl = (games['STL'].values)[i]
            blk = (games['BLK'].values)[i]
            turnO = (games['TOV'].values)[i]
            pts = (games['PTS'].values)[i]
            
            if (games['MATCHUP'].values)[i][4] == '@':
                isHome = 0
            elif (games['MATCHUP'].values)[i][4] == 'v':
                isHome = 1
            
            if (games['WL'].values)[i] == 'W':
                didWin = 1
            elif (games['WL'].values)[i] == 'L':
                didWin = -1
            myBoxScore = gameLog(team=team,gameID=gameID,fgpct=fgPct,pct3=pct3,ftpct=ftpct,oReb=oReb,dReb=dReb,ast=ast,stl=stl,
            blk=blk,turnO=turnO,pts=pts,isHome=isHome,didWin=didWin)
            db_session.add(myBoxScore)
            db_session.commit()

        






    




