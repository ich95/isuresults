import requests
import json

ranking = 5
nationality = "GER"


def getEvents(season):
    # prints list of Events in the given Season (str)
    # returns scheduleUrl of chosen event (str)
    default = 1
    isLive = json.loads(requests.get(
        "https://api.isuresults.eu/events/?orderBy=start&isPublished=1&isLive=1").text)
    liveEvents = []
    num = 1
    output = ""
    for i in isLive['results']:
        liveEvents.append(i['name'])
    result = json.loads(requests.get(
        "https://api.isuresults.eu/events/?season={s}".format(s=season)).text)

    outputString = "{num}:\t{name} ({country})\n"
    for i in result['results']:
        if i['name'] in liveEvents:
            default =num
            output += ">" + \
                outputString.format(
                    num=num, name=i['name'], country=i['nationalFederation'])
        output += " " + \
            outputString.format(
                num=num, name=i['name'], country=i['nationalFederation'])
        num += 1

    id = int(input(output) or default)-1
    return result['results'][id]['scheduleUrl']


def getDistances(eventurl):
    print(eventurl)
    # lists distances of given Event
    # returns url for results of chosen distance
    default = 1
    output = ""
    outputString = "{id}:\t{dist}\n"
    distances = json.loads(requests.get(eventurl).text)
    for i in distances:
        if i['links'][0]['isLive']:
            default = i['links'][0]['identifier']
            output += ">" + \
                outputString.format(
                    id=str(i['links'][0]['identifier']), dist=i['title'])
        output += " " + \
            outputString.format(
                id=str(i['links'][0]['identifier']), dist=i['title'])
    id = int(input(output)or default)
    return distances[id-1]['links'][0]['url']+"results/?inSeconds=0"


def getResults(distanceUrl, ranking, nationality=""):
    # lists results of given distance
    # returns the output for later filtering
    results = json.loads(requests.get(distanceUrl).text)
    for i in results:
        if i['type'] == "ind":
            if i['rank'] is not None and i['competitor']['skater']['firstName'] is not None and i['competitor']['skater']['lastName'] is not None:
                if i['rank'] <= ranking or i['competitor']['skater']['country'] == nationality:
                    print("{rank}: {fname} {lname} ({nat}): {time}".format(rank=str(
                        i['rank']), fname=i['competitor']['skater']['firstName'], lname=i['competitor']['skater']['lastName'], nat=i['competitor']['skater']['country'], time=i['time']))
        else:
            if i['rank'] is not None and i['team']['name'] is not None:
                if i['rank'] <= ranking or i['team']['country'] == nationality:
                    print("{rank}: {tname}({nat}): {time}".format(rank=str(
                        i['rank']), tname=i['team']['name'], nat=i['team']['country'], time=i['time']))






url = getEvents(2022)
dists = getDistances(url)

results = getResults(dists, ranking, nationality)