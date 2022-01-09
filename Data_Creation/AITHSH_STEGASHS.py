import sqlite3
import pandas as pd
import random


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
    topothesia_tmimatos = ["ΑΓΡΙΝΙΟ", "ΑΜΑΛΙΑΔΑ", "ΚΟΥΚΑΚΙ", "ΠΑΤΡΑ"]

    df = pd.read_excel(excel_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT DISTINCT AM,ID FROM KANEI_AITHSH WHERE EIDOS_AITHSHS='ESTIAS'"
    )
    AM = cursor.fetchall()

    for i in range(len(AM)):
        random.seed(AM[i][0])
        katigoria = random.randint(1, 5)
        thl_gonea = random.randint(6930000000, 6999999999)
        ep_patros = epaggelma_patros[random.randint(0, 5)]
        ep_mhtros = epaggelma_mhtros[random.randint(0, 5)]
        top_tmimatos = topothesia_tmimatos[random.randint(0, 3)]
        eis_patros = random.randint(4000, 40000)
        eis_mitros = random.randint(4000, 40000)
        eis_idiou = random.randint(4000, 40000)
        test = random.randint(1, 101)
        if test < 15:
            goneis_anagkes = "ΝΑΙ"  # ellhnika to nai
        else:
            goneis_anagkes = "ΟΧΙ"
        test1 = random.randint(1, 1001)
        if test1 > 700:
            diazigio = "ΝΑΙ"
        else:
            diazigio = "ΟΧΙ"
        test2 = random.randint(1, 1002)
        if test2 < 800:
            orfanos = "ΟΧΙ"
        else:
            orfanos = "ΝΑΙ"

        meli_oik = random.randint(3, 8)
        if meli_oik > 6:
            politekneia = "ΝΑΙ"
        else:
            politekneia = "ΟΧΙ"
        test3 = random.randint(1, 20)
        if test3 > 10:
            stratos = "ΝΑΙ"
        else:
            stratos = "ΟΧΙ"
        test4 = random.randint(1, 200)
        if test4 < 30:
            meli_anagkes = "ΝΑΙ"
        else:
            meli_anagkes = "ΟΧΙ"

        adelfia_spoudazoun = random.randint(0, (meli_oik - 3))

        cursor.execute(
            f"""INSERT INTO AITHSH_STEGASHS
        VALUES ({AM[i][1]},{AM[i][0]},{katigoria},'{df.iat[i,1]}',{thl_gonea}, '{ep_patros}', '{ep_mhtros}',
        '{top_tmimatos}', {eis_patros}, {eis_mitros}, {eis_idiou}, {meli_oik}, {adelfia_spoudazoun}, '{goneis_anagkes}',
        '{diazigio}', '{orfanos}', '{politekneia}', '{stratos}', '{meli_anagkes}'  ); """
        )

    ##cursror.execute(sql, (m1, m2,m3))

    connection.commit()
