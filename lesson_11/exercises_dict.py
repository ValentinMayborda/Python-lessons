import csv
from uuid import uuid4


if __name__ == '__main__':
    # Словник для зберігання данних з основного файлу
    data = {
        'data': list()
    }
    # Зчитування з файлу в словник
    with open('tech_inventory.csv', newline='') as csvfive:
        reader = csv.DictReader(csvfive)
        for row in reader:
            data['data'].append(row)
        print(data)

    for key in data['data']:
        print(key)

    #  Створюємо індекс унікальних айді для кожного запису, тобто словник,
    #  де ключі - це згенеровані унікальні айді, а значення - повна інформація про позицію товару
    unique_index = dict()
    for row in data['data']:
        _id = uuid4()
        unique_index[_id] = row

    print(unique_index)
    # Відображення словника
    i = 1
    for key, value in unique_index.items():
        print(f'{i}. {key}, {value}')
        i += 1

    # створює індекс по категоріям та брендам. Тобто словник,
    # де ключі - це назва категорії/бренду, а значення - це перелік унікальних айді товарів,
    # в яких є таке значення поля категорії/бренду
    category_brand_dct = dict()
