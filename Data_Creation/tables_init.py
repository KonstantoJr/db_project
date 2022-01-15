import sqlite3

# A functions that reads the contents of an 
# sql file and creates the database file
def generate(script_path, db_path):
    with sqlite3.connect(db_path) as conn:
        with open(script_path, "r") as file:
            sql = ""
            for row in file:
                sql += row
            sql = sql.split(";")
        for query in sql:
            cur = conn.cursor()
            cur.execute(query)
