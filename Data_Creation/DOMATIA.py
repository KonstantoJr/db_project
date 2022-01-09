import sqlite3
import pandas as pd


def generate(excel_path, db_path):
    df = pd.read_excel(excel_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    for index, row in df.iterrows():
        cursor.execute(
            f"""INSERT INTO DOMATIA
        VALUES ({row["ID_DOMATIOU"]},{row["OROFOS"]},{row["ARITHMOS"]},'{row["PTERYGA"]}');"""
        )

    ##cursror.execute(sql, (m1, m2,m3))

    connection.commit()
