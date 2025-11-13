import requests

API_KEY = "79df369c68fa417296dfdb3a5986ef6d"
headers = {"X-Auth-Token": API_KEY}

url = "https://api.football-data.org/v4/competitions/PL/teams" 
response = requests.get(url, headers=headers)

data = response.json()
for team in data["teams"]:
    print(team["name"], "-", team["id"])

