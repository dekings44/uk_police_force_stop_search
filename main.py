import requests

response = requests.get('https://randomfox.ca/floof')

print(response.json())

info = response.json()

print(info['image'])
print(info['link'])