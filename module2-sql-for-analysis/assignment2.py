import pandas as pd
import psycopg2
import os

dbname = 'eiquvoxh'
user = 'eiquvoxh'
password = 'JlN6dQH6rW2fiKl799-AjQQByQdJ6yCZ'
host = 'rosie.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

titanic_path = 'titanic.csv'
make_table = "CREATE table titanic (Pclass int, Name varchar(50), Sex varchar(10), Age float, Siblings_or_Spouses_Aboard int, Parents_or_Children_Aboard int, Fare float)"

curs.execute(make_table)
with open(titanic_path, 'r') as f:
        curs.copy_from(f, 'titanic', sep=',')
conn.commit()

curs.execute("SELECT * from titanic").fetchall()