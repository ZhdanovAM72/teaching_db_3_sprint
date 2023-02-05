import sqlite3


# Если в текущей директории нет файла db.sqlite - 
# он будет создан; сразу же будет создано и соединение с базой.
# Если файл существует, функция connect просто подключится к базе.
con = sqlite3.connect('db.sqlite')

# Создаём специальный объект cursor для работы с БД.
# Вся дальнейшая работа будет вестись через методы этого объекта.
cur = con.cursor()

# Готовим SQL-запросы.
# Для читаемости кода запрос обрамлён в тройные кавычки и разбит построчно.
cur.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday_year INTEGER
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);
''')

#directors = [
#    (1, 'Текс Эйвери', 1908),
#    (2, 'Роберт Земекис', 1952),
#    (3, 'Джерри Чиникей', 1912),
#]
movies = [
    (1, 'Весёлые мелодии', 'Мультсериал', 1930),
    (2, 'Кто подставил кролика Роджера', 'Фильм', 1988),
    (3, 'Безумные Мелодии Луни Тюнз', 'Мультсериал', 1931),
    (4, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969),
]

#cur.executemany('INSERT OR IGNORE INTO directors VALUES(?, ?, ?);', directors)
cur.executemany('INSERT OR IGNORE INTO movies VALUES(?, ?, ?, ?);', movies)

#cur.execute('''
#INSERT INTO movies(id, name, type, release_year)
#VALUES (1, 'Весёлые мелодии', 'Мультсериал', 1930);
#''') 

#cur.execute(
#    'INSERT INTO movies VALUES(?, ?, ?);',
#    ('Весёлые мелодии', 'Мультсериал', 1930)
#)

# Применяем запросы.
# Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# пока не вызван метод commit().
con.commit()

# Закрываем соединение с БД.
con.close()
