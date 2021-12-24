import requests

response = requests.get('https://data.police.uk/api/forces')

infos = response.json()

for info in infos:
    id = info['id']
    name = info['name']
    print(id, name)
    