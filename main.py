import mysql.connector
import pandas as pd

i = 360


def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbname"
    )


def insert(name, mrp, discount, price, provider_id):
    mydb = database_connect()
    mycursor = mydb.cursor()

    sql = "INSERT INTO lab_tests (name, mrp, discount, price, provider_id) VALUES (%s, %s, %s, %s, %s)"
    val = (name, mrp, discount, price, provider_id)

    mycursor.execute(sql, val)
    mydb.commit()

    global i
    print(f"[{i}] {name} = record inserted...")
    i += 1


def app():
    df = pd.read_csv('tests.csv')

    for index, row in df.iloc[0:].iterrows():
        mrp = float(row['MRP'].strip().replace(',', ''))
        provider_id = 1

        insert(row['Name'].strip(), mrp, 0, mrp, provider_id)


if __name__ == '__main__':
    app()
