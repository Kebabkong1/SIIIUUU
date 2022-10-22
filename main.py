from asyncio import constants
import requests
import common/constants
headers = {"apikey": "YOUR-APIKEY"}
x = requests.get('http://api.football-data.org/v4/competitions/', headers=headers)

print(x.text)
print(constants-)