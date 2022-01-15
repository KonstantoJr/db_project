import sqlite3
import pandas as pd
import random

# A function to generate some data for the table AITHSH_SITHSHS
def generate(excel_path, db_path):
    df = pd.read_excel(excel_path)
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        # sql query to retrieve all the AM , ID that exist already in the db
        cursor.execute(
            "SELECT DISTINCT AM,ID FROM KANEI_AITHSH WHERE EIDOS_AITHSHS='SITHSHS'"
        )
        AM = cursor.fetchall()

        for i in range(len(AM)):
            am = AM[i][0]
            id = AM[i][1]
            random.seed(AM[i][0])
            etos = random.randint(2015, 2021)
            katoikia = df.iat[i, 0]
            monimh = df.iat[i, 1]
            barcode = random.randint(100000000000, 999999999999)
            eis_patros = random.randint(4000, 40000)
            eis_mitros = random.randint(4000, 40000)
            meli_oik = random.randint(3, 8)
            # A query to insert the random generated data
            cursor.execute("""INSERT INTO AITHSH_SITHSHS
            VALUES (?,?,?,?,?,?,?,?,?);""",
                           (id, am, etos, katoikia, monimh,
                            barcode, eis_patros, eis_mitros,  meli_oik)
                           )


        connection.commit()
