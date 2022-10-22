from asyncio import constants
import requests
from common.constants import leagueID
from env.secrets import api_token
headers = {"apikey": api_token}
x = requests.get('http://api.football-data.org/v4/competitions/', headers=headers)

print(x.text)
print(leagueID)