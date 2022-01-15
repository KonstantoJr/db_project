import sqlite3
import pandas as pd
import random

# A function to generate data to fill the table AITHSH_STEGASHS
def generate(excel_path, db_path):
    epaggelma_patros = [
        "ΚΑΘΗΓΗΤΗΣ",
        "ΕΠΙΕΙΡΗΜΑΤΙΑΣ",
        "ΥΠΑΛΛΗΛΟΣ",
        "ΤΡΑΓΟΥΔΙΣΤΗΣ",
        "ΑΓΡΟΤΗΣ",
        "ΑΝΕΡΓΟΣ",
        "ΓΥΜΝΑΣΤΗΣ",
    ]
    epaggelma_mhtros = [
        "ΚΑΘΗΓΗΤΡΙΑ",
        "ΕΠΙΕΙΡΗΜΑΤΙΑΣ",
        "ΥΠΑΛΛΗΛΟΣ",
        "ΤΡΑΓΟΥΔΙΣΤΡΙΑ",
        "ΑΓΡΟΤΙΣΣΑ",
        "ΑΝΕΡΓΗ",
        "ΓΥΜΝΑΣΤΡΙΑ",
    ]
    topothesia_tmimatos = ["ΑΓΡΙΝΙΟ", "ΚΟΥΚΟΥΛΙ", "ΡΙΟ"]
    category = ["FIRST_YEAR", "OLDER_YEAR",
                "POSTGRADUATE", "HOMOGENOUS", "FOREIGN"]
    df = pd.read_excel(excel_path)
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        # Query to get the AM ,ID already inside the db
        cursor.execute(
            "SELECT DISTINCT AM,ID FROM KANEI_AITHSH WHERE EIDOS_AITHSHS='ESTIAS'"
        )
        AM = cursor.fetchall()

        for i in range(len(AM)):
            random.seed(AM[i][0])
            test5 = random.randint(1, 100)
            if test5 <= 65:
                katigoria = category[0]
            elif test5 > 65 and test5 <= 85:
                katigoria = category[1]
            elif test5 > 85 and test5 <= 90:
                katigoria = category[2]
            elif test5 > 90 and test5 <= 96:
                katigoria = category[3]
            elif test5 > 96:
                katigoria = category[4]
            else:
                katigoria = category[0]
            thl_gonea = random.randint(6930000000, 6999999999)
            ep_patros = epaggelma_patros[random.randint(0, 5)]
            ep_mhtros = epaggelma_mhtros[random.randint(0, 5)]
            test0 = random.randint(0, 20)
            if test0 < 10:
                top = 2
            elif test0 > 16:
                top = 1
            else:
                top = 0
            top_tmimatos = topothesia_tmimatos[top]
            eis_patros = random.randint(4000, 40000)
            eis_mitros = random.randint(4000, 40000)
            eis_idiou = random.randint(4000, 40000)
            test = random.randint(1, 101)
            if test < 15:
                goneis_anagkes = 1  # ellhnika to nai
            else:
                goneis_anagkes = 0
            test1 = random.randint(1, 1001)
            if test1 > 700:
                diazigio = 1
            else:
                diazigio = 0
            test2 = random.randint(1, 1002)
            if test2 < 800:
                orfanos = 0
            else:
                orfanos = 1

            meli_oik = random.randint(3, 8)
            if meli_oik > 6:
                politekneia = 1
            else:
                politekneia = 0
            test3 = random.randint(1, 20)
            if test3 > 10:
                stratos = 1
            else:
                stratos = 0
            test4 = random.randint(1, 11)
            if test4 < 3:
                meli_anagkes = test4
            else:
                meli_anagkes = 0

            adelfia_spoudazoun = random.randint(0, (meli_oik - 3))
            # A query to insert the random generated data
            cursor.execute(
                """INSERT INTO AITHSH_STEGASHS
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); """,
                (AM[i][1], AM[i][0], katigoria, df.iat[i, 1],
                    thl_gonea, ep_patros, ep_mhtros,
                 top_tmimatos, eis_patros, eis_mitros, eis_idiou,
                    meli_oik, adelfia_spoudazoun, goneis_anagkes,
                 diazigio, orfanos, politekneia, stratos, meli_anagkes)
            )

        ##cursror.execute(sql, (m1, m2,m3))

        connection.commit()
