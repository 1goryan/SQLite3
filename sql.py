import sqlite3 as sq

with sq.connect("saper.db") as db:
    cursor = db.cursor()
    """Создаем таблицу с набором полей и типом данных в них"""
    #cursor.execute("""DROP TABLE users""") #Удалить таблицу
    cursor.execute("""CREATE TABLE IF NOT EXISTS users( 
        user_id INTENGER PRIMARY KEY,
        name TEXT NOT NULL,
        sex TEXT NOT NULL,
        old INTENGER,
        score INTENGER
        )""")
    
    def add_user(user_id, name, sex, old, score):
        cursor.execute("""INSERT INTO users (user_id, name, sex, old, score) VALUES ({},{},{},{},{})""".format(user_id, name, sex,  old, score))

    def show_db():
        cursor.execute("""SELECT * FROM users""")
        resault = cursor.fetchall()
        for i in resault:
            print(i)

    def order(pole, deck = " "):
        cursor.execute("""SELECT * FROM users ORDER BY {} {}""".format(pole, deck))
        a = cursor.fetchall()
        for i in a:
            print(i)
    
    #add_user(0, "'Ihor'", "'male'", 21, 0)
    #add_user(1, "'Anton'", "'male'", 19, 500)
    #add_user(2, "'Julia'", "'female'", 19, 0)
    #add_user(3, "'Nika'", "'female'", 19, 0)
    #add_user(4, "'Sergei'", "'male'", 25, 1500)
    #add_user(5, "'Kate'", "'female'", 15, 0)
    #add_user(6, "'Slavik'", "'male'", 22, 300)

    #order("old","DESC")
    #show_db()
    
    #cursor.execute("SELECT name FROM users WHERE score > 100")#Выбор определенных данных с условием
    #a = cursor.fetchall()
    #print(a)

    #cursor.execute("""UPDATE users SET name = 'IHOR' WHERE name == 'Ihor' """)#Изменение данных в базе данных
    #cursor.execute("DELETE FROM users WHERE score = 300") #Удаление данных по условию
    
    

   

