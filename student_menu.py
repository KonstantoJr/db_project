import sqlite_conection as sq
import datetime


class Menu:
    def __init__(self, db_path) -> None:
        self.db = sq.DB_Connection(db_path)
        self.am = self.login()
        self.option = self.basic_menu()
        if self.option == "1":
            # some code here
            self.coupons()
        elif self.option == "2":
            # some code here
            self.food_application()
            return
        elif self.option == "3":
            # some code here
            self.housing_application()
            return
        else:
            return

    def login(self) -> None:
        while True:
            print("Give your AM")
            am = input()
            if am.isdigit():
                break
            else:
                print("Not a nnumber")
        if len(self.db.retrieval_query(f"SELECT * FROM FOITHTHS WHERE AM = {am}")) == 0:
            name = input("Write your full name: ")
            phone = input("Write your cellphone: ")
            self.db.insert_student(name, am, phone)
        return am

    def basic_menu(self) -> None:
        print(
            f"Press 1 to buy food coupons\
        \nPress 2 to make application for food\
        \nPress 3 to make application for housing"
        )
        return input()

    def coupons(self) -> None:
        price = 2
        while True:
            quantity = input("Enter the quantity of coupons ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Not a number")
        date = datetime.datetime.now()
        date = date.strftime("%x")
        self.db.insert_purchase(quantity, self.am, date, total=price * quantity)
        print(f"Amount to pay = {price * quantity}")

    def food_application(self) -> None:
        eidos_app = "Food"
        query = f"""SELECT * FROM KANEI_AITHSH WHERE AM = {self.am} AND EIDOS_AITHSHS = '{eidos_app}'"""
        results = self.db.retrieval_query(query)
        if len(results) == 0:
            date = datetime.datetime.now()
            date = date.strftime("%x")
            print("No food application found")
            print("Would you like to make one?")
            if input("Yes/no (Default:Yes): ") == "no":
                return
            id = self.db.insert_appl(self.am, date, "Αναμονή", eidos_app)
            print("Fill out the following information")
            ak_etos_eggrafhs = input("Academic year of entry: ")
            dnsh_katoikias = input("Address of residence: ")
            dnsh_monimhs = input("Address of main residence: ")
            barcode = input("Barcode of academic id: ")
            total_patros = input("Total income of father: ")
            total_mhtros = input("Total income of mother: ")
            ar_melon_oikegias = input("Number of people in family: ")
            self.db.insert_food_appl(
                id,
                self.am,
                ak_etos_eggrafhs,
                dnsh_katoikias,
                dnsh_monimhs,
                barcode,
                total_patros,
                total_mhtros,
                ar_melon_oikegias,
            )
            self.add_files(id)
        else:
            print(
                f"There is already a food application\nThe status of the application is: {results[0][3]}"
            )

    def housing_application(self) -> None:
        eidos_app = "Housing"
        query = f"""SELECT * FROM KANEI_AITHSH WHERE AM = {self.am} AND EIDOS_AITHSHS = '{eidos_app}'"""
        results = self.db.retrieval_query(query)
        if len(results) == 0:
            date = datetime.datetime.now()
            date = date.strftime("%x")
            print("No food application found")
            print("Would you like to make one?")
            if input("Yes/no (Default:Yes): ") == "no":
                return
            id = self.db.insert_appl(self.am, date, "Αναμονή", eidos_app)
            print("Fill out the following information")
            kathgoria = input("Category of student: ")
            dnsh_monimhs = input("Address of main residence: ")
            thl_goneon = input("Phone number of parent:  ")
            epaggelma_patros = input("Fathers occupation: ")
            epaggelma_mhtros = input("Mothers occupation: ")
            topothesia_tmhmatos = input("Department Location: ")
            total_patros = input("Total income of father: ")
            total_mhtros = input("Total income of mother: ")
            total_idiou = input("Total personal income: ")
            ar_melon = input("Number of people in family: ")
            adelfia_pou_spoudazoun = input("Brothers and Sisters Studying: ")
            goneis_me_eidikes_anagkes = input("Parents with special needs: ")
            diazeugmenoi_goneis = input("Divorced Parents: ")
            orfanos_apo_enan_gonea = input("Orphan by one parent: ")
            poluteknh_oikogenia = input("Many Children Family: ")
            stratiotikh_thhteia_aderfou = input("Brother in service: ")
            melh_oikogenias_me_eidikes_anagkes = input(
                "Number of people in your family with special needs: "
            )
            self.db.insert_housing_appl(
                id,
                self.am,
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
            self.add_files(id)
        else:
            print(
                f"There is already a housing application\nThe status of the application is: {results[0][3]}"
            )

    def add_files(self, id):
        file = input(
            "Enter the path of the file you want to submit.\n Press enter to stop submitting.\n"
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
