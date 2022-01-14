import sqlite3
import input_utils as iu


class DB_Connection:
    def __init__(self, db_path) -> None:
        self.conn = sqlite3.connect(db_path)

    def print_application(self, eidos) -> list:
        sql = ""
        if eidos == "SITHSHS":
            sql = """SELECT * ,(SYNOLIKO_EISODHMA_PATROS + SYNOLIKO_EISODHMA_MHTROS) AS SYNOLIKO 
            FROM AITHSH_SITHSHS WHERE ID IN
            (SELECT ID FROM KANEI_AITHSH WHERE EIDOS_AITHSHS = 'SITHSHS' AND KATASTASH = 'SE ANAMONH')
            ORDER BY SYNOLIKO"""
        elif eidos == "ESTIAS":
            sql = """SELECT * ,(SYNOLIKO_EISODHMA_PATROS + SYNOLIKO_EISODHMA_MHTROS + SYNOLIKO_EISODHMA_IDIOU) AS SYNOLIKO
            FROM AITHSH_STEGASHS WHERE ID IN
            (SELECT ID FROM KANEI_AITHSH WHERE EIDOS_AITHSHS = 'ESTIAS' AND KATASTASH = 'SE ANAMONH')
            ORDER BY SYNOLIKO"""
        cursor = self.conn.cursor()
        results = cursor.execute(sql).fetchall()
        names = [description[0] for description in cursor.description]
        print(names)
        ids = [row[0] for row in results]
        for i in results:
            print(i)
        return ids

    def select_appl_to_review(self, id, eidos_aithshs) -> None:
        if eidos_aithshs == "ESTIAS":
            sql = f"""SELECT * ,(SYNOLIKO_EISODHMA_PATROS + SYNOLIKO_EISODHMA_MHTROS+SYNOLIKO_EISODHMA_IDIOU) AS SYNOLIKO
            FROM AITHSH_STEGASHS WHERE ID = {id}"""
        elif eidos_aithshs == "SITHSHS":
            sql = f"""SELECT * ,(SYNOLIKO_EISODHMA_PATROS + SYNOLIKO_EISODHMA_MHTROS) AS SYNOLIKO
            FROM AITHSH_SITHSHS WHERE ID = {id}"""
        cursor = self.conn.cursor()
        results = cursor.execute(sql).fetchall()
        if len(results) == 0:
            print("Wrong id number.")
            return
        names = [description[0] for description in cursor.description]
        print(names)
        print(results[0])
        sql = f"""SELECT * FROM EGGRAFA WHERE ID_AITHSHS = {id}"""
        results = cursor.execute(sql).fetchall()
        for res in results:
            print(res)
        print("Choose the result of the review.")
        katastash = iu.input_method(
            "Select 1 for OLOKLHROTHHKE\
        \nSelect 2 for ELLEIPHS\
        \nSelect 3 for APORRIFTHHKE",
            "Not a valid input.",
            {"1": "OLOKLHROTHHKE",
             "2": "ELLEIPHS", "3": "APORRIFTHHKE"})
        sql = f"""UPDATE KANEI_AITHSH
        SET KATASTASH = '{katastash}'
        WHERE ID = {id}"""
        cursor.execute(sql)
        self.conn.commit()

    def generate_karta_sithshs(self, start_date, end_date) -> None:
        sql = """SELECT ID , AM 
        FROM KANEI_AITHSH 
        WHERE KATASTASH = 'OLOKLHROTHHKE' AND EIDOS_AITHSHS = 'SITHSHS'"""
        cursor = self.conn.cursor()
        results = cursor.execute(sql)
        for id, am in results:
            sql = """INSERT INTO LAMVANEI
            VALUES(?,?)"""
            card_id = len(cursor.execute(
                "SELECT * FROM LAMVANEI").fetchall()) + 1
            cursor.execute(sql, (am, card_id))
            sql = """ INSERT INTO KARTA_SITHSHS
            VALUES(?,?,?)"""
            cursor.execute(sql, (card_id, start_date, end_date))
            sql = f"""UPDATE KANEI_AITHSH
            SET KATASTASH = 'EPITYXHS'
            WHERE ID = {id}"""
            cursor.execute(sql)
        self.conn.commit()


if __name__ == "__main__":
    from datetime import datetime

    year = datetime.now().strftime("%Y")
    start_date = "1-09-" + year
    end_date = "31-08-" + str(int(year) + 1)
    db = DB_Connection("Data_Creation/merimna.db")
    db.print_food_appl()
    # db.print_housing_appl()
    # db.select_appl_to_review(1, "SITHSHS")
    db.generate_karta_sithshs(start_date, end_date)
