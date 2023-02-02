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
CREATE TABLE IF NOT EXIST directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday_year INTEGER
);
''')
cur.execute('''
CREATE TABLE IF NOT EXIST movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
)
''';)

# Применяем запросы.
# Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# пока не вызван метод commit().
con.commit()

# Закрываем соединение с БД.
con.close()
