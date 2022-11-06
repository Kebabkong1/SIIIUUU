from dataclasses import dataclass
import requests
import json
import time
from common.constants import league_id
from env.secrets import api_token

path = 'leagues.json'
headers = {"X-Auth-Token": api_token}
league_file = open(path, "r",  encoding='utf8')
league_data = json.load(league_file)

def played_matches_response(league_short_name):
    response = requests.get(f'http://api.football-data.org/v4/competitions/{league_short_name}/matches?status=FINISHED', headers=headers)
    print(response.status_code)
    return response

def add_result_array(matches, league_short_name):
    for index, match_info in enumerate(matches):
        home_team = matches[index]["homeTeam"]["name"]
        away_team = matches[index]["awayTeam"]["name"]
        result = match_info["score"]["winner"]
        match result:
            case 'HOME_TEAM':
                league_data["leagues"][league_short_name][home_team].setdefault('resultArray', []).append(3)
                league_data["leagues"][league_short_name][away_team].setdefault('resultArray', []).append(0)
            case 'AWAY_TEAM':
                league_data["leagues"][league_short_name][home_team].setdefault('resultArray', []).append(0)
                league_data["leagues"][league_short_name][away_team].setdefault('resultArray', []).append(3)        
            case 'DRAW':
                league_data["leagues"][league_short_name][home_team].setdefault('resultArray', []).append(1)
                league_data["leagues"][league_short_name][away_team].setdefault('resultArray', []).append(1)        
            case _: 
                print('undefined value in score winner :'  + str(result))

for index, league_short_name in enumerate(league_id.values()):
    print(league_short_name)
    res = played_matches_response(league_short_name)
    res_json = res.json()
    matches = res_json['matches']
    add_result_array(matches, league_short_name)
    if (index==5):
        time.sleep(61)

with open("leagues_result.json", "w",  encoding='utf8') as outfile:
    json.dump(league_data, outfile, ensure_ascii=False)
