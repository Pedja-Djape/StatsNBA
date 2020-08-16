# from nba_api.stats.static.teams import *

# teams = [x["abbreviation"] for x in get_teams()]
# print(teams)

x = ['ATL', 'BOS', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL',
                  'MIA', 'MIL', 'MIN', 'BKN', 'NYK', 'ORL', 'IND', 'PHI', 'PHX', 'POR', 'SAC',
                   'SAS', 'OKC','TOR', 'UTA', 'MEM', 'WAS', 'DET', 'CHA']
import numpy as np
# count = 0;
# for i in x:
#     print('{team: %s id: %s}' %(i,str(count)))
#     count += 1
y = ['{team: %s, id: %s}' %(val,str(i)) for i,val in enumerate(x)]
print(y)

"""
[{name: ATL, id: 0}, 
{name: BOS, id: 1},
 {name: CLE, id: 2},
  {name: NOP, id: 3},
   {name: CHI, id: 4}, {name: DAL, 
id: 5}, {name: DEN, id: 6}, {name: GSW, id: 7}, {name: HOU, id: 8}, {name: LAC, id: 9}, {name: LAL, id: 10}, {name: MIA, id: 11}, {name: MIL, id: 12}, {name: MIN, id: 13}, {name: BKN, id: 14}, {name: NYK, id: 15}, {name: ORL, 
id: 16}, {name: IND, id: 17}, {name: PHI, id: 18}, {name: PHX, id: 19}, {name: POR, id: 20}, {name: SAC, id: 21}, {name: SAS, id: 22}, {name: OKC, id: 23}, {name: TOR, id: 24}, {name: UTA, id: 25}, {name: MEM, id: 26}, {name: 
WAS, id: 27}, {name: DET, id: 28}, {name: CHA, id: 29}]



"""