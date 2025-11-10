# pip install mysql-connector-python
import mysql.connector

from CRUD import print_holidays

headers = ['id', 'country', 'city', 'accomodation', 'price']

DB_CONFIG = {# final kintamasis, konstanta (nekis kodo eigoj)
    'host':"127.0.0.1", # alternatyv rasyti localhost
    'port':3312,
    'user':'root',
    'password':'root',
    'database':'holidays'
}

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_holidays():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM holidays")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    holidays = []
    for row in rows:
        holiday = {}
        for i in range(len(headers)):
            holiday[headers[i]] = str(row[i])
        holidays.append(holiday)
    return holidays


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

    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO `holidays`.`holidays` (`country`,`city`,`accomodation`,`price`) VALUES (%s,%s,%s,%s)',
                (country,city,apt,price))
    conn.commit()
    cur.close()
    conn.close()
    return id_counter

def edit_holidays(holidays):
    print_holidays(holidays)
    print("Pasirinkite atostogų id kurį norite keisti:")
    edit_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays where id = %s",(edit_id,))
    hol = cur.fetchone()
    conn.close()
    cur.close()
    print(hol)
    print("Įveskite šalį")
    country = input()
    print("Įveskite miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    apt = input()
    print("Įveskite kainą")
    price = int(input())
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE `holidays`.`holidays` SET `country` = %s , `city` = %s, `accomodation` = %s, `price` = %s "
                "WHERE `id` = %s;",(country, city, apt, price, edit_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_holidays(holidays):
    print("trinu atostogos")
    print_holidays(holidays)
    print("Pasirinkita atostogų id kurį norite šalinti:")
    del_id = input()
    conn =get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM `holidays`.`holidays` WHERE `id` = %s;',(del_id,))
    conn.commit()
    cur.close()
    conn.close()


