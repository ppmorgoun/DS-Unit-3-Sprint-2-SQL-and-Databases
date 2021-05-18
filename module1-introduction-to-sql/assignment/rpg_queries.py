import sqlite3
from queries import *
"""
Use sqlite3 to load and write queries to explore the data, and answer the following questions.
You should store each query as a string and label each as the indicated variable names.
Also, store each of these queries in a seperate file named queries.py and either run these queries in the file
or import them into another:

TOTAL_CHARACTERS: How many total Characters are there?
TOTAL_SUBCLASS: How many of each specific subclass (the necromancer table)?
TOTAL_ITEMS: How many total Items?
WEAPONS: How many of the Items are weapons?
NON_WEAPONS: How many of the items are not weapons?
CHARACTER_ITEMS: How many Items does each character have? (Return first 20 rows)
CHARACTER_WEAPONS: How many Weapons does each character have? (Return first 20 rows)
AVG_CHARACTER_ITEMS: On average, how many Items does each Character have?
AVG_CHARACTER_WEAPONS: On average, how many Weapons does each character have?
"""
conn = sqlite3.connect('../rpg_db.sqlite3')
curs = conn.cursor()

curs.execute(TOTAL_CHARACTERS)
print('Total number of characters: ', curs.fetchall()[0][0])

curs.execute(TOTAL_SUBCLASS)
print('Total number of specific necromancer subclasses available: ', curs.fetchall()[0][0])

curs.execute(TOTAL_ITEMS)
print('Total number of items: ', curs.fetchall()[0][0])

curs.execute(WEAPONS)
print('Total number of items that are weapons: ', curs.fetchall()[0][0])

curs.execute(NON_WEAPONS)
print('Total number of items that are not weapons: ', curs.fetchall()[0][0])

curs.execute(CHARACTER_ITEMS)
print('The number of items that each character has (showing 20): ', curs.fetchall())

curs.execute(CHARACTER_WEAPONS)
print('The number of weapons each character has (showing 20): ', curs.fetchall())

curs.execute(AVG_CHARACTER_ITEMS)
print('Average number of weapons each character has: ', curs.fetchall()[0][0])

curs.execute(AVG_CHARACTER_WEAPONS)
print('Average number of weapons each character has: ', curs.fetchall()[0][0])