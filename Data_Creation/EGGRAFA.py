import sqlite3
import random


def generate(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = """SELECT ID FROM KANEI_AITHSH"""
    ids = cursor.execute(sql).fetchall()
    # print(ids)
    random.seed(1066546)
    onoma = [
        "/home/konstantinos/data/ekkatharistiko.pdf",
        "/home/konstantinos/data/bebaiosh.pdf",
        "/home/konstantinos/data/paso.pdf",
        "/home/konstantinos/data/spoudon.pdf",
        "/home/konstantinos/data/oikogeniakis_katastashs.pdf",
    ]
    for id in ids:
        for i in range(random.randint(2, 5)):
            sql = """INSERT INTO EGGRAFA(ID_AITHSHS , ONOMA)
            VALUES(?,?)"""
            cursor.execute(sql, (id[0], onoma[i]))
            # print(id[0], onoma[i])
    conn.commit()


if __name__ == "__main__":
    generate("Data_Creation/merimna.db")
