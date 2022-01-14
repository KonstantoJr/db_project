import sqlite_student as sq
import datetime
import input_utils as iu


class Menu:
    def __init__(self, db_path) -> None:
        self.db = sq.DB_Connection(db_path)
        self.am = self.login()
        while True:
            self.option = self.basic_menu()
            if self.option == "1":
                self.coupons()
            elif self.option == "2":
                self.db.purchase_history(self.am)
            elif self.option == "3":
                self.food_application()
            elif self.option == "4":
                self.housing_application()
            elif self.option == "-1":
                return

    def login(self) -> None:
        am, _ = iu.input_number("Give your AM: ", "Not a number")
        if len(self.db.retrieval_query(f"SELECT * FROM FOITHTHS WHERE AM = {am}")) == 0:
            name = input("Write your full name: ")
            phone, _ = iu.input_number(
                "Write your cellphone: ", "Not a number")
            self.db.insert_student(name, am, phone)
        return am

    def basic_menu(self) -> None:
        print(
            f"\nPress 1 to buy food coupons\
        \nPress 2 to print out your purchase history\
        \nPress 3 to make application for food\
        \nPress 4 to make application for housing\
        \nPress -1 to exit."
        )
        return input()

    def coupons(self) -> None:
        price = 2
        quantity, _ = iu.input_number(
            "Enter the quantity of coupons: ", "Not a number")
        quantity = int(quantity)
        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%y %H:%M:%S")
        self.db.insert_purchase(quantity, self.am, date,
                                total=price * quantity)
        print(f"Amount to pay = {price * quantity}")

    def food_application_form(self, new: bool, id=None) -> None:
        eidos_app = "SITHSHS"
        date = datetime.datetime.now()
        date = date.strftime("%x")
        if new == True:
            print("No food application found")
            print("Would you like to make one?")
            if input("Yes/no (Default:Yes): ") == "no":
                return
            id = len(self.db.retrieval_query(
                """SELECT * FROM KANEI_AITHSH""")) + 1
        else:
            print("Previous submission:")
            id = int(id)
            results = self.db.retrieval_query(
                f"""SELECT * FROM AITHSH_SITHSHS WHERE ID = {id}"""
            )
            print(results[0][1:])
        #
        print("Fill out the following information\nPress -1 to go back a step.")

        I = iu.food_application_form_input()
        #
        if new and I != None:
            self.db.insert_appl(self.am, date, "SE ANAMONH", eidos_app)
            self.db.insert_food_appl(
                id,
                self.am,
                I["ak_etos_eggrafhs"],
                I["dnsh_katoikias"],
                I["dnsh_monimhs"],
                I["barcode"],
                I["total_patros"],
                I["total_mhtros"],
                I["ar_melon_oikegias"],
            )
            self.add_files(id)
        elif not new and I != None:
            self.db.update_food_appl(
                id,
                I["ak_etos_eggrafhs"],
                I["dnsh_katoikias"],
                I["dnsh_monimhs"],
                I["barcode"],
                I["total_patros"],
                I["total_mhtros"],
                I["ar_melon_oikegias"],
            )
            #
            print("Previous files:")
            results = self.db.retrieval_query(
                f"""SELECT ONOMA FROM EGGRAFA WHERE ID_AITHSHS = {id}"""
            )
            print(results)
            #
            self.db.del_files(id)
            self.add_files(id)

    def food_application(self) -> None:
        eidos_app = "SITHSHS"
        query = f"""SELECT * FROM KANEI_AITHSH WHERE AM = {self.am} AND EIDOS_AITHSHS = '{eidos_app}'"""
        results = self.db.retrieval_query(query)
        if len(results) == 0:
            self.food_application_form(True)
        else:
            if results[0][3] == "OLOKLHROTHHKE" or results[0][3] == "SE ANAMONH":
                print(
                    "There is already a food application\nTher status of the application is: SE ANAMONH"
                )
            elif results[0][3] == "APORRIFTHKE":
                print("Your application has not been accepted")
            elif results[0][3] == "EPITYXHS":
                print("Your application has been accepted")
                sql = f"""SELECT ID_CARD
                FROM LAMVANEI
                WHERE AM = {self.am}"""
                id_card = self.db.retrieval_query(sql)
                print(f"Your card id is {id_card[0][0]}")
            elif results[0][3] == "ELLEIPHS":
                print("Your application is missing something")
                print(
                    "Please re-enter your information and make sure nothing is missing"
                )
                self.food_application_form(False, results[0][0])

    def housing_application_form(self, new: bool, id=None):
        eidos_app = "ESTIAS"
        date = datetime.datetime.now()
        date = date.strftime("%x")
        if new == True:
            print("No housing application found")
            print("Would you like to make one?")
            if input("Yes/no (Default:Yes): ") == "no":
                return
            id = len(self.db.retrieval_query(
                """SELECT * FROM KANEI_AITHSH""")) + 1
        else:
            print("Previous submission:")
            id = int(id)
            results = self.db.retrieval_query(
                f"""SELECT * FROM AITHSH_STEGASHS WHERE ID = {id}"""
            )
            print(results[0][1:])
        #
        I = iu.housing_appl_form_input()
        if new and I != None:
            self.db.insert_appl(self.am, date, "SE ANAMONH", eidos_app)
            self.db.insert_housing_appl(
                id,
                self.am,
                I["kathgoria"],
                I["dnsh_monimhs"],
                I["thl_goneon"],
                I["epaggelma_patros"],
                I["epaggelma_mhtros"],
                I["topothesia_tmhmatos"],
                I["total_patros"],
                I["total_mhtros"],
                I["total_idiou"],
                I["ar_melon"],
                I["adelfia_pou_spoudazoun"],
                I["goneis_me_eidikes_anagkes"],
                I["diazeugmenoi_goneis"],
                I["orfanos_apo_enan_gonea"],
                I["poluteknh_oikogenia"],
                I["stratiotikh_thhteia_aderfou"],
                I["melh_oikogenias_me_eidikes_anagkes"],
            )
            self.add_files(id)
        elif not new and I != None:
            self.db.update_housing_appl(
                id,
                I["kathgoria"],
                I["dnsh_monimhs"],
                I["thl_goneon"],
                I["epaggelma_patros"],
                I["epaggelma_mhtros"],
                I["topothesia_tmhmatos"],
                I["total_patros"],
                I["total_mhtros"],
                I["total_idiou"],
                I["ar_melon"],
                I["adelfia_pou_spoudazoun"],
                I["goneis_me_eidikes_anagkes"],
                I["diazeugmenoi_goneis"],
                I["orfanos_apo_enan_gonea"],
                I["poluteknh_oikogenia"],
                I["stratiotikh_thhteia_aderfou"],
                I["melh_oikogenias_me_eidikes_anagkes"],)
            print("Previous files:")
            results = self.db.retrieval_query(
                f"""SELECT ONOMA FROM EGGRAFA WHERE ID_AITHSHS = {id}"""
            )
            print(results[0])
            #
            self.db.del_files(id)
            self.add_files(id)

    def housing_application(self) -> None:
        eidos_app = "ESTIAS"
        query = f"""SELECT * FROM KANEI_AITHSH WHERE AM = {self.am} AND EIDOS_AITHSHS = '{eidos_app}'"""
        results = self.db.retrieval_query(query)
        if len(results) == 0:
            self.housing_application_form(True)
        else:
            if results[0][3] == "OLOKLHROTHHKE" or results[0][3] == "SE ANAMONH":
                print(
                    "There is already a housing application\nThe status of the application is: SE ANAMONH"
                )
            elif results[0][3] == "APORRIFTHKE":
                print("Your application has not been accepted")
            elif results[0][3] == "EPITYXHS":
                print("Your application has been accepted")
                # Code here
            elif results[0][3] == "ELLEIPHS":
                print("Your application is missing something")
                print(
                    "Please re-enter your information and make sure nothing is missing"
                )
                self.housing_application_form(False, results[0][0])

    def add_files(self, id):
        file = input(
            "Enter the path of the file you want to submit.\nPress enter to stop submitting.\n"
        )
        while file != "":
            self.db.add_file(id, file.strip())
            while True:
                file = input()
                eggrafa = self.db.retrieval_query(
                    f"SELECT ONOMA FROM EGGRAFA WHERE ID_AITHSHS = {id}"
                )
                for onoma in eggrafa:
                    if file.strip() == onoma[0]:
                        print(onoma[0])
                        print("Already submitted file.")
                        break
                else:
                    break


if __name__ == "__main__":
    menu = Menu("Data_Creation/merimna.db")
