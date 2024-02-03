import csv
import random
import string


def create_initials(s):
    """
    Эта функция, которая создает логин на основе имени

    Параметры:
    s - имя пользователя

    Возвращает:
    строка - логин на основе имени
    """
    names = s.split()
    return f'{names[0]}_{names[1][0]}{names[2][0]}'


def create_password():
    """
    Эта функция, которая создает случайный пароль

    Возвращает:
    строку - случайный пароль
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(10))
    return password


students_passwords = []
with open('scientist.txt', 'r', encoding="utf") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter='#'))

    for row in reader:
        row['login'] = create_initials(row['ScientistName'])
        row['password'] = create_password()
        students_passwords.append(row)

with open('scientist_password.csv', 'w', newline='', encoding="utf") as file:
    writer = csv.DictWriter(file, delimiter='#', fieldnames=['ScientistName', 'preparation', 'date', 'components', 'login', 'password'])
    writer.writeheader()
    writer.writerows(students_passwords)
