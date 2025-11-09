import pandas as pd
from sqlalchemy import create_engine

# Chemin vers ton fichier CSV
csv_file = "C:/Users/yannb/OneDrive/Documents/5_Codage/Projet/data/matchs_ligues.csv"

# Connexion à PostgreSQL (remplace user, password, db_name si besoin)
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/football")

# Charger le CSV en DataFrame en limitant à 131 colonnes
df = pd.read_csv(
    csv_file,
    encoding="utf-8-sig",
    usecols=range(131),   # ⬅️ ne garde que les 131 premières colonnes
    skiprows=1            # ⬅️ saute la première ligne si elle est du texte/titre
)

# Supprimer les espaces ou caractères parasites dans les noms de colonnes
df.columns = df.columns.str.strip()

# Créer la table 'matches' et insérer toutes les données
df.to_sql("matches", engine, if_exists="replace", index=False)

print("✅ Importation réussie : le fichier entier est dans la table 'matches'")
