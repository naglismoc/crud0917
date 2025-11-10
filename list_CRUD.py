from CRUD import print_holidays
from data import load_holidays

def add_holidays(id_counter, holidays):
    print("Itraukti atostogas i sarasa:")
    print("Įveskite šalį")
    country = input()
    print("Įveskite miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    apt = input()
    print("Įveskite kainą")
    price = int(input())
    id_counter += 1
    holiday = {'id': id_counter, 'country': country, 'city': city, 'accomodation': apt, 'price': price}
    holidays.append(holiday)
    return id_counter

def edit_holidays(holidays):
    print_holidays(holidays)
    print("Pasirinkita atostogų id kurį norite keisti:")
    edit_id = input()
    for hol in holidays:
        if str(hol['id']) == edit_id:
            print(hol)
            print("Įveskite šalį")
            hol['country'] = input()
            print("Įveskite miestą")
            hol['city'] = input()
            print("Įveskite apgyvendinimo tipą")
            hol['accomodation'] = input()
            print("Įveskite kainą")
            hol['price'] = int(input())
            break

def delete_holidays(holidays):
    print("trinu atostogos")
    print_holidays(holidays)
    print("Pasirinkita atostogų id kurį norite šalinti:")
    del_id = input()
    for hol in holidays:
        if str(hol['id']) == del_id:
            holidays.remove(hol)
            print("Atostogos sėkmingai ištrintos")
            break
