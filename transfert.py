import requests
from bs4 import BeautifulSoup

def get_player_profile_tm(player_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; examplebot/1.0)"
    }
    resp = requests.get(player_url, headers=headers)
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.text, "html.parser")

    # Exemple : nom, âge, nationalité
    name = soup.find("h1", class_="data-header__headline").get_text(strip=True)
    # dépend de la structure réelle de la page
    # ...
    return {"name": name}

# Exemple d'utilisation
url = "https://www.transfermarkt.com/lionel-messi/profil/spieler/28003"
profile = get_player_profile_tm(url)
print(profile)
