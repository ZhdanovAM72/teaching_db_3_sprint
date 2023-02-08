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

# Связи в таблице 1к1
import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS wrappers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    wrapper_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(wrapper_id) REFERENCES wrappers(id)
);
''')

con.commit()
con.close()

# Получение значений связанных таблиц
import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.execute('''
SELECT ice_cream.name,
       wrappers.name
FROM ice_cream,
     wrappers
WHERE ice_cream.wrapper_id = wrappers.id AND wrappers.name = 'Бумажная с черепами';
''')

for result in cur:
    print(result)

con.close()


# 1 к многим категории таваров
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY,
    slug TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);
''')

con.commit()
con.close()


# Получаем информацию о макс цене группируя по категории и сортируя по убыванию цены
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT ice_cream.name,
       categories.slug,
       MAX(ice_cream.price)
       
FROM ice_cream,
     categories
WHERE ice_cream.category_id = categories.id
GROUP BY categories.slug ORDER
BY ice_cream.price DESC;
''')

for result in cur:
    print(result)

con.commit()
con.close()


# Присоединение таблицы с условием поиска
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT ice_cream.name,
       wrappers.name
FROM ice_cream
JOIN wrappers ON ice_cream.wrapper_id = wrappers.id
WHERE wrappers.name LIKE '%праздн%'
''')

for result in cur:
    print(result)

con.commit()
con.close()


import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT ice_cream.name,
       categories.slug,
       wrappers.name,
       MIN(ice_cream.price),
       AVG(ice_cream.price)
FROM ice_cream
JOIN categories ON ice_cream.category_id = categories.id
LEFT JOIN wrappers ON ice_cream.wrapper_id = wrappers.id
GROUP BY categories.id
''')

for result in cur:
    print(result)

con.commit()
con.close()


import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS toppings(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream_toppings(
id INTEGER PRIMARY KEY,
ice_cream_id INTEGER NOT NULL UNIQUE,
topping_id INTEGER NOT NULL,
FOREIGN KEY(topping_id) REFERENCES toppings(id),
FOREIGN KEY(ice_cream_id) REFERENCES ice_cream(id)
);
''')

con.commit()
con.close()

# Добавление новых столбцов в таблице
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
ALTER TABLE ice_cream
ADD COLUMN is_published INTEGER;
ALTER TABLE ice_cream
ADD COLUMN is_on_main INTEGER;
''')

con.commit()
con.close()


# Переименование колонки
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
ALTER TABLE ice_cream
RENAME COLUMN description TO specification;
''')

con.commit()
con.close()

# Удаление таблицы
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
DROP TABLE ice_cream;
''')

con.commit()
con.close()