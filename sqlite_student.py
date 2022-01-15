import sqlite3
import pandas as pd


class DB_Connection:
    def __init__(self, path_name) -> None:
        self.connection = sqlite3.connect(path_name)
    #Inserts a new student into the database
    def insert_student(self, name, am, phone) -> None:
        cursor = self.connection.cursor()
        sql = """INSERT INTO FOITHTHS(AM , ONOMA , THLEFONO)
        VALUES(?,?,?)"""
        cursor.execute(sql, (am, name, phone))
        self.connection.commit()
    # Inserts a new purchase into the db
    def insert_purchase(self, quantity, am, date, total):
        cursor = self.connection.cursor()
        id = len(self.retrieval_query("""SELECT * FROM AGORA_KOUPONION""")) + 1
        sql = """INSERT INTO AGORA_KOUPONION
        VALUES(?,?,?,?,?)"""
        cursor.execute(sql, (id, am, date, quantity, total))
        self.connection.commit()
    # Gets an sql query and returns the contents
    def retrieval_query(self, sql: str) -> list:
        cursor = self.connection.cursor()
        results = cursor.execute(sql).fetchall()
        return results
    # Insert a new application
    def insert_appl(self, am, hm, katastash, eidos_aithshs):
        cursor = self.connection.cursor()
        id = len(self.retrieval_query("""SELECT * FROM KANEI_AITHSH""")) + 1
        sql = """INSERT INTO KANEI_AITHSH(ID , AM , HM , KATASTASH , EIDOS_AITHSHS)
        VALUES(?,?,?,?,?)"""
        cursor.execute(sql, (id, am, hm, katastash, eidos_aithshs))
        self.connection.commit()
    # deletes all the files inside the EGGRAFA table for a given id
    # this is used only when one application needs to be re send
    # because an admin marked as 'ELLEIPHS'
    def del_files(self, id):
        sql = f"""DELETE FROM EGGRAFA
        WHERE ID_AITHSHS = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
    # gets all the necessary infor in order to update 
    # an existing food application
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
    # Gets the necessary info to insert a new food
    # application
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
    # Gets the necessary information to update
    # an existing housing application
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
    # Gets the necessary application in order to insert
    # a new housing application
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
    # Inserts the path of the file into the database
    def add_file(self, id, name):
        cursor = self.connection.cursor()
        sql = """INSERT INTO EGGRAFA 
        VALUES(?,?)"""
        cursor.execute(sql, (id, name))
        self.connection.commit()
    # Returns the purchase history of a given user
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
    # if the student's application for housing has been accepted 
    # then the room he was given will be returned with the following 
    # query
    def print_room(self, am):
        cursor = self.connection.cursor()
        sql = """SELECT ID_DOMATIOU
        FROM DIAMENEI
        WHERE AM = ?"""
        id = cursor.execute(sql, (am,)).fetchall()[0][0]
        sql = """SELECT TOPOTHESIA , ONOMA , OROFOS , ARITHMOS
        FROM ESTIA NATURAL JOIN DOMATIA
        WHERE ID_DOMATIOU = ?"""
        onoma = cursor.execute(sql, (id,)).fetchall()
        names = [description[0] for description in cursor.description]
        df = pd.DataFrame(onoma, columns=names)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None, 'display.max_colwidth', -1):
            print(df.to_string(index=False))



