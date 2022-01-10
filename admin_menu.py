import sqlite_admin


class Admin:
    def __init__(self) -> None:
        self.option = self.login()
        self.db = sqlite_admin.DB_Connection("Data_Creation/merimna.db")
        if self.option == "1":
            self.food_appl()
        elif self.option == "2":
            self.housing_appl()

    def login(self):
        login = None
        options = ("1", "2")
        while True:
            print(
                f"""Press 1 to check food applications\
            \nPress 2 to check housing applications"""
            )
            login = input()
            if login in options:
                return login
            else:
                print("Not a valid option.")

    def food_appl(self):
        while True:
            ids = set(self.db.print_food_appl())
            while True:
                id = input("Enter the id of the application you want to review: ")
                if id.isdigit():
                    if int(id) in ids:
                        break
                    else:
                        print("Not a right id")
                else:
                    print("Not a number")
            print()
            self.db.select_appl_to_review(id, "SITHSHS")
            option = input("If you want to continue press enter.\nElse press exit.\n")
            if option == "exit":
                break

    def housing_appl(self):
        while True:
            ids = set(self.db.print_housing_appl())
            while True:
                id = input("Enter the id of the application you want to review: ")
                if id.isdigit():
                    if int(id) in ids:
                        break
                    else:
                        print("Not a right id")
                else:
                    print("Not a number")
            print()
            self.db.select_appl_to_review(id, "ESTIAS")
            option = input("If you want to continue press enter.\nElse press exit.\n")
            if option == "exit":
                break


if __name__ == "__main__":
    menu = Admin()
