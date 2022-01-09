import sqlite3
import pandas as pd
import random


def generate(excel_path, db_path):
    df = pd.read_excel(excel_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT DISTINCT AM,ID FROM KANEI_AITHSH WHERE EIDOS_AITHSHS='SITHSHS'"
    )
    AM = cursor.fetchall()

    for i in range(len(AM)):
        random.seed(AM[i][0])
        etos = random.randint(2015, 2021)
        barcode = random.randint(100000000000, 999999999999)
        eis_patros = random.randint(4000, 40000)
        eis_mitros = random.randint(4000, 40000)
        meli_oik = random.randint(3, 8)
        cursor.execute(
            f"""INSERT INTO AITHSH_SITHSHS
	    VALUES ({AM[i][1]},{AM[i][0]},{etos},'{df.iat[i,0]}','{df.iat[i,1]}',{barcode},{eis_patros}, {eis_mitros}, {meli_oik});"""
        )

    ##cursror.execute(sql, (m1, m2,m3))

    connection.commit()
