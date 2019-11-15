import requests
klub=input('Ketik klub : ')
url=f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data=requests.get(url)
players=data.json()['player'] # krn datanya ada di dalam list player, bikin variabel baru

for player in players:
    print(player['strPlayer'])