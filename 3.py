import csv

with open('scientist_sorted.txt', 'r', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='#')
    reader = [row for row in reader]

    command = input()
    while command != 'эксперимент':
        command = command.split('.')
        command.reverse()
        command = '-'.join(command)
        print(command)

        left = 0
        right = len(reader) - 1
        mid = left + (right - left) // 2

        while left <= right:
            print(left, right, reader[mid])
            if reader[mid]['date'] == command:
                print(f'Ученый {reader[mid]["ScientistName"]} создал препарат: {reader[mid]["preparation"]} - {reader[mid]["date"]}')
                break
            elif reader[mid]['date'] < command:
                left = mid + 1
                mid = left + (right - left) // 2
            else:
                right = mid - 1
                mid = left + (right - left) // 2

        else:
            print('В этот день ученые отдыхали')
        command = input()