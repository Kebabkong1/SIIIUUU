from asyncio import constants
import requests
from common.constants import league_id
from env.secrets import api_token
headers = {"apikey": api_token}
response = requests.get('http://api.football-data.org/v4/competitions/', headers=headers)

print(response.text)
print(league_id)