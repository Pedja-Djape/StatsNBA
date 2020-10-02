from dbUpdate import Update
from models import gameLog;
from nba_api.stats.static.teams import get_teams
from nba_api.stats.endpoints.leaguegamefinder import LeagueGameFinder

t = get_teams()
teams = [{'id': team['id'], 'name': team['full_name']} for team in t]

# atlID = teams[0]['id']

toUpdate = Update('Luka Doncic')
# toUpdate.addGametoLog(atlID)
i = 1
for team in teams:
    teamID = team['id']
    toUpdate.addGametoLog(teamID=teamID)
    print('%d. %s ... ADDED' % (i,team['name']))
    i += 1












