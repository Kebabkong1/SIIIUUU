from asyncio import constants
import requests
from common.constants import leagueID
headers = {"apikey": "YOUR-APIKEY"}
x = requests.get('http://api.football-data.org/v4/competitions/', headers=headers)

print(x.text)
print(leagueID)