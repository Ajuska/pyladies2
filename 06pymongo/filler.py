from pymongo import MongoClient
from faker import Faker

client = MongoClient()
db = client['pyladies']
phones = db['phones']


faker = Faker('cs_CZ')
phones.drop() #remove maze jednotlive zaznamy, drop smaze fyzicky soubor

for i in range(10000):
    phones.insert({
        "name": faker.name(),
        "phone": faker.phone_number(),
    })

print("Kolekce phones ma {0} zaznamu".format(phones.count()))
