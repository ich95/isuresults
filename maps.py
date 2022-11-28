import requests
import json
data = []
base = "insert into karte (id,eventname,start,end,season,latitude,longitude,trackname) Values \n"
additional = "({},'{}','{}','{}',{},{},{},'{}'),\n"


for i in range(1,6):
    data += json.loads(requests.get("https://api.isuresults.eu/events/?page="+str(i)).text)['results']

newlist = sorted(data, key=lambda d: d['id']) 
for i in newlist:
    #print(str(i['id'])+": ("+str(i['season'])+") "+i['name']+";"+i['track']['name'])
    base += additional.format(str(i['id']),i['name'],i['start'],i['end'],str(i['season']),i['track']['latitude'],i['track']['longitude'],i['track']['name'])


print(base)