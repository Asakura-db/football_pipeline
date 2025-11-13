import requests

API_KEY = "79df369c68fa417296dfdb3a5986ef6d"
headers = {"X-Auth-Token": API_KEY}

team_id = 66  # Manchester United
url = f"https://api.football-data.org/v4/teams/{team_id}"
response = requests.get(url, headers=headers)

team_data = response.json()
print("Équipe :", team_data["name"])
print("Joueurs :")

for player in team_data["squad"]:
    print(player["name"], "-", player["position"], "-", player["nationality"])

