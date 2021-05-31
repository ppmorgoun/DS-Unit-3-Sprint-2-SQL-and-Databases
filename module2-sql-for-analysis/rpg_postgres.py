import psycopg2
import os
import csv
import pandas as pd


dbname = os.environ['PG_DB']
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
host = os.environ['PG_HOST']

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

table_paths = {'main_armory_item': 'item_id int PRIMARY KEY, name varchar(30), value int, weight int',
               'main_armory_weapon': 'item_ptr_id int PRIMARY KEY, power int',
              'main_auth_group': 'id int PRIMARY KEY, name varchar(80)',
               'main_auth_group_permissions': 'id int PRIMARY KEY, group_id int, permission_id int',
              'main_auth_permission': 'id int PRIMARY KEY, content_type_id int, codename varchar(100), name varchar(255)',
               'main_auth_user': 'id int PRIMARY KEY, password varchar(128), last_login datetime, is_super_user bool, username varchar(150), first_name varchar(30), email varchar(254), is_staff bool, is_active bool, date_joined datetime, last_name varchar(150)',
              'main_auth_user_groups': 'id int PRIMARY KEY, user_id int, group_id int',
               'main_auth_user_user_permissions': 'id int PRIMARY KEY, user_id int, permission_id int',
              'main_charactercreator_character': 'character_id int PRIMARY KEY, name varchar(30), level int, exp int, hp int, strength int, intelligence int, dexterity int, wisdom int',
               'main_charactercreator_character_inventory': 'id int PRIMARY KEY, character_id int, item_id int',
              'main_charactercreator_cleric': 'character_ptr_id int PRIMARY KEY, using_shield bool, mana int',
               'main_charactercreator_fighter': 'character_ptr_id int PRIMARY KEY, using_shield bool, rage int',
              'main_charactercreator_mage': 'character_ptr_id int PRIMARY KEY, has_pet bool, mana int',
               'main_charactercreator_necromancer': 'mage_ptr_id int PRIMARY KEY, talisman_charged bool',
              'Assignment/main_charactercreator_thief': 'character_ptr_id int PRIMARY KEY, is_sneaking bool, energy int',
               'main_django_admin_log': 'id int PRIMARY KEY, object_id text, object_repr varchar(200), action_flag int, change_message text, content_type_id int, user_id int, action_time datetime',
              'main_django_content_type': 'id int PRIMARY KEY, app_label varchar(100), model varchar(100)',
               'main_django_migrations': 'id int PRIMARY KEY, app varchar(255), name varchar(255), applied bool',
              'main_django_session': 'session_key varchar(40) PRIMARY KEY, session_data text, expire_date datetime',
               'main_sqlite_master': 'type text, name text, tbl_name text, rootpage int, sql text',
              'main_sqlite_sequence': 'name text, seq int'}



#for table, cols in table_paths.items():
##    q = f'CREATE table {table} ({cols})'
 #   curs.execute(q)
 #   with open(f'Assignment/{table}.csv', 'r') as f:
 #       # Notice that we don't need the `csv` module.
 #       #next(f) # Skip the header row.
 #       curs.copy_from(f, table, sep=',')
 #   conn.commit()
conn.close()