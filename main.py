from CRUD import print_options
from db_CRUD import *

holidays = load_holidays()
id_counter = 3

while True:
    print_options()
    choise = input()
    match choise:
        case '1':
            print_holidays(holidays)
        case '2':
            id_counter = add_holidays(id_counter,holidays)
        case '3':
            edit_holidays(holidays)
        case '4':
            delete_holidays(holidays)
        case '5':
            print("isvaziuoju i atostogos(exit)")
            break
        case _: #defaultas, kai neatitiko nei vieno case
            print("patikrinkite ivesti")

