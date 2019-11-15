import requests
x='&appid=afb195ebd8e248c43f8990b85e3a8841'
y=input('Ketik kota : ')
url=f'http://api.openweathermap.org/data/2.5/weather?q={y}{x}'
data=requests.get(url)
data=data.json()
# print(data['sys']['sunrise'])
# print(data['sys']['sunset'])
sunrise=data['sys']['sunrise']
sunset=data['sys']['sunset']

from datetime import datetime
waktu=datetime.utcfromtimestamp(int(sunrise))
print(waktu)