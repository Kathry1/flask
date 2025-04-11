import requests

url = "https://kathrypythonanywhere.pythonanywhere.com/api/v1/retrain"

# CSV-Datei mit neuen Trainingsdaten (Pfad anpassen!)
file_path = 'data/Advertising_new.csv'

files = {'file': open(file_path, 'rb')}

response = requests.post(url, files=files)

print("Status:", response.status_code)
print("Antwort:", response.text)
