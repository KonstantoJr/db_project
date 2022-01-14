import sqlite_admin
import input_utils as iu


class Admin:
    def __init__(self) -> None:
        self.db = sqlite_admin.DB_Connection("Data_Creation/merimna.db")
        while True:
            self.option = self.login()
            if self.option == 1:
                self.applications("SITHSHS")
            elif self.option == 2:
                self.applications("ESTIAS")
            elif self.option == -1:
                return

    def login(self):
        login = iu.input_method(
            "Press 1 to check food applications\
            \nPress 2 to check housing applications\
            \nPress -1 to exit.\n", "Not a valid option.",
            {"1": 1, "2": 2, "-1": -1})
        return login

    def applications(self, eidos):
        while True:
            if eidos == "SITHSHS":
                ids = set(self.db.print_application(eidos))
            elif eidos == "ESTIAS":
                ids = set(self.db.print_application(eidos))
            while True:
                id = input(
                    "Enter the id of the application you want to review: ")
                if id.isdigit():
                    if int(id) in ids:
                        break
                    else:
                        print("Not a right id")
                else:
                    print("Not a number")
            print()
            self.db.select_appl_to_review(id, eidos)
            option = input(
                "If you want to continue press enter.\nElse press exit.\n")
            if option == "exit":
                break


if __name__ == "__main__":
    menu = Admin()
