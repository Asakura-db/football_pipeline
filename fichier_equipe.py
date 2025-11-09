import requests
import pandas as pd
import time
from sqlalchemy import create_engine

# ⚡ PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/football")

# API Football
API_KEY = "79df369c68fa417296dfdb3a5986ef6d"
BASE_URL = "https://api.football-data.org/v4"
headers = {"X-Auth-Token": API_KEY}

# Championnats
competitions = ["PL", "FL1", "BL1", "SA", "PD"]  # Premier League, Ligue 1, Bundesliga, Serie A, La Liga

teams_data = []

for comp in competitions:
    url = f"{BASE_URL}/competitions/{comp}/teams?season=2024"
    response = requests.get(url, headers=headers)
    data = response.json()

    for team in data.get("teams", []):
        teams_data.append({
            "team_id": team["id"],
            "team_name": team["name"],
            "short_name": team.get("shortName"),
            "tla": team.get("tla"),
            "venue": team.get("venue")
        })

    # Pause obligatoire pour l'API gratuite (10 appels/min)
    time.sleep(6)

# Mettre en DataFrame
df_teams = pd.DataFrame(teams_data)

# Supprimer espaces ou caractères parasites dans les noms de colonnes
df_teams.columns = df_teams.columns.str.strip()

# Insérer dans PostgreSQL dans la table 'teams' (replace)
df_teams.to_sql("teams", engine, if_exists="replace", index=False)

print(f"✅ Toutes les équipes ont été importées dans la table 'teams' ({len(df_teams)} lignes)")
