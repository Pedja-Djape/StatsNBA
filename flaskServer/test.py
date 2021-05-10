from dbUpdate import Update
from models import gameLog;
from nba_api.stats.static.teams import get_teams
from nba_api.stats.endpoints.leaguegamefinder import LeagueGameFinder
import numpy as np
import torch

t = get_teams()
teams = [{'id': team['id'], 'name': team['full_name']} for team in t]

atlID = teams[0]['id']

# toUpdate = Update('Luka Doncic')
# # toUpdate.addGametoLog(atlID)
# i = 1
# for team in teams:
#     teamID = team['id']
#     toUpdate.addGametoLog(teamID=teamID)
#     print('%d. %s ... ADDED' % (i,team['name']))
#     i += 1

games = LeagueGameFinder(team_id_nullable=atlID).get_data_frames()[0]
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
games.index = np.arange(0,40,1)
data = []
team = np.reshape(games['TEAM_NAME'].values,(40,1))
gameID = np.reshape(games['GAME_ID'].values,(40,1))
fgpct = np.reshape(games['FG_PCT'].values,(40,1)).astype(float)
pct3 = np.reshape(games['FG3_PCT'].values,(40,1)).astype(float)
ftpct = np.reshape(games['FT_PCT'].values,(40,1)).astype(float)
oReb = np.reshape(games['OREB'].values,(40,1)).astype(float)
dReb = np.reshape(games['DREB'].values,(40,1)).astype(float)
ast = np.reshape(games['AST'].values,(40,1)).astype(float)
stl = np.reshape(games['STL'].values,(40,1)).astype(float)
blk = np.reshape(games['BLK'].values,(40,1)).astype(float)
turnO = np.reshape(games['TOV'].values,(40,1)).astype(float)
pts = np.reshape(games['PTS'].values,(40,1)).astype(float)
isHome = []; didWin = []
for i in range(0,40,1):
    if (games['MATCHUP'].values)[i][4] == '@':
        isHome += [0]
    elif (games['MATCHUP'].values)[i][4] == 'v':
        isHome += [1]
    
    if (games['WL'].values)[i] == 'W':
        didWin += [1]
    elif (games['WL'].values)[i] == 'L':
        didWin += [-1] 
isHome = np.reshape(np.array(isHome),(40,1)).astype(float)
didWin = np.reshape(np.array(didWin),(40,1)).astype(float)
c = np.column_stack((team,gameID,fgpct,pct3,ftpct,oReb,dReb,ast,stl,blk,turnO,pts,isHome))

td = c[:,2:]
print(td.dtype)
td = torch.from_numpy(td).float()

tl = np.reshape(c[:,-1],(40,1))
tl = torch.from_numpy(tl).float()



import ML.nnLib as lib 


net = lib.NeuralNetwork()

netOut = lib.train(td,tl,net)

# for i in range(0,len(games)):
#     team = (games['TEAM_NAME'].values)[i]
#     gameID = (games['GAME_ID'].values)[i]
#     fgPct = (games['FG_PCT'].values)[i]
#     pct3  = (games['FG3_PCT'].values)[i]
#     ftpct = (games['FT_PCT'].values)[i]
#     oReb = (games['OREB'].values)[i]
#     dReb = (games['DREB'].values)[i]
#     ast = (games['AST'].values)[i]
#     stl = (games['STL'].values)[i]
#     blk = (games['BLK'].values)[i]
#     turnO = (games['TOV'].values)[i]
#     pts = (games['PTS'].values)[i]
    
    # if (games['MATCHUP'].values)[i][4] == '@':
    #     isHome = 0
    # elif (games['MATCHUP'].values)[i][4] == 'v':
    #     isHome = 1
    
    # if (games['WL'].values)[i] == 'W':
    #     didWin = 1
    # elif (games['WL'].values)[i] == 'L':
    #     didWin = -1 
    
#     data += [[team,gameID,fgPct,pct3,ftpct,oReb,dReb,ast,stl,blk,turnO,pts,isHome]]

# data = np.array(data)
# print(data)
# print(data.shape)












