import pandas as pd
from sqlalchemy import create_engine

csv_file = "joueurs_5_championnats.csv"

# Lire le CSV sans utiliser la première ligne comme nom de colonnes
df = pd.read_csv(csv_file, header=None, encoding="utf-8-sig")

# Définir les noms de colonnes corrects
df.columns = ["team", "player_id", "full_name", "position", "shirt_number", "birth_date", "nationality"]

# Connexion à PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/football")

print(f"Nombre de joueurs à insérer : {len(df)}")

# Insérer les données
df.to_sql("players", engine, if_exists="replace", index=False)

print("✅ Importation réussie")
