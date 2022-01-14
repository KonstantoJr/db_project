import sqlite3


def generate(db_path):
    # pteryga = ["A1", "A2"]
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        sql = """SELECT ID_DOMATIOU FROM ESTIA"""
        results = cursor.execute(sql).fetchall()
        id_domatiou = [id[0] for id in results]
        # print(id_domatiou)
        sql = """SELECT TOPOTHESIA , COUNT(TOPOTHESIA)
        FROM ESTIA
        GROUP BY TOPOTHESIA"""
        results = cursor.execute(sql).fetchall()
        topothesia = [(top[0], top[1]) for top in results]
        # print(topothesia)
        dx = 0
        for rooms in range(len(topothesia)):
            for room in range(topothesia[rooms][1]):
                sql = """INSERT INTO DOMATIA
                VALUES (?,?,?);"""
                if room > (topothesia[rooms][1] // 2):
                    if topothesia[rooms][1] % 2 == 0:
                        orofos = 2
                        aritmos = room % (topothesia[rooms][1] // 2)
                    else:
                        orofos = 2
                        aritmos = (room - 1) % (topothesia[rooms][1] // 2) + 1
                else:
                    orofos = 1
                    aritmos = room + 1
                cursor.execute(sql, (id_domatiou[room + dx], orofos, aritmos))
            dx += topothesia[rooms][1]
        # cursror.execute(sql, (m1, m2,m3))

        connection.commit()


if __name__ == "__main__":
    generate("merimna.db")
