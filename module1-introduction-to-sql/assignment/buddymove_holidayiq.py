import pandas as pd
import sqlite3

df = pd.read_csv('../buddymove_holidayiq.csv')
df.head()

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
# df.to_sql('buddymove_holidayiq', con = conn)

test_q = 'SELECT * FROM buddymove_holidayiq'
results = curs.execute(test_q).fetchall()
#columns = [col[0] for col in curs.description()]
data = pd.DataFrame(results)
data.head()

# Count how many rows you have - it should be 249!
count = 'SELECT COUNT(*) FROM buddymove_holidayiq'
print(f'Number of rows: {curs.execute(count).fetchall()[0][0]}')

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100
# in the Shopping category?
reviews = 'SELECT COUNT(*) ' \
          'FROM buddymove_holidayiq ' \
          'WHERE Nature > 100 ' \
          'AND Shopping > 100'
print(f'Number of users who reviewed at least 100 Nature and Shopping: {curs.execute(reviews).fetchall()[0][0]}')


# What are the average number of reviews for each category?
avg = 'SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic) ' \
      'FROM buddymove_holidayiq'
print(f'Average number of reviews per category: {curs.execute(avg).fetchall()[0]}')

conn.close()