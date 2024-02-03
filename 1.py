import csv

with open('scientist_sorted.txt', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='#')

    receipts = {}
    for row in reader:
        preparation = receipts.get(row['preparation'], 0)

        if preparation == 0:
            receipts[row['preparation']] = {
                "trueScientist": row['ScientistName'],
                "falseScientists": [],
                "date": row['date']
            }
        else:
            if preparation['date'] > row['date']:
                receipts[row['preparation']]['trueScientist'] = row['ScientistName']
                receipts[row['preparation']]['falseScientists'].append({ "author": preparation['trueScientist'], "date": preparation['date'] })
                receipts[row['preparation']]['date'] = row['date']
            else:
                receipts[row['preparation']]['falseScientists'].append({ "author": row['ScientistName'], "date": row['date'] })

    for key, value in receipts.items():
        print(f"Разработчиками {key} были такие люди:")

        for data in value['falseScientists']:
            print(f"{data['author']} - {data['date']}")

        print(f"Оригинальный рецепт принадлежит: {value['trueScientist']}\n")