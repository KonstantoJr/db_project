import sqlite3
import random
import random_date

def generate(db_path):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        sql = """SELECT AM FROM FOITHTHS"""
        results = cursor.execute(sql).fetchall()
        ID=1
        sql = f"""INSERT INTO AGORA_KOUPONION
        VALUES(?,?,?,?,?)"""
        for am in results:
            for j in range(random.randint(0,2)):
                date = random_date.random_date(am[0]+ j)
                posotita = random.randint(5,10)
                cursor.execute(sql, (ID, am[0], date, posotita, posotita*2))
                ID += 1
        # cursror.execute(sql, (m1, m2,m3))

        connection.commit()

