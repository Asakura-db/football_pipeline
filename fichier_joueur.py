import requests
import pandas as pd
import time

API_KEY = "79df369c68fa417296dfdb3a5986ef6d"
BASE_URL = "https://api.football-data.org/v4"
headers = {"X-Auth-Token": API_KEY}

# Championnats
competitions = ["PL", "FL1", "BL1", "SA", "PD"]  # Premier League, Ligue 1, Bundesliga, Serie A, La Liga

players_data = []

for comp in competitions:
    url = f"{BASE_URL}/competitions/{comp}/teams?season=2024"
    response = requests.get(url, headers=headers)
    data = response.json()

    for team in data.get("teams", []):
        team_id = team["id"]
        team_name = team["name"]

        # Pause obligatoire (limite API gratuite : 10 appels/min)
        time.sleep(6)

        url_team = f"{BASE_URL}/teams/{team_id}"
        response_team = requests.get(url_team, headers=headers)
        team_data = response_team.json()

        squad = team_data.get("squad", [])
        for player in squad:
            players_data.append({
                "team": team_name,
                "id": player.get("id"),
                "name": player.get("name"),
                "position": player.get("position"),
                "shirtNumber": player.get("shirtNumber"),
                "dateOfBirth": player.get("dateOfBirth"),
                "nationality": player.get("nationality")
            })

# Mettre en DataFrame
df_players = pd.DataFrame(players_data)

# Ajouter la ligne explicative en haut
description = {
    "team": "Nom de l'équipe",
    "id": "→ identifiant unique du joueur",
    "name": "→ nom complet",
    "position": "→ poste (Goalkeeper, Defender, Midfielder, Attacker)",
    "shirtNumber": "→ numéro de maillot (si dispo)",
    "dateOfBirth": "→ date de naissance",
    "nationality": "→ nationalité"
}

# Fusionner la ligne descriptive + données joueurs
df_final = pd.concat([pd.DataFrame([description]), df_players], ignore_index=True)

# Sauvegarde CSV
df_final.to_csv("joueurs_5_championnats.csv", index=False, encoding="utf-8-sig")

print("✅ Tous les joueurs ont été exportés dans joueurs_5_championnats.csv")
