import sqlite3
import input_utils as iu
import pandas as pd
import math


class DB_Connection:
    def __init__(self, db_path) -> None:
        self.conn = sqlite3.connect(db_path)
    # Prints all the pending for review applications
    # depending on the 'eidos'
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
        if len(results) == 0:
            print(f"No {eidos} application for review.")
            return None
        names = [description[0] for description in cursor.description]
        ids = [row[0] for row in results]
        # Pandas is used to print out the results of the following querries
        data = results
        df = pd.DataFrame(data, columns=names)
        if eidos == "SITHSHS":
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None, 'display.max_colwidth', -1):
                print(df.to_string(index=False))
        else:
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df.to_string(index=False))
        print()
        return ids

    # Given an id from the user the following function
    # prints out again the info for the given id
    # and then asks the user if the applications 
    # is valid , missing something or is being rejected
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
        df = pd.DataFrame(results[0], names)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df)
        sql = f"""SELECT * FROM EGGRAFA WHERE ID_AITHSHS = {id}"""
        results = cursor.execute(sql).fetchall()
        for res in results:
            print(res[1])
        print("Choose the result of the review.")
        katastash = iu.input_method(
            "Press 1 for OLOKLHROTHHKE\
        \nPress 2 for ELLEIPHS\
        \nPress 3 for APORRIFTHHKE\
        \nPress -1 to exit\n",
            "Not a valid input.",
            {"1": "OLOKLHROTHHKE",
             "2": "ELLEIPHS", "3": "APORRIFTHHKE", "-1": -1})
        if katastash == -1:
            return
        sql = f"""UPDATE KANEI_AITHSH
        SET KATASTASH = '{katastash}'
        WHERE ID = {id}"""
        cursor.execute(sql)
        self.conn.commit()
    # A functions that generates the food cards
    # If the application 'KATASTASH' is 'OLOKLHROTHHKE'
    # that means a user has reviewed it and is being accepted
    def generate_karta_sithshs(self, start_date, end_date) -> None:
        sql = """SELECT ID , AM 
        FROM KANEI_AITHSH 
        WHERE KATASTASH = 'OLOKLHROTHHKE' AND EIDOS_AITHSHS = 'SITHSHS'"""
        cursor = self.conn.cursor()
        results = cursor.execute(sql).fetchall()
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
    # The following fucntions calculates, 
    # given the total number of student for each loc and each category,
    # how many rooms go to each category per location
    def calculate_rooms(self):
        cursor = self.conn.cursor()
        # the options dictionary contains 
        # the rates for each category of student
        # Meaning that in the following example 40% of rooms go to FIRST_YEAR STUDENTS
        options = {
            "FIRST_YEAR": 0.40,
            "OLDER_YEAR": 0.30,
            "POSTGRADUATE": 0.10,
            "HOMOGENOUS": 0.10,
            "FOREIGN": 0.10,
        }
        sql = """SELECT TOPOTHESIA_TMHMATOS , KATHGORIA,COUNT(KATHGORIA)
        FROM AITHSH_STEGASHS
        GROUP BY TOPOTHESIA_TMHMATOS , KATHGORIA"""
        results = cursor.execute(sql).fetchall()
        tmhma_kathgoria_foithtes = {result[0]: {} for result in results}
        for i in results:
            tmhma_kathgoria_foithtes[i[0]][i[1]] = i[2]
        sql = """SELECT TOPOTHESIA_TMHMATOS ,COUNT(KATHGORIA)
        FROM AITHSH_STEGASHS
        GROUP BY TOPOTHESIA_TMHMATOS """
        results = cursor.execute(sql).fetchall()
        tmhma_foithtes = {result[0]: result[1] for result in results}
        sql = """SELECT TOPOTHESIA , COUNT(TOPOTHESIA) AS TOTAL_ROOMS
        FROM ESTIA
        GROUP BY TOPOTHESIA;"""
        results = cursor.execute(sql).fetchall()
        total_rooms = {result[0]: result[1] for result in results}
        supposed_rooms = {key: {} for key in tmhma_kathgoria_foithtes.keys()}
        actual_rooms = {key: {} for key in tmhma_kathgoria_foithtes.keys()}
        remaining_students = {key: {}
                              for key in tmhma_kathgoria_foithtes.keys()}
        for i in tmhma_kathgoria_foithtes.keys():
            for j in tmhma_kathgoria_foithtes[i].keys():
                supposed_rooms[i][j] = total_rooms[i] * options[j]
                if math.floor(supposed_rooms[i][j]) <= tmhma_kathgoria_foithtes[i][j]:
                    actual_rooms[i][j] = math.floor(supposed_rooms[i][j])
                    remaining_students[i][j] = tmhma_kathgoria_foithtes[i][j] - \
                        actual_rooms[i][j]
        for key in tmhma_foithtes.keys():
            # if the total applicants for a given location 
            # are less than the total rooms provided to their location
            # then all students get a room
            if tmhma_foithtes[key] <= total_rooms[key]:
                actual_rooms[key] = tmhma_kathgoria_foithtes[key]
                # print(key)
                continue
            # In case one category has less students than rooms
            # then that room goes to the next category
            curr_rooms = sum(actual_rooms[key].values())
            while True:
                if curr_rooms == total_rooms[key]:
                    break
                for cat in remaining_students[key].keys():
                    if curr_rooms == total_rooms[key]:
                        break
                    if remaining_students[key][cat] > 0:
                        actual_rooms[key][cat] += 1
                        remaining_students[key][cat] += -1
                        curr_rooms += 1
        return actual_rooms
    # The following function changes all the necessary attributes so
    # and gives the appropriate room to each student
    def give_rooms(self, start_date, end_date):
        actual_rooms = self.calculate_rooms()
        cursor = self.conn.cursor()
        for topothesia in actual_rooms:
            for kathgoria in actual_rooms[topothesia]:
                sql = """UPDATE KANEI_AITHSH
                    SET KATASTASH = 'EPITYXHS'
                    WHERE ID IN 
                    (SELECT ID  
                    FROM (
                    SELECT ID ,(SYNOLIKO_EISODHMA_PATROS + SYNOLIKO_EISODHMA_MHTROS + SYNOLIKO_EISODHMA_IDIOU) AS SYNOLIKO
                    FROM AITHSH_STEGASHS
                    WHERE KATHGORIA = ? 
                    AND
                    TOPOTHESIA_TMHMATOS = ?
                    ORDER BY SYNOLIKO
                    LIMIT ?
                    ))"""
                cursor.execute(
                    sql, (kathgoria, topothesia, actual_rooms[topothesia][kathgoria]))
                sql = """SELECT ID  
                            FROM (
                            SELECT ID ,(SYNOLIKO_EISODHMA_PATROS + SYNOLIKO_EISODHMA_MHTROS + SYNOLIKO_EISODHMA_IDIOU) AS SYNOLIKO
                            FROM AITHSH_STEGASHS
                            WHERE KATHGORIA = ? 
                            AND
                            TOPOTHESIA_TMHMATOS = ?
                            ORDER BY SYNOLIKO
                            LIMIT ?)"""
                ids = cursor.execute(
                    sql, (kathgoria, topothesia, actual_rooms[topothesia][kathgoria])).fetchall()
                for id in ids:
                    sql = """SELECT ID_DOMATIOU
                            FROM ESTIA
                            WHERE TOPOTHESIA = ?
                            AND 
                            ID_DOMATIOU NOT IN
                            (
                            SELECT ID_DOMATIOU
                            FROM DIAMENEI
                            )
                            LIMIT 1"""

                    room = cursor.execute(sql, (topothesia,)).fetchall()
                    if len(room) == 0:
                        return -1
                    am = cursor.execute(
                        "SELECT AM FROM AITHSH_STEGASHS WHERE ID =?", (id[0],)).fetchall()[0][0]
                    sql = """INSERT INTO DIAMENEI
                    VALUES(?,?,?,?)"""
                    cursor.execute(sql, (am, room[0][0], start_date, end_date))
        sql = """UPDATE KANEI_AITHSH
        SET KATASTASH = 'APORRIFTHHKE'
        WHERE EIDOS_AITHSHS = 'ESTIAS' AND KATASTASH != 'EPITYXHS'"""
        cursor.execute(sql)
        self.conn.commit()


