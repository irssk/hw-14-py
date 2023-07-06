import sqlite3

connect = sqlite3.connect("database.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
Clients (
client_id INTEGER PRIMARY KEY AUTOINCREMENT ,
client_name TEXT,
client_surname TEXT,
client_coins INT);
""")

connect.commit()

client_name = input("Please enter your name: ")
client_surname = input("Please enter your surname: ")
client_coins = input("Please enter the number of coins you have: ")

P="insert into Clients (client_name, client_surname, client_coins) values ('"+client_name+"','"+client_surname+"','"+client_coins+"')"

cursor.execute(P)

connect.commit()