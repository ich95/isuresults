from unittest import result
import requests
import json
URL="https://api.isuresults.eu/events/2022_AUT_0002/competitions/1/results/?inSeconds=0"
URL_DITANCES = "https://api.isuresults.eu/events/2022_AUT_0002/competitions"
valid = []
distances = json.loads(requests.get(URL_DITANCES).text)
for i in distances:
    print("{id}: {dist} (Ref: {ref}, Starter: {sta}".format(id=str(i['scheduleNumber']),dist=i['title'],ref=i['referee']['firstName']+" "+i['referee']['lastName'], sta=i['starter']['firstName']+" "+i['starter']['lastName']))
    valid.append(str(i['scheduleNumber']))
id = input("Results for Distance: ")
if id not in valid:
    print("not a valid Distance")
    exit()
results = json.loads(requests.get("https://api.isuresults.eu/events/2022_AUT_0002/competitions/{id}/results/?inSeconds=0".format(id=id)).text)
print("#########################")
# print(results)
for i in results:
    if i['rank'] is not None and i['competitor']['skater']['firstName'] is not None and i['competitor']['skater']['lastName'] is not None:
        # print(str(i['rank'])+": "+i['competitor']['skater']['firstName']+" "+i['competitor']['skater']['lastName']+" "+ i['time'])
        if i['rank'] <=10 or i['competitor']['skater']['country'] == "GER":
            print("{rank}: {fname} {lname} ({nat}): {time}".format(rank=str(i['rank']),fname=i['competitor']['skater']['firstName'],lname=i['competitor']['skater']['lastName'],nat=i['competitor']['skater']['country'],time=i['time']))