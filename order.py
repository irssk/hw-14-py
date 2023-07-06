import sqlite3

connect = sqlite3.connect("database.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
'Order' (
order_id INTEGER PRIMARY KEY AUTOINCREMENT ,
client_id INT,
dish_id INT);
""")

connect.commit()

client_id = input("Please enter the client's ID: ")
dish_id = input("Please enter the dish ID: ")

P="insert into 'Order' (client_id, dish_id) values ('"+client_id+"','"+dish_id+"')"

cursor.execute(P)

connect.commit()