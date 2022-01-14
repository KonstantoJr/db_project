# Requires an input from user that is a number
# Variable Text is the message displayed to the user requesting the input
# Variable error is the error message displayed to the user in case of a wrong input
# Acceptable inputs are all positive numbers and -1
# In case of -1 the method returns None and -1
# This is so we know the user wants to go back
def input_number(text, error):
    while True:
        inp = input(text)
        if inp.isdigit():
            return inp, 1
        elif inp == "-1":
            return None, -1
        print(error)


# Variable Text is the message displayed to the user requesting the input
# Variable error is the error message displayed to the user in case of a wrong input
# Variable options is a dictionary
# The keys of the dictionary are the inputs required from the user
# The values for each key is the returned value
def input_method(text: str, error: str, options: dict):
    while True:
        inp = input(text)
        if inp in options.keys():
            return options[inp]
        print(error)


def housing_appl_form_input():
    I = {"kathgoria": None, "dnsh_monimhs": None, "thl_goneon": None, "epaggelma_patros": None, "epaggelma_mhtros": None, "topothesia_tmhmatos": None, "total_patros": None, "total_mhtros": None, "total_idiou": None, "ar_melon": None, "adelfia_pou_spoudazoun": None,
         "goneis_me_eidikes_anagkes": None, "diazeugmenoi_goneis": None, "orfanos_apo_enan_gonea": None, "poluteknh_oikogenia": None, "stratiotikh_thhteia_aderfou": None, "melh_oikogenias_me_eidikes_anagkes": None}
    order = 0
    print("Fill out the following information\nPress -1 in any step to go back a step")
    while True:
        if order == 0:
            I["kathgoria"] = input_method(
                "Student Category:\
                \nPress 1 for first year student\
                \nPress 2 for older year student\
                \nPress 3 for postgraduate student\
                \nPress 4 for homogenous student\
                \nPress 5 for foreign student\
                \nPress -1 to go back\n",
                "Not an option",
                options={
                    "1": "FIRST_YEAR",
                    "2": "OLDER_YEAR",
                    "3": "POSTGRADUATE",
                    "4": "HOMOGENOUS",
                    "5": "FOREIGN",
                    "-1": -1
                },
            )
            if I["kathgoria"] == -1:
                return None
            order += 1
        elif order == 1:
            I["dnsh_monimhs"] = input("Address of main residence: ")
            if I["dnsh_monimhs"] == "-1":
                order += -1
            else:
                order += 1
        elif order == 2:
            I["thl_goneon"], step = input_number(
                "Phone number of parent: ", "Not a number")
            order += step
        elif order == 3:
            I["epaggelma_patros"] = input("Fathers occupation: ")
            if I["epaggelma_patros"] == "-1":
                order += -1
            else:
                order += 1
        elif order == 4:
            I["epaggelma_mhtros"] = input("Mothers occupation: ")
            if I["epaggelma_mhtros"] == "-1":
                order += -1
            else:
                order += 1
        elif order == 5:
            I["topothesia_tmhmatos"] = input_method(
                "Department Location\n\
                            \nPress 1 for Πανεπιστημιούπολη Ρίο\
                            \nPress 2 for Κουκούλι Πατρών\
                            \nPress 3 for Αγρίνιο\
                            \nPress -1 to go back\n",
                "Not an option",
                options={
                    "1": "Πανεπιστημιούπολη Ρίο",
                    "2": "Κουκούλι Πατρών",
                    "3": "Αγρίνιο",
                    "-1": -1
                },
            )
            if I["topothesia_tmhmatos"] == -1:
                order += -1
            else:
                order += 1
        elif order == 6:
            I["total_patros"], step = input_number(
                "Total income of father: ", "Not a number")
            order += step
        elif order == 7:
            I["total_mhtros"], step = input_number(
                "Total income of mother: ", "Not a number")
            order += step
        elif order == 8:
            I["total_idiou"], step = input_number(
                "Total personal income : ", "Not a number")
            order += step
        elif order == 9:
            I["ar_melon"], step = input_number(
                "Number of people in family: ", "Not a number")
            order += step
        elif order == 10:
            I["adelfia_pou_spoudazoun"], step = input_number(
                "Brothers and Sisters studying: ", "Not a number"
            )
            order += step
        elif order == 11:
            I["goneis_me_eidikes_anagkes"] = input_method(
                "Parents with special needs\
                        \nPress 1 for YES\
                        \nPress 2 for NO\
                        \nPress -1 to go back\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ", "-1": -1},
            )
            if I["goneis_me_eidikes_anagkes"] == -1:
                order += -1
            else:
                order += 1
        elif order == 12:
            I["diazeugmenoi_goneis"] = input_method(
                "Divorced Parents\n\
                        \nPress 1 for YES\
                        \nPress 2 for NO\
                        \nPress -1 to go back\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ", "-1": -1},
            )
            if I["diazeugmenoi_goneis"] == -1:
                order += -1
            else:
                order += 1
        elif order == 13:
            I["orfanos_apo_enan_gonea"] = input_method(
                "Orphan by one parent\
                        \nPress 1 for YES\
                        \nPress 2 for NO\
                        \nPress -1 to go back\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ", "-1": -1},
            )
            if I["orfanos_apo_enan_gonea"] == -1:
                order += -1
            else:
                order += 1
        elif order == 14:
            I["poluteknh_oikogenia"] = input_method(
                "Many children family\
                        \nPress 1 for YES\
                        \nPress 2 for NO\
                        \nPress -1 to go back\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ", "-1": -1},
            )
            if I["poluteknh_oikogenia"] == -1:
                order += -1
            else:
                order += 1
        elif order == 15:
            I["stratiotikh_thhteia_aderfou"] = input_method(
                "Brother in military service\
                        \nPress 1 for YES\
                        \nPress 2 for NO\
                        \nPress -1 to go back\n",
                "Not an option",
                options={"1": "ΝΑΙ", "2": "ΟΧΙ", "-1": -1},
            )
            if I["stratiotikh_thhteia_aderfou"] == -1:
                order += -1
            else:
                order += 1
        elif order == 16:
            I["melh_oikogenias_me_eidikes_anagkes"], step = input_number(
                "Number of people in your family with special needs: ", "Not a number"
            )
            order += step
        elif order >= 17:
            return I


def food_application_form_input():
    order = 0
    I = {
        "ak_etos_eggrafhs": None,
        "dnsh_katoikias": None,
        "dnsh_monimhs": None,
        "barcode": None,
        "total_patros": None,
        "total_mhtros": None,
        "ar_melon_oikegias": None
    }
    while True:

        if order == 0:
            I["ak_etos_eggrafhs"], step = input_number(
                "Academic year of entry: ", "Not a valid year"
            )
            if step == -1:
                return None
            order += step
        elif order == 1:
            I["dnsh_katoikias"] = input("Address of residence: ")
            if I["dnsh_katoikias"] == "-1":
                order += -1
            else:
                order += 1
        elif order == 2:
            I["dnsh_monimhs"] = input("Address of main residence: ")
            if I["dnsh_monimhs"] == "-1":
                order += -1
            else:
                order += 1
        elif order == 3:
            I["barcode"], step = input_number(
                "Barcode of academic id: ", "Not a number"
            )
            order += step
        elif order == 4:
            I["total_patros"], step = input_number(
                "Total income of father: ", "Not a number"
            )
            order += step
        elif order == 5:
            I["total_mhtros"], step = input_number(
                "Total income of mother: ", "Not a number"
            )
            order += step
        elif order == 6:

            I["ar_melon_oikegias"], step = input_number(
                "Number of people in family: ", "Not a number"
            )
            order += step
        elif order >= 7:
            return I
