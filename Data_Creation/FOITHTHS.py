import sqlite3
import pandas as pd

# A function to insert the data from an excel file to the db
# the excel needs to be like */excel_files/Names.xls
def generate(excel_path, db_path):
    df = pd.read_excel(excel_path)
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        for _, row in df.iterrows():
            name = row["Name"]
            AM = row["AM"]
            PHONE = row["PHONE"]
            cursor.execute(
                f"""INSERT INTO FOITHTHS
            VALUES (?,?,?);""", (AM, name, PHONE)
            )

        connection.commit()
