import requests
import time
import json
from common.constants import league_id
from env import secrets

print(secrets.api_token)
def saving_to_dict(league):
    headers = {"X-Auth-Token": '34e1475dd9f740f797baf591f0ab5e30'}
    api_url = ("http://api.football-data.org/v4/competitions/" + league + "/teams")
    response = requests.get(api_url, headers=headers)
    response_json = response.json()
    teams_json = response_json["teams"]
    teams_dict = {}
    for el in teams_json:
        teams_dict[el["shortName"]] = el["id"]
    return teams_dict

leagues = {}

i = 0
print(league_id)
print(league_id.values())
for val in league_id.values():
    print(val)
    league_key = val
    league_teams = saving_to_dict(val)
    val = []
    val.append(league_teams)
    leagues[league_key] = val
    if(i == 5): 
        time.sleep(60)
    i += 1

final_dict = {}
final_dict["leagues"] = leagues

with open("leagues.json", "w") as outfile:
    json.dump(final_dict, outfile)

