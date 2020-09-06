# import mysql.connector as mysql
import numpy as np 
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
# from matplotlib.patches import RegularPolygon
# import PIL as Pillow
# from PIL import Image
# from matplotlib.colors import ListedColormap,ColorConverter, LinearSegmentedColormap, Normalize
# import matplotlib.colors as mcolors
# from matplotlib.patches import Circle, Rectangle, Arc
# from . import polytest as zone





# db = mysql.connect(
#     host = "localhost",
#     user = 'root',
#     password = ,
#     database = "nba" 
# )# point to 'nba' database 

# # creating an instance of 'cursor' class to execute the SQL queries 
# mycursor = db.cursor()

from nba_api.stats.static.players import find_players_by_full_name
from nba_api.stats.static.teams import *
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail


from shapely.geometry import LineString
from matplotlib.patches import Rectangle

def paintC816(side,ax,color):
    x = np.arange(start = -80,stop = 80.0,step = 1e-2)
    yArc = np.sqrt(80**2 - x**2) 
    yLL = -2*x - 17.5
    yRL = 2*x - 17.5
    yTop = 0*x + 142.5

    filtM1 = yArc < yTop
    filtM2 = yArc > yLL
    filtM3 = yArc > yRL
    filtM = filtM1 & filtM2 & filtM3
    ax.fill_between(x,yArc,yTop, where = filtM,color = color,alpha = 1.,edgecolor = None)
    from shapely.geometry import LineString
    arcls = LineString(np.column_stack((x,yArc))); lls = LineString(np.column_stack((x,yLL)))
    xi,yi = (arcls.intersection(lls).xy)[0][0],(arcls.intersection(lls).xy)[1][0]

    triangleLx = [xi,-80,xi,xi]; triangleLy = [yi,142.5,142.5,yi];
    triangleRx = [-xi,80,-xi,-xi]; triangleRy = [yi,142.5,142.5,yi];
    ax.fill(triangleLx,triangleLy,color = color,alpha = 1.);ax.fill(triangleRx,triangleRy,color = color,alpha = 1.)

    return True

def paintC8(side,ax,color):

    ux = np.arange(start = -80,stop = 80,step = 1e-2)
    uArc = np.sqrt(80**2 - (ux)**2)
    lx = np.arange(start = -40,stop = 40,step = 1e-2)
    lArc = np.sqrt(40**2 - (lx)**2)

    fx2 = [];fx3 = [];
    fy1= [];fy2 = [];fy3 = [];
    for i in range(0,len(ux)):
        if ux[i] >= -40 and ux[i] <= 40:
            fy1 += [uArc[i]]
        elif ux[i] >= -80 and ux[i] < -40:
            fx2 += [ux[i]]
            fy2 += [uArc[i]]
        elif ux[i] > 40 and ux[i] <= 80:
            fx3 += [ux[i]]
            fy3 += [uArc[i]]
    zeros = len(fx2)*[0]
    ax.fill_between(lx,fy1,lArc,where = fy1 > lArc,color = color,alpha = 1.)
    ax.fill_between(fx2,fy2,zeros,where = fy2 > zeros,color = color,alpha = 1.)
    ax.fill_between(fx3,fy3,zeros,where = fy3 > zeros,color = color,alpha = 1.)

    return True

def paintl8(side,ax,color):
    if side == 'L' or side == 'l':
        arcxn = np.arange(start = -80,stop = -40,step = 1e-2)
        arcy = np.sqrt(80**2 - (arcxn)**2)
        yn = -2*arcxn - 17.5
        ax.fill_between(arcxn,arcy,yn,where = yn >= arcy,color = color,alpha = 1.)
    elif side == 'R' or side == 'r':
        arcxp = np.arange(start = 40,stop = 80,step = 1e-2)
        arcpy = np.sqrt(80**2 - (arcxp)**2)
        yr = 2*arcxp - 17.5
        ax.fill_between(arcxp,arcpy,yr,where = yr >= arcpy,color = color,alpha = 1.)

    return True

def rA(side,ax,color):
    x = np.arange(-40,40.01,step = 1e-2)
    circp = np.sqrt(40**2 - x**2); circn = -np.sqrt(40**2 - x**2)
    ax.fill_between(x,circp,circn,where = circp > circn,color= color,alpha = 1.)
    return True

def midC816(side,ax,color):
    x = np.arange(-80,80.01,step = 1e-2)
    arc16 = np.sqrt(160**2 - x**2)
    hori = 0*x + 142.5
    #ax.plot(x,arc16)
    ax.fill_between(x,hori,arc16,where = arc16>hori,color = color,alpha = 1.)
    return True

def midC1624(side,ax,color):
    x = np.arange(-115,115,step = 1e-2)
    arc24 = np.sqrt(240**2 - x**2); arc16 = np.sqrt(160**2 - x**2)
    yL = -2*x-17.5; yR = 2*x - 17.5
    # intersection points: (78.469,139.327) (114.274,211.155)
    ax.fill_between(x,arc24,arc16,where = (arc16<arc24) & (arc16 > yL) & (arc16>yR),color = color,alpha = 1.)

    xr = np.arange(78.46,114.29,step = 1e-2);yar = np.sqrt(240**2 - xr**2);ylr = 2*xr -17.5
    xl = np.arange(-114.27,-78.49); yal = np.sqrt(240**2 - xl**2); yll = -2*xl - 17.5
    ax.fill_between(xr,yar,ylr,where = yar > ylr,color = color,alpha = 1.); ax.fill_between(xl,yal,yll,where = yal > yll,color = color,alpha = 1.)

    return True

def LRS816(side,ax,color):
    lowerBound,outerBound = 0,0
    if side.upper() == 'L':
        lowerBound = -160
        upperBound = -80
        factor = -1
    elif side.upper() == 'R':
        lowerBound = 80
        upperBound = 160
        factor = 1

    x = np.arange(lowerBound,upperBound,step = 1e-2)
    arc = np.sqrt(160**2 - x**2)
    straight = x*0 - 47.5
    ax.fill_between(x,arc,straight,color = color, alpha = 1.)
    return True

def LRS1624(side,ax,color):

    if side == 'l' or side == 'L':
        factor = -1
        lower = -240;upper = -129 + 0.01
    elif side == 'R' or side == 'r':
        factor = 1
        lower = 129;upper = 240+0.01

    x = np.arange(lower,upper,step = 1e-2)
    line = (factor*8.1/11)*x - 1
    arcu = np.sqrt(240**2 - x**2); arcl = np.ones(len(arcu))
    intx = factor*193.734;inty = 141.659
    if factor == 1:
        for i in range(0,len(arcu)):
            if x[i] <= 160:
                arcl[i] = np.sqrt(160**2 - x[i]**2)
            if x[i] >= 220:
                arcl[i] = arcu[i] 
            if x[i] >= 128.4 and x[i] <= 193.73:
                arcu[i] = (8.1/11)*x[i] - 1
            if x[i] > 193.73:
                line[i] = arcu[i]
        ax.fill_between(x,arcl,arcu,where = (arcl<arcu) & (arcu>=line) ,color = color, alpha = 1.)
        xbox = np.arange(160,220.01,step = 1e-2); y1 = xbox*0 + 1 ; y2 = xbox*0 - 47.5
        ax.fill_between(xbox,y1,y2,color = color,alpha = 1.)
    elif factor == -1:
        for i in range(0,len(arcu)):
            if x[i] >= -160:
                arcl[i] = np.sqrt(160**2 - x[i]**2)
            if x[i] <= -220:
                arcl[i] = arcu[i] +1
            if x[i] <= -128.4 and x[i] >= -193.73:
                arcu[i] = -(8.1/11)*x[i] - 1
            if x[i] < -193.73:
                line[i] = arcu[i]
        ax.fill_between(x,arcl,arcu,where = (arcl <= arcu) & (arcu >=line),color = color, alpha = 1.)
        xbox = np.arange(-220,-160.01,step = 1e-2); y1 = xbox*0 + 1 ; y2 = xbox*0 - 47.5
        ax.fill_between(xbox,y1,y2,color = color,alpha = 1.)
        #ax.add_patch(Rectangle((-220,-47.5),width = (220-160),height = 48.4,color = color,alpha = 1.))
    return True

def LRSC1624(side,ax,color):
    if side == 'l' or side == 'L':
        factor = -1
        lower = -230;upper = -78.53 + 0.01
    elif side == 'R' or side == 'r':
        factor = 1
        lower = 78.53;upper = 230+0.01

    x = np.arange(lower,upper,step = 1e-2)
    arcu = np.sqrt(240**2 - x**2); arcl = np.ones(len(arcu))
    linel = factor*(8.1/11)*x - 1; lineu = factor*2*x - 17.5

    for i in range(0,len(x)):
        if (factor*x[i]) <= 160:
            arcl[i] = np.sqrt(160**2 - x[i]**2)
        if (factor*x[i]) > 129.25:
            arcl[i] = linel[i]
        if (factor*x[i]) > 78.48 and (factor*x[i]) < 114.25:
            arcu[i] = lineu[i] 
        if (factor*x[i]) < 193.9:
            linel[i] = arcu[i]
        if (factor*x[i]) > 114.25:
            lineu[i] = arcu[i]
        
    ax.fill_between(x,arcu,arcl,where = (arcu>=arcl) & (arcu>=lineu),color=color,alpha = 1.)
    # ax.plot(x,arcu,color = 'red')
    # ax.plot(x,arcl,color = 'blue')
    # ax.plot(x,linel,color = 'orange')
    # ax.plot(x,lineu,color = 'green')
    return True
# LRSC1624(side='l',ax = plt.gca(),color = 'red')

def cLR3(side,ax,color):
    if side == 'l' or side == 'L':
        factor = -1
        lower = -250;upper = -220 + 0.01
    elif side == 'R' or side == 'r':
        factor = 1
        lower = 220;upper = 250+0.01
    x = np.arange(lower,upper,step = 1e-2)
    y1 = 0*x + 92.;y2 = 0*x - 47.5
    ax.fill_between(x,y1,y2,color=color,alpha = 1.)
    return True

def LR3(side,ax,color):
    if side == 'l' or side == 'L':
        factor = -1
        lower = -250;upper = -220 + 0.01
        l = -220; u = -111.75 + 0.01
    elif side == 'R' or side == 'r':
        factor = 1
        lower = 220;upper = 250+0.01
        l = 111.75; u = 220 + 0.01

    xbox = np.arange(lower,upper,step = 1e-2)
    y1 = xbox*0 + 92.5; y2 = xbox*0 + 360
    ax.fill_between(xbox,y1,y2,color = color,alpha = 1.)
    x = np.arange(l,u,step = 1e-2)
    yline = factor*2*x - 17.5; arc = np.sqrt(240**2 - x**2)
    for i in range(len(yline)):
        if yline[i] > 360:
            yline[i] = 360
    ax.fill_between(x,yline,arc, color = color, alpha = 1.)
    return True

def c3(side,ax,color):
    x = np.arange(start = -188.75,stop = 188.76,step = 1e-2)
    yArc = np.sqrt(240**2 - x**2) 
    yLL = -2*x - 17.5
    yRL = 2*x - 17.5
    yTop = 0*x + 360
    ax.fill_between(x,yArc,yTop,where = (yArc<yTop) & (yArc>yLL) & (yArc>yRL),color = color,alpha = 1.)
    intx,inty = 114.274, 211.048; 
    tLx = [-intx,-intx,-188.75,-intx]; tLy=[inty,360,360,inty]
    tRx = [intx,intx,188.75,intx]; tRy=[inty,360,360,inty]
    ax.fill(tLx,tLy,color = color,alpha = 1.);ax.fill(tRx,tRy,color = color,alpha = 1.)
    # ax.plot(x,yLL,color = 'black',ls = 'dashed',lw = 1)
    # ax.plot(x,yRL,color = 'black',ls = 'dashed',lw = 1)
    # ax.plot(x,yTop,color = 'black',ls = 'dashed',lw = 1)
    # draw_court(outer_lines=True)
    # plt.show()
    return True


def outlineZone():
    ax = plt.gca()
    x = np.arange(-250,250.01,step = 1e-2);
    zero = (len(x)//2) + 1
    ################################################
    ax.plot(x[zero-18875:zero-4260],(x[zero-18875:zero-4260])*-2 - 17.5,color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero+4260:zero+18875],(x[zero+4260:zero+18875])*2 - 17.5,color = 'black',ls = 'dashed',lw = 1)
    ################################################
    ax.plot(x[zero-22000:zero+22000],np.sqrt(240**2 - (x[zero-22000:zero+22000])**2),color = 'black',ls = 'dashed',lw = 1)
    ################################################
    ax.plot(x,0*x + 360,color = 'black',ls = 'dashed',lw = 1)
    ################################################
    cornerL = np.linspace(-221.5,-221.5,num = 44000); ycornerL = np.linspace(-47.5,92.5,num = 44000)
    cornerR = np.linspace(221.5,221.5,num = 44000); ycornerR = np.linspace(-47.5,92.5,num = 44000)
    ax.plot(cornerL,ycornerL,color = 'black',ls = 'dashed',lw = 1); ax.plot(cornerR,ycornerR,color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero-25000:zero - 22000],(x[zero-25000:zero - 22000])*0 + 92.5,color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero+22000:zero + 25000],(x[zero-25000:zero - 22000])*0 + 92.5,color = 'black',ls = 'dashed',lw = 1)
    ##################################################
    ax.plot(x[zero - 16000:zero+16000],np.sqrt(160**2 - (x[zero - 16000:zero+16000])**2),color = 'black',ls = 'dashed',lw = 1)   
   #######################################################################################################
    sL = np.linspace(-160,-160,num = 32000); sR = np.linspace(160,160, num = 32000);sy = np.linspace(-47.5,0,num = 32000);
    ax.plot(sL,sy,color = 'black',ls = 'dashed',lw = 1); ax.plot(sR,sy,color = 'black',ls = 'dashed',lw = 1)
    ##################################################
    ax.plot(x[zero-4000:zero + 4000],np.sqrt(40**2 - (x[zero-4000:zero + 4000])**2),color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero-4000:zero + 4000],-np.sqrt(40**2 - (x[zero-4000:zero + 4000])**2),color = 'black',ls = 'dashed',lw = 1)
    ####################################################
    ax.plot(x[zero-8000:zero+8000],np.sqrt(80**2 - (x[zero-8000:zero+8000])**2),color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero-8000:zero-4000],(x[zero-8000:zero-4000])*0,color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero+4000:zero+8000],(x[zero+4000:zero+8000])*0,color = 'black',ls = 'dashed',lw = 1)
    ######################################################
    ax.plot(x[zero-19373:zero - 12931],(-8.1/11)*(x[zero-19373:zero - 12931])-1,color = 'black',ls = 'dashed',lw = 1)
    ax.plot(x[zero+12931:zero - 19373],(8.1/11)*(x[zero-12931:zero - 19373])-1,color = 'black',ls = 'dashed',lw = 1)






def getPlayerPic(playerID,zoom,offset):
    from matplotlib import offsetbox as osb 
    import urllib
    picture = urllib.request.urlopen("https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/" + str(playerID) + ".png")
    playerPic = plt.imread(picture)
    img = osb.OffsetImage(playerPic, zoom)
    img = osb.AnnotationBbox(img, offset,pad=0.0, box_alignment=(1,0), frameon=False)
    return img



def getShotsDFs(playerFullName,teamFullName):
    playerDict = find_players_by_full_name(playerFullName)
    teamDict = find_teams_by_full_name(teamFullName)

    shotsDF =  ShotChartDetail(player_id=playerDict[0]["id"],team_id=teamDict[0]["id"],context_measure_simple="FGA").get_data_frames()
    #Cleaning up shot dfs
    shotsDF[0] = shotsDF[0].drop(columns = [ 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID',
     'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME',"ACTION_TYPE","SHOT_TYPE", 'PERIOD', 'MINUTES_REMAINING', 'SECONDS_REMAINING',
     'GAME_DATE', 'HTM', 'VTM',"EVENT_TYPE"])

    #Alphabetical Order
    shotsDF[0].sort_values(by=["SHOT_ZONE_BASIC","SHOT_ZONE_AREA"],ascending=True,inplace=True)


    return shotsDF #player,league averages
    


def getCareerShotDF(playerFullName):
    from nba_api.stats.endpoints.playercareerstats import PlayerCareerStats
    player = find_players_by_full_name(playerFullName)[0]
    carDF = PlayerCareerStats(player_id = player['id']).get_data_frames()[0]
    teams = []
    for i in range(0,len(carDF),1):
        val = carDF["TEAM_ID"].values[i]
        if val == 0:
            continue
        if len(teams) == 0:
                teams += [val]
        else:
            while val not in teams:
                teams += [val]
        
    teams = [find_team_name_by_id(j)['full_name'] for j in teams]
    allShotDFs = [getShotsDFs(playerFullName,team)[0] for team in teams]
    LOC_X,LOC_Y,SHOT_ZONE_BASIC,SHOT_ZONE_AREA,SHOT_ZONE_RANGE,SHOT_DISTANCE,SHOT_ATTEMPTED_FLAG,SHOT_MADE_FLAG = [],[],[],[],[],[],[],[]
    for df in allShotDFs:
        LOC_X += list(df["LOC_X"].values)
        LOC_Y += list(df["LOC_Y"].values)
        SHOT_ZONE_BASIC += list(df["SHOT_ZONE_BASIC"].values)
        SHOT_ZONE_AREA += list(df["SHOT_ZONE_AREA"].values)
        SHOT_ZONE_RANGE += list(df["SHOT_ZONE_RANGE"].values)
        SHOT_DISTANCE += list(df["SHOT_DISTANCE"].values)
        SHOT_ATTEMPTED_FLAG += list(df["SHOT_ATTEMPTED_FLAG"].values)
        SHOT_MADE_FLAG += list(df["SHOT_MADE_FLAG"].values)
    
    columns = ["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE","SHOT_DISTANCE","LOC_X","LOC_Y","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
    careerDF = pd.DataFrame(list(zip(SHOT_ZONE_BASIC,SHOT_ZONE_AREA,SHOT_ZONE_RANGE,SHOT_DISTANCE,LOC_X,LOC_Y,SHOT_ATTEMPTED_FLAG,SHOT_MADE_FLAG)),columns=columns)
    return careerDF


def genEffPlayerShotDF(playerDF,leagueDF):
    
    playerFGA = np.zeros(len(leagueDF))
    playerFGM = np.zeros(len(leagueDF))
    playerFGPCT = np.zeros(len(leagueDF))
    playerAvgStVerts = np.array([[0,0]]*20)
    playerAvgStDist = np.zeros(len(leagueDF))
    
    for idx,row in playerDF.iterrows():
        for lrow in range(len(leagueDF)):
            if row["SHOT_ZONE_BASIC"] == leagueDF.loc[lrow,"SHOT_ZONE_BASIC"] and row["SHOT_ZONE_AREA"] == leagueDF.loc[lrow,"SHOT_ZONE_AREA"] and row["SHOT_ZONE_RANGE"] == leagueDF.loc[lrow,"SHOT_ZONE_RANGE"]:
                playerFGA[lrow] += 1
                playerFGM[lrow] += row["SHOT_MADE_FLAG"]
                playerAvgStVerts[lrow][0] += row["LOC_X"]
                playerAvgStVerts[lrow][1] += row["LOC_Y"]
                playerAvgStDist[lrow] += np.sqrt( (row["LOC_X"] / 10)**2  + (row["LOC_Y"] / 10)**2      )

    for i in range(0,len(playerFGA)):
        if playerFGA[i] == 0:
            playerFGPCT[i] = 0
            playerAvgStVerts[i] = [0,0]
            playerAvgStDist[i] = 0
        else:
            playerFGPCT[i] = round(playerFGM[i] / playerFGA[i],3)
            playerAvgStVerts[i][0] = playerAvgStVerts[i][0] / playerFGA[i]
            playerAvgStVerts[i][1] = playerAvgStVerts[i][1] / playerFGA[i]
            playerAvgStDist[i] = round(playerAvgStDist[i] / playerFGA[i])
    
    

    columns = ["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE","SHOT_DISTANCE","LOC_X","LOC_Y","FGA","FGM","FG_PCT"]

    
    adjPlayerDF = pd.DataFrame(list(zip(leagueDF["SHOT_ZONE_BASIC"].values,
    leagueDF["SHOT_ZONE_AREA"].values,
    leagueDF["SHOT_ZONE_RANGE"].values,
    playerAvgStDist,
    playerAvgStVerts[:,0],
    playerAvgStVerts[:,1],
    playerFGA,
    playerFGM,
    playerFGPCT)),
    columns = columns)


    return adjPlayerDF



# FROM: https://github.com/savvastj/nbashots
def draw_court(ax=None, color='black', lw=3, outer_lines=False):
    from matplotlib.patches import Circle, Rectangle, Arc
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()
    ax.set(xlim=(-253,253),ylim=(-49.5,450))
    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    # hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    # backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the 
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    # court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
    #                   bottom_free_throw, restricted, corner_three_a,
    #                   corner_three_b, three_arc, center_outer_arc,
    #                   center_inner_arc]
    court_elements = [outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)
    plt.axis('off')
    return ax


def initPlot(plotType):
    from matplotlib.colors import ListedColormap,ColorConverter, LinearSegmentedColormap, Normalize
    fig = plt.figure(figsize = (5.21,5.21))
    ax = draw_court(outer_lines=True)

    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    fig.patch.set_alpha(0.0)

    ax.set_ylim(-47.5,450)
    ax.set_xticklabels(labels = [''],fontsize = 18,alpha = .7, minor = False)
    ax.set_yticklabels(labels = [''],fontsize = 18,alpha = .7, minor = False)

    blue = ColorConverter.to_rgb('#0003FF')
    gray = ColorConverter.to_rgb('#e1e5e5')
    red = ColorConverter.to_rgb('#FF0000')
    purple = ColorConverter.to_rgb('#FC00FF')

    if plotType == 'Player SC':
        norm = Normalize(vmin=0, vmax=1)
        myCmap = LinearSegmentedColormap.from_list(colors = [blue,gray,red],name= 'myCmap')
        myBar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm,cmap=myCmap),orientation = 'horizontal',ticks = [0.0,0.5,1.0])  
        myBar.ax.set_xticklabels(['0%','50%','100%'])
        myBar.ax.tick_params(size = 0)
    
    elif plotType == '2Player SC':
        norm = Normalize(vmin = 0,vmax = 1)
        myCmapPos = LinearSegmentedColormap.from_list(colors = [gray,blue],name = 'myCmapPos')
        myCmapNeg = LinearSegmentedColormap.from_list(colors = [gray,purple],name = 'myCmapNeg')
        myCmap = [myCmapNeg,myCmapPos]
        myCmapT = LinearSegmentedColormap.from_list(colors = [purple,gray,blue],name = 'myCmapT')
        myBar = fig.colorbar(mpl.cm.ScalarMappable(norm = norm,cmap = myCmapT), orientation = 'horizontal',ticks = [0,0.5,1.0])
        myBar.ax.tick_params(size = 0)
    
    elif plotType == "Player ESC":
        norm = Normalize(vmin = 0,vmax = 1)
        myCmapPos = LinearSegmentedColormap.from_list(colors = [gray,red],name = 'myCmapPos')
        myCmapNeg = LinearSegmentedColormap.from_list(colors = [gray,blue],name = 'myCmapNeg')
        myCmap = [myCmapNeg,myCmapPos]
        myCmapT = LinearSegmentedColormap.from_list(colors = [blue,gray,red],name = 'myCmapT')
        myBar = fig.colorbar(mpl.cm.ScalarMappable(norm = norm,cmap = myCmapT), orientation = 'horizontal',ticks = [0,0.5,1.0])
        myBar.set_ticklabels(['Below Avg.','League Avg.','Above Abg.'])
        myBar.ax.tick_params(size = 0)

    return fig,ax,myBar,myCmap

def effplot(playerFullName):
    # from zoneMap import c3,LR3,LR3,paintC816,paintC8,paintl8,paintl8,cLR3,midC816,midC1624,LRSC1624,LRS1624,LRS816,LRSC1624,LRS1624,LRS816,rA,cLR3, outlineZone
    # import polytest as zone

    fig,ax,myBar,myCmap = initPlot('Player ESC')
    # using random player to get league-averages data frame
    ldf = getShotsDFs('lebron james','los angeles lakers')[1]
    carDf = getCareerShotDF(playerFullName=playerFullName)
    eDF = genEffPlayerShotDF(carDf,ldf)
    pName = find_players_by_full_name(playerFullName)[0]["full_name"]
    # color maps are reversed
    myCmapPos, myCmapNeg = myCmap[1],myCmap[0]

    relEff = []
    effList = [None,c3,LR3,LR3,None,paintC816,paintC8,paintl8,paintl8,cLR3,midC816,midC1624,
               LRSC1624,LRS1624,LRS816,LRSC1624,LRS1624,LRS816,rA,cLR3]

    for i in range(len(ldf)):
        if eDF.loc[i]['SHOT_ZONE_AREA'] == 'Back Court(BC)':

            continue
        else:
            if eDF.loc[i]['SHOT_ZONE_BASIC'] == ldf.loc[i]['SHOT_ZONE_BASIC'] and eDF.loc[i]["SHOT_ZONE_AREA"] == ldf.loc[i]['SHOT_ZONE_AREA'] and eDF.loc[i]["SHOT_ZONE_RANGE"] == ldf.loc[i]["SHOT_ZONE_RANGE"]:
                rel = (eDF.loc[i]["FG_PCT"] - ldf.loc[i]["FG_PCT"])
                if rel < 0: 
                    col = myCmapNeg((-rel)**0.25)
                elif rel > 0: 
                    col = myCmapPos(rel**0.25)
                sideKey = eDF.loc[i]["SHOT_ZONE_AREA"]
                side = None
                if sideKey[-1] == ')' and sideKey[-4] == '(':
                    side = sideKey[-3]
                elif sideKey[-1] == ')' and sideKey[-3] == '(':
                    side = sideKey[-2] 
                #color in zone
                effList[i](side=side,ax=ax,color=col)

    draw_court(outer_lines=True)
    outlineZone()
    ax.set_title(pName + "'s Career Shot Efficiency vs. League Efficiency")
    # plt.show()
    name = pName.replace(" ","")
    plt.savefig('C:/Users/pedja/Documents/Programming/StatsNBA/Application/flask-server/lib/images/playerSC/'+ name + '.jpeg')
    plt.close()
    return True




def plotPlayerSC(playerFullName):
    from matplotlib.patches import RegularPolygon
    # intialize plot for player shot chart
    fig,ax,myBar,myCmap = initPlot('Player SC')
    # getting player shot dataframe
    initPlayerDF = getCareerShotDF(playerFullName)
    #Getting official player and team name
    playerDict = find_players_by_full_name(playerFullName)[0]

    # Labelling color bar
    myBar.set_label(playerDict["full_name"] + "'s " + "Shooting Percentage (%)" )
    # Labelling Plot
    ax.set_title(playerDict["full_name"] + " Career Shot-Chart!")

    # Getting player efficiency data
    fga = []
    fgm = []
    for idx,row in initPlayerDF.iterrows():
        fga += [[row["LOC_X"],row["LOC_Y"]]]
        if row["SHOT_MADE_FLAG"] == 1:
            fgm += [[row["LOC_X"],row["LOC_Y"]]]
    fga = np.array(fga)
    fgm = np.array(fgm)

    # initiating hexbins
    fgaHexD = plt.hexbin(fga[:,0],fga[:,1],gridsize = (30),extent = [-249,249,-47.5,450],mincnt=0,alpha=0.0)
    fgmHexD = plt.hexbin(fgm[:,0],fgm[:,1],gridsize = (30),extent = [-249,249,-47.5,450],mincnt = 0,alpha=0.0)
    
    fgaV = fgaHexD.get_offsets()
    fgaF = fgaHexD.get_array()

    fgmF = fgmHexD.get_array()

    eff = np.zeros(len(fgmF))
    for idx in range(0,len(eff)):
        if fgaF[idx] < 1:
            continue
        if fgaF[idx] == 0:
            eff[idx] = 0
        else:
            eff[idx] = round((fgmF[idx]/fgaF[idx]),4)

    for idx,shotLoc in enumerate(fgaV):
        if shotLoc[1] > 310:
            continue
        else:
            scale =  np.pi * (fgaF[idx])**0.25
            color = myCmap(eff[idx])
            hex = RegularPolygon((fgaV[idx][0],fgaV[idx][1]),numVertices=6,radius=scale,color=color,alpha = 0.8)
            ax.add_patch(hex)


    name = playerDict["full_name"].replace(" ","")
    plt.savefig('C:/Users/pedja/Documents/Programming/StatsNBA/Application/flask-server/lib/images/playerSC/'+ name + '.jpeg')
    plt.close()
    # plt.show()




def playerShotComp(player1,player2):
    from matplotlib.patches import RegularPolygon
    fig,ax,myBar,myCmap = initPlot('2Player SC')
    myCmapNeg , myCmapPos = myCmap[0] , myCmap[1]

    p1DF = getCareerShotDF(player1)
    p2DF = getCareerShotDF(player2)

    p1Dict = find_players_by_full_name(player1)[0]
    p2Dict = find_players_by_full_name(player2)[0]

    myBar.set_label(p2Dict['full_name']+ "'s" + ' vs. ' + p1Dict['full_name'] + "'s Shooting Percentage" )
    ax.set_title("Who's more the more efficient shooter? ")

    fga1,fgm1 = np.zeros(shape = (len(p1DF),2)),np.zeros(shape = (len(p1DF),2))
    fga2,fgm2 = np.zeros(shape = (len(p2DF),2)),np.zeros(shape = (len(p2DF),2))

    for idx,row in p1DF.iterrows():
        fga1[idx] = [row["LOC_X"],row["LOC_Y"]]
        if row["SHOT_MADE_FLAG"] == 1:
            fgm1[idx] = [row["LOC_X"],row["LOC_Y"]]

    for idx,row in p2DF.iterrows():
        fga2[idx] = [row["LOC_X"],row["LOC_Y"]]
        if row["SHOT_MADE_FLAG"] == 1:
            fgm2[idx] = [row["LOC_X"],row["LOC_Y"]]

    fgaH1 = plt.hexbin(fga1[:,0],fga1[:,1],gridsize = (30),extent = [-250,250,-47.5,450],mincnt=0,alpha=0.0)
    fgmH1 = plt.hexbin(fgm1[:,0],fgm1[:,1],gridsize = (30),extent = [-250,250,-47.5,450],mincnt = 0,alpha=0.0)
    fgaV1 = fgaH1.get_offsets()
    fgaF1 = fgaH1.get_array()
    fgmF1 = fgmH1.get_array()

    fgaH2 = plt.hexbin(fga2[:,0],fga2[:,1],gridsize = (30),extent = [-250,250,-47.5,450],mincnt=0,alpha=0.0)
    fgmH2 = plt.hexbin(fgm2[:,0],fgm2[:,1],gridsize = (30),extent = [-250,250,-47.5,450],mincnt = 0,alpha=0.0)
    fgaV2 = fgaH2.get_offsets()
    fgaF2 = fgaH2.get_array()
    fgmF2 = fgmH2.get_array()



    relEff = np.zeros(len(fgaF1)) #1/2 have same lengths
    
    for i in range(0,len(relEff),1):
        diff = 0
        if fgaF1[i] == 0 and fgaF2[i] == 0:
            diff = -2
        elif fgaF1[i] == 0:
            diff = -(fgmF2[i]/fgaF2[i])
        elif fgaF2[i] == 0:
            diff = (fgmF1[i]/fgaF1[i])
        else:
            diff = (fgmF1[i]/fgaF1[i]) - (fgmF2[i]/fgaF2[i])

        relEff[i] = round(diff,4)
    
    # #             #fix negative value for color mapping 
    for idx,shotLoc in enumerate(fgaV1):
        scale =  2*np.pi
        if relEff[idx] == -2:
            continue
        if relEff[idx] < 0:
            color = myCmapNeg(-relEff[idx])
        # if fgaV1[idx][1] > 350:
        #     continue
        else:
            color = myCmapPos(relEff[idx])
        hex = RegularPolygon((fgaV1[idx][0],fgaV1[idx][1]),numVertices=6,radius=scale,color=color,alpha = 0.8)
        ax.add_patch(hex)

    myBar.ax.set_xticklabels([p2Dict['full_name'] ,'Equal',p1Dict['full_name']])

    name = (p1Dict['full_name'] + p2Dict['full_name']).replace(" ","")
    # print(name)
    plt.savefig('C:/Users/pedja/Documents/Programming/StatsNBA/Application/flask-server/lib/images/twoPlayerSCs/'+name + '.jpeg',)
    # plt.show()











    
    



    


    
    
