from dataclasses import dataclass
import requests
import json
from common.constants import league_id
from env.secrets import api_token

path = "SIIIUUU\common\league-data.json"
headers = {"X-Auth-Token": api_token}
#response = requests.get('https://api.football-data.org/v4/competitions/PL/matches?status=FINISHED', headers=headers)

#response_json = response.json()

#print(response_json["matches"][0]["score"])
#print(response_json["matches"][0]["homeTeam"]["name"])
#print(response_json["matches"][0]["awayTeam"]["name"])
#print(response_json)

f = open(path, "r")
data = json.load(f)
league_names= ["PL"]


for leagues in data["leagues"]:
    for league in leagues:
        print(league)
        for team in leagues[league]:
            print(team)

f.close()


print(data["leagues"][0]["PL"][0])
data["leagues"][0]["PL"][0]["Arsenal"]["kim"] = 1

fw = open(path, 'w')

fw.write(json.dumps(data))

fw.close