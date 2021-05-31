import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Creating our basic table with 3 columns
create_q = 'CREATE table demo (' \
    's text,' \
    'x int,' \
    'y int)'
curs.execute(create_q)
conn.commit()

# Inserting our 3 rows into the demo table
insert = 'INSERT into demo VALUES (\'g\', 3, 9), (\'v\', 5, 7), (\'f\', 8, 7)'
curs.execute(insert)

show_all = 'SELECT * FROM demo'
print(curs.execute(show_all).fetchall())
conn.commit()

# Testing out our new table with 3 simple queries
row_count = 'SELECT COUNT(*) from demo'
xy_at_least_5 = 'SELECT COUNT(*) from demo WHERE x > 4 AND y > 4'
unique_y = 'SELECT COUNT(DISTINCT y) from demo'

print(f'Amount of rows our table has: {curs.execute(row_count).fetchall()}')
print(f'Amount of rows where columns X and Y are atleast 5: {curs.execute(xy_at_least_5).fetchall()}')
print(f' Number of unique values in column Y: {curs.execute(unique_y).fetchall()}')
