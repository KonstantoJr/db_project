import sqlite3


class DB_Connection:
    def __init__(self, path_name) -> None:
        self.connection = None
        self.connection = sqlite3.connect(path_name)

    def insert_student(self, name, am, phone) -> None:
        cursor = self.connection.cursor()
        sql = """INSERT INTO FOITHTHS(AM , ONOMA , THLEFONO)
        VALUES(?,?,?)"""
        cursor.execute(sql, (am, name, phone))
        self.connection.commit()

    def insert_purchase(self, quantity, am, date, total):
        cursor = self.connection.cursor()
        sql = """INSERT INTO AGORA_KOUPONION(AM , HM_AGORAS, POSOTHTA , TIMH)
        VALUES(?,?,?,?)"""
        cursor.execute(sql, (am, date, quantity, total))
        self.connection.commit()

    def retrieval_query(self, sql) -> list:
        cursor = self.connection.cursor()
        results = cursor.execute(sql).fetchall()
        self.connection.commit()
        return results

    def clear_table(self, table):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE  FROM {table}")
        self.connection.commit()


if __name__ == "__main__":
    db = DB_Connection("merimna.db")
    # db.insert_student("Κώστας Κωνσταντόπουλος", 1066546, 6948647574)
    print(db.retrieval_query("SELECT * FROM FOITHTHS WHERE AM = 1066546"))
    # db.clear_table("FOITHTHS")
