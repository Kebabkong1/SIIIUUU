import json
from common.constants import league_id

path = 'leagues_result.json'

league_file = open(path, "r",  encoding='utf8')
league_data = json.load(league_file)

inform_teams=[]
for index, league_short_name in enumerate(league_id.values()):
   
    for team in league_data["leagues"][league_short_name]: 
        try:
            arr =  league_data["leagues"][league_short_name][team]["resultArray"][-5:]
            if (sum(arr)>9):
                inform_teams.append(team)
        except: 
            print("empty array for " + team)

print(inform_teams)
