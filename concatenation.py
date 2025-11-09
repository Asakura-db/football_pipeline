import pandas as pd
import glob

# Chemin vers ton dossier CSV
chemin_dossier = r"C:/Users/yannb/OneDrive/Documents/5_Codage/Projet/data/matches/*.csv"

# Récupère tous les fichiers CSV
fichiers = glob.glob(chemin_dossier)

dfs = []

for fichier in fichiers:
    # Nom du fichier sans chemin ni extension comme "competition"
    competition = fichier.split("\\")[-1].replace(".csv", "")
    
    # Lecture du CSV en sautant la première ligne
    df = pd.read_csv(fichier, skiprows=1, encoding="utf-8-sig")
        
    dfs.append(df)

# Concatène tous les CSV
df_final = pd.concat(dfs, ignore_index=True)

# Vérifie les premières lignes
print(df_final.head())

# Sauvegarde tout en un seul CSV combiné (optionnel)
df_final.to_csv(r"C:/Users/yannb/OneDrive/Documents/5_Codage/Projet/data/matches_combined.csv", index=False, encoding="utf-8")
