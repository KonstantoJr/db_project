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
        id = len(self.retrieval_query("""SELECT * FROM AGORA_KOUPONION""")) + 1
        sql = """INSERT INTO AGORA_KOUPONION
        VALUES(?,?,?,?,?)"""
        cursor.execute(sql, (id, am, date, quantity, total))
        self.connection.commit()

    def retrieval_query(self, sql: str) -> list:
        cursor = self.connection.cursor()
        results = cursor.execute(sql).fetchall()
        return results

    def insert_appl(self, am, hm, katastash, eidos_aithshs):
        cursor = self.connection.cursor()
        id = len(self.retrieval_query("""SELECT * FROM KANEI_AITHSH""")) + 1
        sql = """INSERT INTO KANEI_AITHSH(ID , AM , HM , KATASTASH , EIDOS_AITHSHS)
        VALUES(?,?,?,?,?)"""
        cursor.execute(sql, (id, am, hm, katastash, eidos_aithshs))
        self.connection.commit()

    def del_files(self, id):
        sql = f"""DELETE FROM EGGRAFA
        WHERE ID_AITHSHS = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def update_food_appl(
        self,
        id,
        ak_etos_eggrafhs,
        dnsh_katoikias,
        dnsh_monimhs,
        barcode,
        total_patros,
        total_mhtros,
        ar_melon_oikegias,
    ):
        id = int(id)
        sql2 = f"""UPDATE KANEI_AITHSH
        SET KATASTASH = 'SE ANAMONH'
        WHERE ID = {id}"""
        sql = f"""UPDATE AITHSH_SITHSHS
        SET 'AK_ETOS_EGGRAFHS' = ?,
        'D/NSH_KATOIKIAS' = ?,
        'D/NSH_MONIMHS_KATOIKIAS' = ?,
        'BARCODE_PASOU' = ?,
        'SYNOLIKO_EISODHMA_PATROS' = ?,
        'SYNOLIKO_EISODHMA_MHTROS' = ?,
        'AR_MELON_OIKOGENEIAS' = ?
        WHERE ID = {id};"""
        cursor = self.connection.cursor()
        cursor.execute(
            sql,
            (
                ak_etos_eggrafhs,
                dnsh_katoikias,
                dnsh_monimhs,
                barcode,
                total_patros,
                total_mhtros,
                ar_melon_oikegias,
            ),
        )
        self.connection.commit()
        cursor.execute(sql2)
        self.connection.commit()

    def insert_food_appl(
        self,
        id,
        am,
        ak_etos_eggrafhs,
        dnsh_katoikias,
        dnsh_monimhs,
        barcode,
        total_patros,
        total_mhtros,
        ar_melon_oikegias,
    ):
        cursor = self.connection.cursor()
        sql = """INSERT INTO AITHSH_SITHSHS
        VALUES(?,?,?,?,?,?,?,?,?)"""
        values = (
            id,
            am,
            ak_etos_eggrafhs,
            dnsh_katoikias,
            dnsh_monimhs,
            barcode,
            total_patros,
            total_mhtros,
            ar_melon_oikegias,
        )
        cursor.execute(sql, values)
        self.connection.commit()

    def update_housing_appl(
            self,
            id,
            kathgoria,
            dnsh_monimhs,
            thl_goneon,
            epaggelma_patros,
            epaggelma_mhtros,
            topothesia_tmhmatos,
            total_patros,
            total_mhtros,
            total_idiou,
            ar_melon,
            adelfia_pou_spoudazoun,
            goneis_me_eidikes_anagkes,
            diazeugmenoi_goneis,
            orfanos_apo_enan_gonea,
            poluteknh_oikogenia,
            stratiotikh_thhteia_aderfou,
            melh_oikogenias_me_eidikes_anagkes):
        id = int(id)
        sql2 = f"""UPDATE KANEI_AITHSH
        SET KATASTASH = 'SE ANAMONH'
        WHERE ID = {id}"""
        sql = f"""UPDATE AITHSH_STEGASHS
        SET 'KATHGORIA' = ?,
        'D/NSH_MONIMHS_KATOIKIAS' = ?,
        'THL_GONEON' = ?,
        'EPAGGELMA_PATROS' =?,
        'EPAGGELMA_MHTROS' = ?,
        'TOPOTHESIA_TMHMATOS' =?,
        'SYNOLIKO_EISODHMA_PATROS' = ?,
        'SYNOLIKO_EISODHMA_MHTROS' = ?,
        'SYNOLIKO_EISODHMA_IDIOU' = ?,
        'AR_MELON_OIKOGENEIAS' = ?,
        'ADELFIA_POU_SPOUDAZOUN' = ?,
        'GONEIS_ME_EIDIKES_ANAGKES = ?,
        'DIAZEUGMENOI_GONEIS' = ?,
        'ORFANOS_APO_ENAN_GONEA' = ?,
        'POLUTEKNH_OIKOGENEIA' = ?,
        'STRATIOTIKH_THHTEIA_ADERFOU = ?,
        'MELH_OIKOGENEIAS_ME_EIDIKES_ANAGKES' = ?
        WHERE ID = {id};"""
        cursor = self.connection.cursor()
        cursor.execute(
            sql,
            (
                kathgoria,
                dnsh_monimhs,
                thl_goneon,
                epaggelma_patros,
                epaggelma_mhtros,
                topothesia_tmhmatos,
                total_patros,
                total_mhtros,
                total_idiou,
                ar_melon,
                adelfia_pou_spoudazoun,
                goneis_me_eidikes_anagkes,
                diazeugmenoi_goneis,
                orfanos_apo_enan_gonea,
                poluteknh_oikogenia,
                stratiotikh_thhteia_aderfou,
                melh_oikogenias_me_eidikes_anagkes
            )
        )
        cursor.execute(sql2)
        self.connection.commit()

    def insert_housing_appl(
        self,
        id,
        am,
        kathgoria,
        dnsh_monimhs,
        thl_goneon,
        epaggelma_patros,
        epaggelma_mhtros,
        topothesia_tmhmatos,
        total_patros,
        total_mhtros,
        total_idiou,
        ar_melon,
        adelfia_pou_spoudazoun,
        goneis_me_eidikes_anagkes,
        diazeugmenoi_goneis,
        orfanos_apo_enan_gonea,
        poluteknh_oikogenia,
        stratiotikh_thhteia_aderfou,
        melh_oikogenias_me_eidikes_anagkes,
    ):
        cursor = self.connection.cursor()
        sql = """INSERT INTO AITHSH_STEGASHS
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        values = (
            id,
            am,
            kathgoria,
            dnsh_monimhs,
            thl_goneon,
            epaggelma_patros,
            epaggelma_mhtros,
            topothesia_tmhmatos,
            total_patros,
            total_mhtros,
            total_idiou,
            ar_melon,
            adelfia_pou_spoudazoun,
            goneis_me_eidikes_anagkes,
            diazeugmenoi_goneis,
            orfanos_apo_enan_gonea,
            poluteknh_oikogenia,
            stratiotikh_thhteia_aderfou,
            melh_oikogenias_me_eidikes_anagkes,
        )
        cursor.execute(sql, values)
        self.connection.commit()

    def add_file(self, id, name):
        cursor = self.connection.cursor()
        sql = """INSERT INTO EGGRAFA 
        VALUES(?,?)"""
        cursor.execute(sql, (id, name))
        self.connection.commit()

    def purchase_history(self, am):
        sql = f"""SELECT HM_AGORAS, POSOTHTA , TIMH
        FROM AGORA_KOUPONION
        WHERE AM = {am}
        ORDER BY HM_AGORAS DESC"""
        results = self.retrieval_query(sql)
        if len(results) == 0:
            print("You have not made a purchase yet.")
            return
        print("HM_AGORAS\t\tPOSOTHTA\tTIMH")
        for i in results:
            print(f"{i[0]}\t{i[1]}\t\t{i[2]}")

    def clear_table(self, table):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE  FROM {table}")
        self.connection.commit()


if __name__ == "__main__":
    db = DB_Connection("Data_Creation/merimna.db")
    # db.insert_student("Κώστας Κωνσταντόπουλος", 1066546, 6948647574)
    # print(db.retrieval_query("SELECT * FROM FOITHTHS WHERE AM = 1066546"))
    # db.clear_table("KANEI_AITHSH")
    # db.clear_table("AITHSH_STEGASHS")
    # db.clear_table("AITHSH_SITHSHS")
    # db.clear_table("EGGRAFA")
    # db.clear_table("LAMVANEI")
    # db.clear_table("KARTA_SITHSHS")
    # db.clear_table("AGORA_KOUPONION")
    #sql = """DROP TABLE IF EXISTS FOITHTHS"""
    #cursor = db.connection.cursor()
    # cursor.execute(sql)
    # db.connection.commit()
