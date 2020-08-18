import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_user_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, password TEXT, email TEXT)"
                                                         
cursor.execute(create_user_table)

connection.commit()

connection.close()