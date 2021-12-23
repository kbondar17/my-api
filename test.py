import requests

BASE = 'http://127.0.0.1:5000/'

# r = requests.get(BASE + 'getnews')
# print('результат get-запроса:',r.json())

print(requests.get('https://weedly-backend.herokuapp.com/getnews').json())
