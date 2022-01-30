# ISU Speed Skating Results
get the results of ISU Speed Skating Events
Please view the [API Docs](https://api.isuresults.eu/docs/) of isuresults too: 
# API Endpoints Used
## Event overview
https://api.isuresults.eu/events/?season=2022
- season=2022 -> the current season <br>
Example output:
```json
{"count":14,
"next":null,
"previous":null,
"results":[
    {"id":240,
    "name":"ISU World Cup Speed Skating Final",
    "isuShortName":"wcssned2022",
    "nationalFederation":"NED",
    "isuId":"2022_NED_0002",
    "start":"2022-03-12",
    "end":"2022-03-13",
    "season":2022,
    "tags":["world-cup","senior","final"],
    "track":{
        "id":24,
        "name":"Thialf",
        "city":"Heerenveen",
        "country":"NED",
        "timeZone":"Europe/Amsterdam",
        "timeZoneOffset":"+0100",
        "isOutdoor":false,
        "isActive":true,
        "altitude":3,
        "latitude":"52.938399",
        "longitude":"5.942384"
        },
        "logo":"https://media.isuresults.eu/event/logo/Z21KKmlPTPGeVJQythSUSQ.jpg",
        "precision":3,
        "isPublished":true,
        "isCancelled":false,
        "trackUrl":"https://api.isuresults.eu/tracks/24/",
        "competitorsUrl":"https://api.isuresults.eu/events/2022_NED_0002/competitors/",
        "teamsUrl":"https://api.isuresults.eu/events/2022_NED_0002/teams/",
        "competitionsUrl":"https://api.isuresults.eu/events/2022_NED_0002/competitions/",
        "championshipsUrl":"https://api.isuresults.eu/events/2022_NED_0002/championships/",
        "scheduleUrl":"https://api.isuresults.eu/events/2022_NED_0002/schedule/"},
        {...}
]
```
## Distances of event
https://api.isuresults.eu/events/2022_AUT_0002/competitions
- 2022_AUT_0002 -> the specific event <br>
Example Output:
```json
[{
    "scheduleNumber":1,
    "type":"ID",
    "title":"500m Women",
    "subTitle":"",
    "start":"2022-01-28T09:00:00Z",
    "distance":{
        "identifier":"ID_500",
        "name":"500 Meter",
        "distance":500,
        "lapCount":2,
        "type":"ID",
        "resourceUrl":"https://api.isuresults.eu/distances/ID_500/"},
        "number":null,
        "category":"F",
        "division":"",
        "referee":{
            "id":28,
            "firstName":"Ekaterina",
            "lastName":"Pilshchikova",
            "country":"RUS",
            "gender":"F",
            "dateOfBirth":"1970-01-01",
            "dateOfDeath":null,
            "isActive":true,
            "photo":null,
            "created":"2017-10-28T13:25:07.289886Z",
            "modified":"2017-10-28T13:25:07.296170Z"
            },"starter":{
                "id":110,
                "firstName":"Kari",
                "lastName":"Hautamäki",
                "country":"FIN",
                "gender":"F",
                "dateOfBirth":"1970-01-01",
                "dateOfDeath":null,
                "isActive":true,
                "photo":null,
                "created":"2017-10-28T13:25:07.293323Z",
                "modified":"2017-10-28T13:25:07.302084Z"
                },
                "isLive":false,
                "isOfficial":true,
                "resultsUrl":"https://api.isuresults.eu/events/2022_AUT_0002/competitions/1/results/",
                "personalBestsUrl":"https://api.isuresults.eu/events/2022_AUT_0002/competitions/1/personal-bests/",
                "lastUpdate":"2022-01-28T09:45:17Z",
                "created":"2022-01-02T09:23:10.817645Z",
                "modified":"2022-01-30T11:39:34.878784Z"
                },
                {...}
]
```

## Results of distance of given event
https://api.isuresults.eu/events/2022_AUT_0002/competitions/1/results/?inSeconds=0
- inSeconds=0 : if 0-> Time has format mm:ss.fff otherwise it would be ss.fff <br>
Example output:
```json
[{
    "id":71372,
    "type":"ind",
    "competitor":{
        "number":147,
        "identifier":"F147",
        "skater":{
            "id":1893,
            "firstName":"Pien",
            "lastName":"Smit",
            "country":"NED",
            "gender":"F",
            "dateOfBirth":"2004-03-25",
            "dateOfDeath":null,
            "isActive":false,
            "iocCode":"SSNED22503200401",
            "photo":null,
            "personalBestUrl":"https://api.isuresults.eu/skaters/1893/personal-best/",
            "created":"2021-11-25T19:41:56.985231Z",
            "modified":"2021-11-25T19:41:56.985231Z"}
            },
            "startNumber":24,
            "startLane":"I",
            "armband":"white",
            "rank":1,
            "status":0,
            "time":"39.388",
            "timeBehind":"0.000",
            "reskate":0,
            "isOfficial":true,
            "created":"2022-01-27T18:02:51.871003Z",
            "modified":"2022-01-28T09:45:16.488787Z",
            "laps":[{
                "number":1,
                "time":"10.85",
                "passageTime":"10.851",
                "rank":3},
                {"number":2,
                "time":"28.53",
                "passageTime":"39.388",
                "rank":1
                }]},
    {...},
```

# additional Features (kind of useless but nice to have for me)
- define number of ranking (rank 1 to ?? e.g. Rank 1 to 5 or top ten)
- get other positions of given nationality (defined by 3letter Code e.g. GER, NED)

# known issues
- when two events are listed as "live" the numbers get out of order. 
- Mass Start Events currently not working
