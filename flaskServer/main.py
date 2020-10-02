from flask import Flask, jsonify, render_template, request, send_from_directory
# from flask_cors import CORS

from nba_api.stats.static.players import find_players_by_full_name
from nba_api.stats.static.teams import find_team_by_abbreviation

from database import db_session
from models import Player, individualSC, playerLeagueSC, playerShotStats,twoSC,gameLog
from dbUpdate import Update

app = Flask('__name__')
# cors = CORS(app) # have the proxy set up, don't need cors
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/team-info/<string:home>/<string:away>/', methods=['GET','POST'])
def getTeamInfo(home,away):
    with app.app_context():
        homeInfo = find_team_by_abbreviation(home)
        awayInfo = find_team_by_abbreviation(away)
        response = jsonify(home=homeInfo,away=awayInfo)
    return response

@app.route('/api/player-info/<string:player_name>/', methods = ['GET','POST'])
def getPlayerInfo(player_name):
    with app.app_context():
        playerInfo = find_players_by_full_name(player_name)[0]
        response = jsonify(playerInfo)
        return response

@app.route('/api/players',methods = ['GET','POST'])
def getPlayers():
    with app.app_context():
        ps = Player.query.all()
        players = [p.name for p in ps]
        response = jsonify(players = players)
    return response


@app.route('/api/player-sc/<string:player_name>/', methods = ['GET','POST'])
def getPlayerSC(player_name):
    with app.app_context():
        pName = find_players_by_full_name(player_name)[0]['full_name']
        try:
            soloSC = ((individualSC.query.filter(individualSC.name == pName).first()).shotChart).decode('utf-8')
            compSC = ((playerLeagueSC.query.filter(playerLeagueSC.name == pName).first()).shotChart).decode('utf-8')
        
        except AttributeError: 
            add = Update(pName)
            add.addPlayer(); add.addPlayerSC(); add.addPlayerLeagueSC();
            soloSC = ((individualSC.query.filter(individualSC.name == pName).first()).shotChart).decode('utf-8')
            compSC = ((playerLeagueSC.query.filter(playerLeagueSC.name == pName).first()).shotChart).decode('utf-8')
        

        leagueTable = (playerShotStats.query.filter(playerShotStats.name == 'League').all())
        playerTable = (playerShotStats.query.filter(playerShotStats.name == pName).all())
        Lszb, Lsza, Lszr, Lfgpct = [],[],[],[]
        Pszb, Psza, Pszr, Pfgpct = [],[],[],[]
        if len(playerTable) >= len(leagueTable):
            for i in range(0,len(leagueTable),1):
                Lszb += [leagueTable[i].shot_zone_basic]; Pszb += [playerTable[i].shot_zone_basic]
                Lsza += [leagueTable[i].shot_zone_area]; Psza += [playerTable[i].shot_zone_area]
                Lszr += [leagueTable[i].shot_zone_range]; Pszr += [playerTable[i].shot_zone_range]
                Lfgpct += [leagueTable[i].fg_pct]; Pfgpct += [playerTable[i].fg_pct]
                
        elif len(playerTable) < len(leagueTable):
            for i in range(0,len(playerTable),1):
                Pszb += [playerTable[i].shot_zone_basic]
                Psza += [playerTable[i].shot_zone_area]
                Pszr += [playerTable[i].shot_zone_range]
                Pfgpct += [playerTable[i].fg_pct]
            # for i in range(0,len(leagueTable),1):
                Lszb += [leagueTable[i].shot_zone_basic]
                Lsza += [leagueTable[i].shot_zone_area]
                Lszr += [leagueTable[i].shot_zone_range]
                Lfgpct += [leagueTable[i].fg_pct]

        pdf = [Pszb,Psza,Pszr,Pfgpct]; ldf = [Lszb,Lsza,Lszr,Lfgpct]
        
        # print(leagueTable)
        response = jsonify(soloSC=soloSC,playerLeagueSC=compSC,name = pName,pdf=pdf,ldf=ldf)
        
    return response


@app.route('/api/getCompSc/<string:player1>/<string:player2>')
def getCompSc(player1,player2):
    with app.app_context():
        plist =[row.secondPlayer for row in (twoSC.query.filter(twoSC.firstPlayer == player1).all())]
        # print(plist)
        if player2 in plist:

            compSC = (twoSC.query.filter(twoSC.firstPlayer == player1, 
                                        twoSC.secondPlayer == player2).first().shotChart).decode('utf-8')

        if player2 not in plist:
            plist = [row.secondPlayer for row in (twoSC.query.filter(twoSC.firstPlayer == player2).all())]
            compSC = (twoSC.query.filter(twoSC.firstPlayer == player2,
                                        twoSC.secondPlayer == player1).first().shotChart).decode('utf-8')

        response = jsonify(shotChart=compSC)
    return response


@app.route('/api/player-shooting-stats/<string:player>')
def getPlayerShootingStats(player):
    with app.app_context():
        pName = find_players_by_full_name(player)[0]['full_name']
        playerTable = (playerShotStats.query.filter(playerShotStats.name == pName).all())
        Pszb, Psza, Pszr, Pfgpct = [],[],[],[]
        for i in range(0,len(playerTable),1):
            Pszb += [playerTable[i].shot_zone_basic]
            Psza += [playerTable[i].shot_zone_area]
            Pszr += [playerTable[i].shot_zone_range]
            Pfgpct += [playerTable[i].fg_pct]
        
        pdf = [Pszb,Psza,Pszr,Pfgpct]
        response = jsonify(pdf = pdf)

    return response


app.run(debug=True)
