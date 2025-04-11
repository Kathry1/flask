import requests

# API-URL (läuft lokal auf Port 5000)
url = "http://127.0.0.1:5000/api/v1/predict"

# Beispiel-Eingabedaten
data = {
    "TV": 100,
    "radio": 20,
    "newspaper": 10
}

# Sende POST-Anfrage
response = requests.post(url, json=data)

# Zeige Antwort
print("Response:", response.json())
