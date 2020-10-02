import numpy as np
import os,sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from models import gameLog
import nnLib
import torch 

atlTable = gameLog.query.filter(gameLog.team == 'Atlanta Hawks').all()


arrays = []
mat = np.array((atlTable[0].fgPct,atlTable[0].pct3,atlTable[0].ftpct,atlTable[0].oReb,atlTable[0].dReb,atlTable[0].ast,atlTable[0].stl, atlTable[0].blk,atlTable[0].turnO,atlTable[0].pts,atlTable[0].isHome))


train = []
cnt = atlTable[0].didWin
for game in atlTable:
    if cnt == 0:
        cnt += 1
        continue
    else:
        vec = np.array((game.fgPct,game.pct3,game.ftpct,game.oReb,game.dReb,game.ast,game.stl, game.blk,game.turnO,game.pts,game.isHome))
        mat = np.vstack((mat,vec))
        train += [game.didWin]

mat = mat[1:,:] # 20 games by 11 features

matTensor = torch.from_numpy(mat).float()
trainTensor = torch.from_numpy(
    np.array([train]).T
).float()

net = nnLib.NeuralNetwork()
nnLib.train(matTensor,trainTensor,model=net,learningRate=0.0095,epochs=300)










