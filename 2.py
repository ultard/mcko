import csv

def fast_sort(array, value):
    """
    Алгоритм быстрой сортировки массива

    Параметры:
    object - изначальный список, который нужно отсортировать
    value - по какому параметру в с списке нужно отсортировать

    Возвращает:
    список- отсортированный алгоритмом список
    """

    if len(array) <= 1:
        return array

    pivot = array[0][value]

    left = [x for x in array[1:] if x[value] <= pivot]
    right = [x for x in array[1:] if x[value] > pivot]

    return fast_sort(left, value) + [array[0]] + fast_sort(right, value)


# читаем файл и сортируем данные
with open('scientist.txt', 'r', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='#')

    array = [row for row in reader][1:]
    array = fast_sort(array, 'date')

# записываем в файл результат сортировки
with open('scientist_sorted.txt', 'w', newline='', encoding="utf8") as file:
    writer = csv.DictWriter(file, delimiter='#', fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(array)
