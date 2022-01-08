import sqlite_conection as sq
import datetime 
class Menu:
    def __init__(self) -> None:
        self.db = sq.DB_Connection("merimna.db")
        self.am = self.login()
        
        self.option = self.basic_menu()
        match self.option:
            case "1":
                # some code here
                self.coupons()
                return
            case "2":
                # some code here
                self.food_application()
                return
            case "3":
                # some code here
                self.housing_application()
                return
            case _:
                return
    
    def login(self) -> None:
        print("Give your AM")
        am = input()
        if len(self.db.retrieval_query(f"SELECT * FROM FOITHTHS WHERE AM = {am}")) == 0:
            name = input("Write your full name: ")
            phone = input("Write your cellphone: ")
            self.db.insert_student(name , am , phone)
        return am
    def basic_menu(self) -> None:
        print(f"Press 1 to buy food coupons\
        \nPress 2 to make application for food\
        \nPress 3 to make application for housing")
        return input()
    
    def coupons(self) -> None:
        price = 2
        while True:
            quantity= input("Enter the quantity of coupons ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Not a number")
        date = datetime.datetime.now()
        date = date.strftime("%x")
        self.db.insert_purchase(quantity , self.am , date , total = price * quantity)
        print(f"Amount to pay = {price * quantity}")
    
    def food_application(self) -> None:
        pass
    def housing_application(self) -> None:
        pass


if __name__ == "__main__":
    menu = Menu()
