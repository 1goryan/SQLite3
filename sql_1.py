import sqlite3
from random import randint




global db
global sql
db = sqlite3.connect('server.db') #переменная отвечает за подключение к БД
sql = db.cursor() #создаем курсор

sql.execute("""CREATE TABLE IF NOT EXISTS users (
        login TEXT,
        password TEXT,
        cash BIGINT
    )""")
db.commit()

def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?,?,?)", (user_login, user_password, 0))
        db.commit()
        print("registred")
    else:
        print("such a record already exists")

        for value in sql.execute("SELECT * FROM users"):
            print(value) 

def add_money():
    user_login = input('Log in: ')
    user_password = input('Password: ')
    number = randint(1, 2)

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    sql.execute(f"SELECT password FROM users WHERE password = '{user_password}'")

    if sql.fetchone() is None:
        print("This login or password isn't exist")
        reg()     
        
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = {1000} WHERE login = '{user_login}'")
            db.commit()
        else:
            print('You lose')

def enter():
    for i in sql.execute("SELECT login, password, cash FROM users"):
        print(i)

def main():
    add_money()
    enter()

main()