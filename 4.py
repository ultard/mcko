import csv

def generate_password(username):
    """
    Генерирует логин пароль для пользователя

    Параметры:
    username - имя пользователя

    Возвращает:
    пароль для пользователя
    """

with open('scientist.txt', 'r', encoding="utf") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='#')
    reader = [row for row in reader]

