import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT *
FROM movies
WHERE type = NULL;
''')

# cur.execute('''
# SELECT name,
#        release_year
# FROM movies
# WHERE (release_year BETWEEN 1965 AND 1990) AND type LIKE '%ильм';
# ''')



for result in cur:
    print(result)
