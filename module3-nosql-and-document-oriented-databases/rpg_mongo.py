import os
import pymongo
import sqlite3
from dotenv import load_dotenv

load_dotenv()

pw = os.getenv('DB_PASSWORD')
user = os.getenv('DB_USERNAME')
name = os.getenv('DB_NAME')

mongo_client = pymongo.MongoClient(
    f"mongodb://{user}:{pw}@cluster0.mcy7x.mongodb.net/{name}?retryWrites=true&w=majority")

sqlite_conn = sqlite3.connect("../module1-introduction-to-sql/rpg_db.sqlite3")
sqlite_curs = sqlite_conn.cursor()
db = mongo_client.myFirstDatabase
if not 'rpg_data' in db.list_collection_name():
    db.create_collection('rpg_data')

character_query = """SELECT * FROM charactercreator_character"""
item_query = """SELECT * FROM armory_item left armory_weapon on armort_item.item_id = armory_weapon.item_ptr_id"""

# Query from sqlite and insert into mongo.

character_results = sqlite_curs.execute(character_query).fetchall()

for c in character_results:
    doc = {}
    keys = ['name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    db.rpg_data.insert_one(doc)
