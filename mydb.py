import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

cursorObject = dataBase.cursor()

#create a database

cursorObject.execute('CREATE DATABASE zoho')
print('All Done!')