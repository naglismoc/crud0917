import csv

headers = ['id', 'country', 'city', 'price', 'accomodation']
def load_holidays():
    with open("lithuania_accommodation.csv", mode='r',encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_holidays(holidays):
    with open("lithuania_accommodation.csv",mode="w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(holidays)


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
    new_id  = str(int(holidays[-1]['id']) + 1) if len(holidays) > 0 else 1
    holiday = {'id': new_id, 'country': country, 'city': city, 'accomodation': apt, 'price': price}
    holidays.append(holiday)
    save_holidays(holidays)
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
    save_holidays(holidays)

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
    save_holidays(holidays)

def print_holidays(holidays):
    print("Stai atostogos")
    for hol in holidays:
        print(f'{str(hol['id']) + '.':<3} Šalis / miestas {hol['country']:<12}/ {hol['city']:<10}, kaina'
              f' {hol['price']}, '
              f'apgyvendinimas {hol['accomodation']:>12}')


def print_options():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")