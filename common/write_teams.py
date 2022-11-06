import requests
import time
import json
from common.constants import league_id
from env import secrets

def saving_to_dict(league):
    headers = {"X-Auth-Token": secrets.api_token}
    api_url = ("http://api.football-data.org/v4/competitions/" + league + "/teams")
    response = requests.get(api_url, headers=headers)
    response_json = response.json()
    print(response.status_code)
    teams_json = response_json["teams"]
    teams_dict = {}
    for team in teams_json:
        teams_dict[team["name"]] = {"id":team["id"]}
    return teams_dict

leagues = {}

for short_league_name in league_id.values():
    league_teams = saving_to_dict(short_league_name)
    leagues[short_league_name] = league_teams
    if(len(leagues) == 5): 
        time.sleep(61)

final_dict = {}
final_dict["leagues"] = leagues


with open("leagues.json", "w",  encoding='utf8') as outfile:
    json.dump(final_dict, outfile, ensure_ascii=False)

