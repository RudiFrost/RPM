import requests

res = requests.get("https://api.opendota.com/api/heroes")

print(res.json())

f = open('dota.json', 'w')
f.write(str(res.json()))







