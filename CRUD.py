def print_options():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")


def print_holidays(holidays):
    print("Stai atostogos")
    for hol in holidays:
        print(f'{str(hol['id']) + '.':<3} Šalis / miestas {hol['country']:<12}/ {hol['city']:<10}, kaina'
              f' {hol['price']}, '
              f'apgyvendinimas {hol['accomodation']:>12}')