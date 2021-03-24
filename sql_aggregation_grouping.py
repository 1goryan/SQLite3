import sqlite3 as sq

with sq.connect("games.db") as db:
    cursor = db.cursor()
    
    #cursor.execute("""DROP TABLE games""") #Удалить таблицу
    cursor.execute("""CREATE TABLE IF NOT EXISTS games( 
        user_id INTENGER,
        score INTENGER,
        time INTENGER
        )""")

    def add_user(user_id, score, time):
        cursor.execute("""INSERT INTO games (user_id, score, time) VALUES ({},{},{})""".format(user_id, score, time))

    #add_user(1, 200, 100000)
    #add_user(1, 300, 110010)   
    #add_user(2, 500, 100010)
    #add_user(1, 400, 201034)
    #add_user(3, 100, 200010)
    #add_user(2, 600, 210000)
    #add_user(2, 300, 210010)

    def show_db():
        cursor.execute("""SELECT * FROM games""")
        resault = cursor.fetchall()
        for i in resault:
            print(i)

    #show_db()

    #cursor.execute(""" SELECT count (user_id)  FROM games WHERE user_id = 1""") #Подсчет сколько раз в поле встречается уникальное значение
    #cursor.execute(""" SELECT DISTINCT user_id  FROM games""") #подсчет сколько уникальных значений в поле
    #cursor.execute("""SELECT sum(score) FROM games WHERE user_id = 1 """) #подсчет суммы значенией в поле скор с условием
    cursor.execute(""" SELECT user_id, sum(score) FROM games GROUP BY user_id""") #группировка значений по полю
        
    resault = cursor.fetchall()
    print(resault)
    