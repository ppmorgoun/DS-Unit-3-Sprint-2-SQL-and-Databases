import os
import pymongo
import sqlite3
from dotenv import load_dotenv

load_dotenv()

pw = os.getenv('DB_PASSWORD')
user = os.getenv('DB_USERNAME')
name = os.getenv('DB_NAME')

mongo_client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{pw}@cluster0.mcy7x.mongodb.net/{name}?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

old = 'mongodb+srv://{user}:{pw}@cluster0.mcy7x.mongodb.net/{name}?retryWrites=true&w=majority'
new = 'mongodb+srv://USER:PASSWORD@cluster0.syvro.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
sqlite_conn = sqlite3.connect("../module1-introduction-to-sql/rpg_db.sqlite3")
sqlite_curs = sqlite_conn.cursor()
db = mongo_client['myFirstDatabase']

#db.create_collection('rpg_data')

character_query = """SELECT * FROM charactercreator_character"""
item_query = """SELECT * FROM armory_item left join armory_weapon where armory_item.item_id = armory_weapon.item_ptr_id"""
weapon_query = """SELECT * FROM armory_weapon left join armory_item where armory_weapon.item_ptr_id = armory_item.item_id"""
inventory_query = """SELECT * FROM charactercreator_character_inventory"""

# Query from sqlite and insert into mongo.

# Character data
character_results = sqlite_curs.execute(character_query).fetchall()

for c in character_results:
    doc = {}
    keys = ['name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    db.rpg_data.insert_one(doc)

# Item data
item_results = sqlite_curs.execute(item_query).fetchall()

for c in item_results:
    doc = {}
    keys = ['item_id', 'name', 'value', 'weight', 'power']
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    db.rpg_data.insert_one(doc)

# Item data
weapon_results = sqlite_curs.execute(weapon_query).fetchall()

for c in weapon_results:
    doc = {}
    keys = ['item_id', 'power', 'name', 'value', 'weight']
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    db.rpg_data.insert_one(doc)

# Inventory data
inventory_results = sqlite_curs.execute(inventory_query).fetchall()

for c in inventory_results:
    doc = {}
    keys = ['id', 'character_id', 'item_id']
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    db.rpg_data.insert_one(doc)
