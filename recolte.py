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
    tmp = (k["number"], k["totalStands"]["availabilities"]["bikes"])
    r.append(tmp)

r = sorted(r, key=lambda x: x[0])
r = [i[1] for i in r]

import time
nom = "data/"+str(int(time.time()))+".json"
with open(nom, "w") as f :
    json.dump(r, f)
if True :
    import os
    os.system("git add " + nom)
    os.system("git commit -m 'la routine' " + nom)
    os.system("git push")
    os.system("rm " + nom)
