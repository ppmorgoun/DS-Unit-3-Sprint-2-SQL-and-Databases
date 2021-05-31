import sqlite3

# Creating a new database called demo_data
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Creating a table named demo and specifying the schema
create_q = 'CREATE table demo (' \
    's text,' \
    'x int,' \
    'y int)'
curs.execute(create_q)
conn.commit()

# Creating a show_all query for later
show_all = 'SELECT * FROM demo'

# Creating our insert query to insert the required data
insert = 'INSERT into demo VALUES (\'g\', 3, 9), (\'v\', 5, 7), (\'f\', 8, 7)'
curs.execute(insert)

# Testing to see if the insert query worked
print(curs.execute(show_all).fetchall())

# Committing the table
conn.commit()

# Testing our table with some queries
row_count = 'SELECT COUNT(*) from demo'
xy_at_least_5 = 'SELECT COUNT(*) from demo WHERE x > 4 AND y > 4'
unique_y = 'SELECT COUNT(DISTINCT y) from demo'

print(curs.execute(row_count).fetchall())
print(curs.execute(xy_at_least_5).fetchall())
print(curs.execute(unique_y).fetchall())

conn.close()
