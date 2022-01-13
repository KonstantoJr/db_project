import sqlite_student as sq
import datetime


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

    @staticmethod
    def input_number(text, error):
        while True:
            inp = input(text)
            if inp.isdigit():
                return inp, 1
            elif inp == "-1":
                return None, -1
            print(error)

    @staticmethod
    def input_method(text: str, error: str, options: dict):
        while True:
            inp = input(text)
            if inp in options.keys():
                return options[inp]
            print(error)

    @staticmethod
    def food_application_form_input() -> None | list:
        order = 0
        ak_etos_eggrafhs = None
        dnsh_katoikias = None
        dnsh_monimhs = None
        barcode = None
        total_patros = None
        total_mhtros = None
        ar_melon_oikegias = None
        while True:
            if order == 0:
                ak_etos_eggrafhs, step = Menu.input_number(
                    "Academic year of entry: ", "Not a valid year"
                )
                if step == -1:
                    return [None] * 7
                order += step
            elif order == 1:
                dnsh_katoikias = input("Address of residence: ")
                if dnsh_katoikias == "-1":
                    order += -1
                else:
                    order += 1
            elif order == 2:
                dnsh_monimhs = input("Address of main residence: ")
                if dnsh_monimhs == "-1":
                    order += -1
                else:
                    order += 1
            elif order == 3:
                barcode, step = Menu.input_number(
                    "Barcode of academic id: ", "Not a number"
                )
                order += step
            elif order == 4:
                total_patros, step = Menu.input_number(
                    "Total income of father: ", "Not a number"
                )
                order += step
            elif order == 5:
                total_mhtros, step = Menu.input_number(
                    "Total income of mother: ", "Not a number"
                )
                order += step
            elif order == 6:

                ar_melon_oikegias, step = Menu.input_number(
                    "Number of people in family: ", "Not a number"
                )
                order += step
            elif order >= 7:
                return [
                    ak_etos_eggrafhs,
                    dnsh_katoikias,
                    dnsh_monimhs,
                    barcode,
                    total_patros,
                    total_mhtros,
                    ar_melon_oikegias,
                ]

    def login(self) -> None:
        am, _ = Menu.input_number("Give your AM: ", "Not a number")
        if len(self.db.retrieval_query(f"SELECT * FROM FOITHTHS WHERE AM = {am}")) == 0:
            name = input("Write your full name: ")
            phone, _ = Menu.input_number("Write your cellphone: ", "Not a number")
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
        quantity = Menu.input_number("Enter the quantity of coupons: ", "Not a number")
        quantity = int(quantity)
        date = datetime.datetime.now()
        date = date.strftime("%x")
        self.db.insert_purchase(quantity, self.am, date, total=price * quantity)
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
            id = len(self.db.retrieval_query("""SELECT * FROM KANEI_AITHSH""")) + 1
        else:
            print("Previous submission:")
            id = int(id)
            results = self.db.retrieval_query(
                f"""SELECT * FROM AITHSH_SITHSHS WHERE ID = {id}"""
            )
            print(results[0][1:])
        #
        print("Fill out the following information\nPress -1 to go back a step.")

        (
            ak_etos_eggrafhs,
            dnsh_katoikias,
            dnsh_monimhs,
            barcode,
            total_patros,
            total_mhtros,
            ar_melon_oikegias,
        ) = Menu.food_application_form_input()
        #
        if new and ak_etos_eggrafhs != None:
            self.db.insert_appl(self.am, date, "SE ANAMONH", eidos_app)
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
        elif not new and ak_etos_eggrafhs != None:
            self.db.update_food_appl(
                id,
                ak_etos_eggrafhs,
                dnsh_katoikias,
                dnsh_monimhs,
                barcode,
                total_patros,
                total_mhtros,
                ar_melon_oikegias,
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

    def housing_application(self) -> None:
        eidos_app = "ESTIAS"
        query = f"""SELECT * FROM KANEI_AITHSH WHERE AM = {self.am} AND EIDOS_AITHSHS = '{eidos_app}'"""
        results = self.db.retrieval_query(query)
        if len(results) == 0:
            date = datetime.datetime.now()
            date = date.strftime("%x")
            print("No food application found")
            print("Would you like to make one?")
            if input("Yes/no (Default:Yes): ") == "no":
                return
            id = self.db.insert_appl(self.am, date, "SE ANAMONH", eidos_app)
            print("Fill out the following information")
            kathgoria = Menu.input_method(
                "Student Category:\n\
                Press 1 for first year student\n\
                Press 2 for older year student\n\
                Press 3 for postgraduate student\n\
                Press 4 for homogenous student\n\
                Press 5 for foreign student\n",
                "Not an option",
                options={
                    "1": "FIRST_YEAR",
                    "2": "OLDER_YEAR",
                    "3": "POSTGRADUATE",
                    "4": "HOMOGENOUS",
                    "5": "FOREIGN",
                },
            )
            dnsh_monimhs = input("Address of main residence: ")
            thl_goneon = Menu.input_number("Phone number of parent: ", "Not a number")
            epaggelma_patros = input("Fathers occupation: ")
            epaggelma_mhtros = input("Mothers occupation: ")
            topothesia_tmhmatos = Menu.input_method(
                "Department Location\n\
                Press 1 for Πανεπιστημιούπολη Ρίο\n\
                Press 2 for Κουκούλι Πατρών\n\
                Press 3 for Αγρίνιο\n",
                "Not an option",
                options={
                    "1": "Πανεπιστημιούπολη Ρίο",
                    "2": "Κουκούλι Πατρών",
                    "3": "Αγρίνιο",
                },
            )
            total_patros = Menu.input_number("Total income of father: ", "Not a number")
            total_mhtros = Menu.input_number("Total income of mother: ", "Not a number")
            total_idiou = Menu.input_number("Total personal income : ", "Not a number")
            ar_melon = Menu.input_number("Number of people in family: ", "Not a number")
            adelfia_pou_spoudazoun = Menu.input_number(
                "Brothers and Sisters studying: ", "Not a number"
            )
            goneis_me_eidikes_anagkes = Menu.input_method(
                "Parents with special needs\n\
            Press 1 for YES\n\
            Press 2 for NO\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ"},
            )
            diazeugmenoi_goneis = Menu.input_method(
                "Divorced Parents\n\
            Press 1 for YES\n\
            Press 2 for NO\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ"},
            )
            orfanos_apo_enan_gonea = Menu.input_method(
                "Orphan by one parent\n\
            Press 1 for YES\n\
            Press 2 for NO\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ"},
            )
            poluteknh_oikogenia = Menu.input_method(
                "Many children family\n\
            Press 1 for YES\n\
            Press 2 for NO\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ"},
            )
            stratiotikh_thhteia_aderfou = Menu.input_method(
                "Brother in military service\n\
            Press 1 for YES\n\
            Press 2 for NO\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ"},
            )
            melh_oikogenias_me_eidikes_anagkes = Menu.input_number(
                "Number of people in your family with special needs: ", "Not a number"
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
