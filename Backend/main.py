import requests

def fetch_data(endpoint, filter={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filter)

    return response.json() if response.status_code == 200 else None

character = fetch_data("character", {"name": "Rick"})
if character:
    print(character)
else:
    print("Failed to fetch data.")