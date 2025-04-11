import requests

url = "https://kathrypythonanywhere.pythonanywhere.com/api/v1/predict"
data = {
    "TV": 100,
    "radio": 20,
    "newspaper": 10
}

response = requests.post(url, json=data)
print("Statuscode:", response.status_code)
print("Antwort (roh):", response.text)

