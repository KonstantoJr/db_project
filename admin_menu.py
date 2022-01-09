import sqlite_conection


class Admin:
    def __init__(self) -> None:
        self.option = self.login()

        if self.option == "1":
            self.food_appl()
        elif self.option == "2":
            self.housing_appl()

    def login(self):
        print(
            f"""Press 1 to check food applications\
        \nPress 2 to check housing applications"""
        )
        return input()

    def food_appl(self):
        pass

    def housing_appl(self):
        pass


if __name__ == "__main__":
    menu = Admin()
