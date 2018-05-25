#test_get_eventlist.py
import requests
import json
# from importlib import reload
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )


url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url, params={'eid':'1'})
result = r.json()
# jsondata = json.dumps(result,ensure_ascii = False).encode('utf-8')
jsondata = json.dumps(result).encode('utf-8')
print(jsondata)



# .decode('unicode-escape')
# jsondata= json.dumps( dics, ensure_ascii = False, indent = 4 )