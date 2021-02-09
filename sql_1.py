import sqlite3

db = sqlite3.connect('server.db') #переменная отвечает за подключение к БД
sql = db.cursor() #создаем курсор

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")
db.commit()

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute("SELECT login FROM users")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES(?,?,?)", (user_login, user_password, 0))
    db.commit()
    print("registred")
else:
    print("such a record already exists")

    for value in sql.execute("SELECT * FROM users"):
        print(value[2]) 