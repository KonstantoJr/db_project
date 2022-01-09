import sqlite3
import pandas as pd
import random_date


def generate(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT AM FROM FOITHTHS")
    am = cursor.fetchall()

    cursor.execute("SELECT ID FROM KANEI_AITHSH")
    ID = cursor.fetchall()
    num = len(ID)
    for t in am:
        num += 1
        date = random_date.random_date(t[0])
        cursor.execute(
            f"""INSERT INTO KANEI_AITHSH
        VALUES ({num},{t[0]},'{date}','SE ANAMONH','SITHSHS');"""
        )
        num += 1
        cursor.execute(
            f"""INSERT INTO KANEI_AITHSH
        VALUES ({num},{t[0]},'{date}','SE ANAMONH','ESTIAS');"""
        )

    ##cursror.execute(sql, (m1, m2,m3))

    connection.commit()
