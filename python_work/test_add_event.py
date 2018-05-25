import requests

url = "http://127.0.0.1:8000/api/add_event/"
payload = {'eid':3,'name':'小米6','limit':2000,
'address':"北京水立方",'start_time':'2017-05-10 12:00:00'}

r = requests.post(url,data = payload)

result = r.json()

print(result)



