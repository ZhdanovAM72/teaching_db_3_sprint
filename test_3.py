import sqlite3

con = sqlite3.connect('test_db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS original_names(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    original_name_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(original_name_id) REFERENCES original_names(id)
);
''')

cur.execute('''
SELECT movies.name,
       original_names.name
FROM movies,
     original_names
WHERE movies.original_name_id = original_names.id;
''')

for result in cur:
    print(result)

# original_names = [
#     (1, 'Last Action Hero'),
#     (2, 'Murder, She Wrote'),
#     (3, 'Looney Tunes'),
#     (4, 'Il Buono, il brutto, il cattivo'),
#     (5, 'Who Framed Roger Rabbit'),
#     (6, 'Merrie Melodies')
# ]

# movies = [
#     (1, 'Безумные Мелодии Луни Тюнз', 3),
#     (2, 'Весёлые мелодии', 6),
#     (3, 'Кто подставил кролика Роджера', 5),
#     (4, 'Хороший, плохой, злой', 4),
#     (5, 'Последний киногерой', 1),
#     (6, 'Она написала убийство', 2)
# ]

# cur.executemany('INSERT INTO original_names VALUES(?, ?);', original_names)
# cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)

con.commit()
con.close()