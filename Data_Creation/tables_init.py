import sqlite3


def generate(db_path):
    conn = sqlite3.connect(db_path)
    with open("database.sql", "r") as file:
        sql = ""
        for row in file:
            sql += row
        sql = sql.split(";")
    for query in sql:
        cur = conn.cursor()
        cur.execute(query)
