import student_menu as sm


def food_application_form() -> None | list:
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
            ak_etos_eggrafhs, step = sm.Menu.input_number(
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
            barcode, step = sm.Menu.input_number(
                "Barcode of academic id: ", "Not a number"
            )
            order += step
        elif order == 4:
            total_patros, step = sm.Menu.input_number(
                "Total income of father: ", "Not a number"
            )
            order += step
        elif order == 5:
            total_mhtros, step = sm.Menu.input_number(
                "Total income of mother: ", "Not a number"
            )
            order += step
        elif order == 6:

            ar_melon_oikegias, step = sm.Menu.input_number(
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


if __name__ == "__main__":
    results = food_application_form()
    # rint(sm.Menu.input_number("test\n", "error\n"))
