import pymongo

#vytvoreni databaze
client = pymongo.MongoClient()
#pristup k databazi
db = client['pyladies']
#pristup ke kolekci
phones = db['phones']

for radek in phones.find():
    print(radek)
