import numpy as np
import matplotlib.pyplot as plt
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