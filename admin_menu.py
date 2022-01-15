import sqlite_admin
import input_utils as iu
from datetime import datetime


class Admin:
    def __init__(self) -> None:
        self.db = sqlite_admin.DB_Connection("Data_Creation/merimna.db")
        while True:
            self.option = self.login()
            if self.option == 1:
                self.applications("SITHSHS")
            elif self.option == 2:
                self.applications("ESTIAS")
            elif self.option == 3:
                self.generate_cards()
            elif self.option == 4:
                self.assign_rooms()
            elif self.option == -1:
                return

    def login(self):
        login = iu.input_method(
            "Press 1 to check food applications\
            \nPress 2 to check housing applications\
            \nPress 3 to generate 'Food Cards'\
            \nPress 4 to assign rooms.\
            \nPress -1 to exit.\n", "Not a valid option.",
            {"1": 1, "2": 2, "3": 3, "4": 4, "-1": -1})
        return login

    def applications(self, eidos):
        while True:
            if eidos == "SITHSHS":
                ids = self.db.print_application(eidos)

            elif eidos == "ESTIAS":
                ids = self.db.print_application(eidos)
            if ids == None:
                break
            ids = set(ids)
            while True:
                print(ids)
                id, _ = iu.input_number(
                    "Press -1 to exit.\nEnter the id of the application you want to review: ", "Not a number.")
                if id == None:
                    return
                if int(id) in ids:
                    break

            print()
            self.db.select_appl_to_review(id, eidos)
            option = input(
                "If you want to continue press enter.\nElse press -1.\n")
            if option == "-1":
                break

    def generate_cards(self):
        year = datetime.now().strftime("%Y")
        start_date = "1-09-" + year
        end_date = "31-08-" + str(int(year) + 1)
        self.db.generate_karta_sithshs(start_date, end_date)
        print("Cards have been generated successfully")

    def assign_rooms(self):
        year = datetime.now().strftime("%Y")
        start_date = "1-09-" + year
        end_date = "31-08-" + str(int(year) + 1)
        if self.db.give_rooms(start_date, end_date) == -1:
            print("Rooms have already be assigned")
        else:
            print("Rooms have been assigned successfully\n")


if __name__ == "__main__":
    menu = Admin()
