# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
# cursorObject.execute("DROP DATABASE contactsdjango")
cursorObject.execute("CREATE DATABASE contactsdjango")

print("All Done!")

# python mydb.py