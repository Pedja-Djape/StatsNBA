from dbUpdate import Update

from nba_api.stats.endpoints.leagueleaders import LeagueLeaders


allPlayers = LeagueLeaders().get_data_frames()[0]



for i in range(0,208,1):
    
    playerName = (allPlayers.iloc[i]['PLAYER'])
    newPLayer = Update(playerName)
    # newPLayer.addPlayer()
    # newPLayer.addPlayerLeagueSC()
    newPLayer.addPlayerShotStats()
    print(str(i+1) + ". Added %s" % (playerName))







