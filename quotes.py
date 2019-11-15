import requests

url='http://quotes.rest/qod'
data=requests.get(url)
data=data.json()
print(data)
print(data['contents']['quotes']['0']['quote'])
print(data['contents']['quotes']['0']['author'])