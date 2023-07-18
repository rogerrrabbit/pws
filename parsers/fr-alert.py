import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

# Définir l'URL à parser
url = "https://fr-alert.gouv.fr/les-alertes"

# Faire une requête HTTP pour récupérer le contenu de la page
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
response = requests.get(url, verify=False)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Créer un objet BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Parcourir les dates
    dates = soup.find_all(class_="date")
    for date in dates:
        date_titre = date.find(class_="date-title").text.strip()

        # Parcourir les alertes et extraire les informations pertinentes
        alertes = date.find_all(class_="alert-item")
        for alerte in alertes:
            id = alerte['id']

            # Trouver le titre de l'alerte
            titre = alerte.find(class_="alert-title").text.strip()

            # Trouver l'heure de l'alerte
            heure = alerte.find(class_="alert-hour").text.strip()
            date_heure = date_titre + ", " + heure

            # Trouver le lieu de l'alerte
            lieu = alerte.find(class_="alert-place").text.strip()

            # Afficher les informations de l'alerte
            print(f"{id}")
            print(f"Titre: {titre}")
            print(f"Date et heure: {date_heure}")
            print(f"Lieu: {lieu}")
            print()
