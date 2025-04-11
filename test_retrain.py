import requests

# URL des Retrain-Endpunkts
url = "http://127.0.0.1:5000/api/v1/retrain"

# Lade die CSV-Datei hoch
files = {'file': open('data/Advertising_new.csv', 'rb')}





# Sende POST-Anfrage
response = requests.post(url, files=files)

# Zeige die Antwort
print("Response:", response.json())
