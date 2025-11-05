holidays = [
            {
                'id': 1,
                "country":"Lithuania",
                "city":"Palanga",
                "price":20,
                "accomodation":"hotel"
            },
            {
                'id': 2,
                "country":"Turkija",
                "city":"Alanya",
                "price":60,
                "accomodation":"hostel"
            },
            {
                'id': 3,
                "country":"Cyprus",
                "city":"Larnaka",
                "price":70,
                "accomodation":"apartaments"
            }
        ]
id_counter = 3

while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    choise = input()
    match choise:
        case '1':
            print("Stai atostogos")
            for hol in holidays:
                print(f'{str(hol['id'])+'.':<3} Šalis / miestas {hol['country']:<12}/ {hol['city']:<10}, kaina'
                      f' {hol['price']}, '
                      f'apgyvendinimas {hol['accomodation']:>12}')
        case '2':
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
            holiday = {'id':id_counter, 'country':country, 'city':city, 'accomodation':apt, 'price':price}
            holidays.append(holiday)
        case '3':
            for hol in holidays:
                print(f'{str(hol['id']) + '.':<3} Šalis / miestas {hol['country']:<12}/ {hol['city']:<10}, kaina'
                      f' {hol['price']}, '
                      f'apgyvendinimas {hol['accomodation']:>12}')
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
        case '4':
            print("trinu atostogos")
            for hol in holidays:
                print(f'{str(hol['id']) + '.':<3} Šalis / miestas {hol['country']:<12}/ {hol['city']:<10}, kaina'
                      f' {hol['price']}, '
                      f'apgyvendinimas {hol['accomodation']:>12}')
            print("Pasirinkita atostogų id kurį norite šalinti:")
            del_id = input()
            for hol in holidays:
                if str(hol['id']) == del_id:
                    holidays.remove(hol)
                    print("Atostogos sėkmingai ištrintos")
                    break
        case '5':
            print("isvaziuoju i atostogos(exit)")
            break
        case _: #defaultas, kai neatitiko nei vieno case
            print("patikrinkite ivesti")

