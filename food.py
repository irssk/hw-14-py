import sqlite3

connect = sqlite3.connect("database.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
Food (
food_id INTEGER PRIMARY KEY AUTOINCREMENT ,
label TEXT,
cost INT);
""")

connect.commit()

label = input("Please enter the name of the dish: ")
cost = input("Please enter the cost of the dish: ")


P="INSERT INTO Food (label, cost) values ('"+label+"','"+cost+"')"

cursor.execute(P)

connect.commit()