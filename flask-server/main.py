from flask import Flask, jsonify, render_template, request, send_from_directory
# from flask_cors import CORS

from nba_api.stats.static.players import find_players_by_full_name
from nba_api.stats.static.teams import find_team_by_abbreviation

from database import db_session
from models import Player, individualSC, playerLeagueSC
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
        response = jsonify(soloSC=soloSC,playerLeagueSC=compSC,name = pName)
        
    return response







app.run(debug=True)
