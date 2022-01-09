import sqlite3
import pandas as pd


def generate(excel_path, db_path):
    df = pd.read_excel(excel_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    for index, row in df.iterrows():
        name = row["Name"]
        AM = row["AM"]
        PHONE = row["PHONE"]
        cursor.execute(
            f"""INSERT INTO FOITHTHS
        VALUES ({row["AM"]},'{row["Name"]}',{row["PHONE"]});"""
        )

    connection.commit()
