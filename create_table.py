import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tests"
)

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE lab_tests (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, mrp FLOAT NOT NULL, discount FLOAT NULL, price FLOAT NULL, provider_id INT NOT NULL)")

print('Table created...')
