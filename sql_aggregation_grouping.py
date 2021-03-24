import sqlite3 as sq

with sq.connect("games.db") as db:
    cursor = db.cursor()
    
    #cursor.execute("""DROP TABLE ИМЯ""") #Удалить таблицу
    cursor.execute("""CREATE TABLE IF NOT EXISTS games( 
        user_id INTENGER,
        score INTENGER,
        time INTENGER
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS users( 
        user_id INTENGER PRIMARY KEY,
        name TEXT NOT NULL,
        sex TEXT NOT NULL,
        old INTENGER,
        score INTENGER
        )""")

    def add_user_games(user_id, score, time):
        cursor.execute("""INSERT INTO games (user_id, score, time) VALUES ({},{},{})""".format(user_id, score, time))
    def add_user_users(user_id, name, sex, old, score):
        cursor.execute("""INSERT INTO users (user_id, name, sex, old, score) VALUES ({},{},{},{},{})""".format(user_id, name, sex,  old, score))
    #add_user_games(1, 200, 100000)
    #add_user_games(1, 300, 110010)   
    #add_user_games(2, 500, 100010)
    #add_user_games(1, 400, 201034)
    #add_user_games(3, 100, 200010)
    #add_user_games(2, 600, 210000)
    #add_user_games(2, 300, 210010)

    def show_db():
        cursor.execute("""SELECT * FROM games""")
        resault = cursor.fetchall()
        for i in resault:
            print(i)

    #show_db()

    #cursor.execute(""" SELECT count (user_id)  FROM games WHERE user_id = 1""") #Подсчет сколько раз в поле встречается уникальное значение
    #cursor.execute(""" SELECT DISTINCT user_id  FROM games""") #подсчет сколько уникальных значений в поле
    #cursor.execute("""SELECT sum(score) FROM games WHERE user_id = 1 """) #подсчет суммы значенией в поле скор с условием
    #cursor.execute(""" SELECT user_id, sum(score) FROM games GROUP BY user_id""") #группировка значений по полю
    
    #add_user_users(0, "'Ihor'", "'male'", 21, 0)
    #add_user_users(1, "'Anton'", "'male'", 19, 500)
    #add_user_users(2, "'Julia'", "'female'", 19, 0)
    #add_user_users(3, "'Nika'", "'female'", 19, 0)
    #add_user_users(4, "'Sergei'", "'male'", 25, 1500)
    #add_user_users(5, "'Kate'", "'female'", 15, 0)
    #add_user_users(6, "'Slavik'", "'male'", 22, 300)
    
    #cursor.execute("""SELECT name, sex, games.score FROM games JOIN users ON games.user_id = users.rowid """)
    cursor.execute("""SELECT name, sex, sum(games.score) FROM games JOIN users ON games.user_id = users.rowid GROUP BY games.user_id ORDER BY games.score DESC """)
    resault = cursor.fetchall()
    for f in resault:
        print(f)
    