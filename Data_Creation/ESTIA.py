import sqlite3


def generate(db_path):
    loc = ["ΡΙΟ", "ΚΟΥΚΟΥΛΙ", "ΑΓΡΙΝΙΟ"]
    name = ["ΦΟΙΤΗΤΙΚΗ ΕΣΤΙΑ ΠΑΤΡΑΣ", "ΚΟΥΚΟΥΛΙ ΠΑΤΡΩΝ",
            "ΦΟΙΤΗΤΙΚΗ ΕΣΤΙΑ ΜΕΣΟΛΟΓΓΙΟΥ"]
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        id = 0
        order = 0
        rooms = [15, 10, 10]
        sql = """INSERT INTO ESTIA
        VALUES(?,?,?)"""
        for j in range(3):
            for i in range(rooms[j]):
                id += 1
                cursor.execute(sql, (loc[order], name[order], id))
            order += 1
        # cursror.execute(sql, (m1, m2,m3))

        connection.commit()
