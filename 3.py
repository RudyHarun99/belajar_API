# python GET request => API
# urllib
# py -m pip install requests

import requests

# url='https://jsonplaceholder.typicode.com/users/1' # mengambil data users id 1
# data=requests.get(url)
# print(data) # menampilkan status
# print(data.json()) # menampilkan semua data id 1
# print(type(data.json())) # menampilkan type data id 1
# print(data.json()['name']) # menampilkan data keys 'name' id 1
# print(data.json()['address']['street']) # menampilkan data keys 'address','street' id 1

url='https://jsonplaceholder.typicode.com/users' # mengambil semua data 
data=requests.get(url)
# menampilkan semua data keys 'name','address','street'
for i in data.json():
    print(i['name'],'di Jl.',i['address']['street'])