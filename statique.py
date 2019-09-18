import urllib3
API_KEY = "72e8588f830327a17b61280992faa24f6887b8e4"
http = urllib3.PoolManager()
import json

def liste_contract() :
    url = "https://api.jcdecaux.com/vls/v3/contracts?apiKey="+API_KEY
    r = http.request('GET', url)
    l = json.loads(r.data)
    return [i["name"] for i in l]

def liste_stations_ville(ville) :
    url = "https://api.jcdecaux.com/vls/v3/stations?contract="+ville+"&apiKey="+API_KEY
    r = http.request('GET', url)
    l = json.loads(r.data)
    return l

def info_station(ville, numero) :
    url = "https://api.jcdecaux.com/vls/v3/stations/"+str(numero)+"?contract="+ville+"&apiKey="+API_KEY
    r = http.request('GET', url)
    l = json.loads(r.data)
    return l

l = liste_stations_ville("lyon")
r = []
for k in l :
    r.append((k["number"], k["totalStands"]["capacity"]))
r = sorted(r, key=lambda x: x[0])
r = [i[1] for i in r]

with open("statique.json", "w") as f :
    json.dump(r, f)
