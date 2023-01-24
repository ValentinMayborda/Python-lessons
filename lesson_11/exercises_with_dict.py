import csv
from uuid import uuid4


# Словарь де зберігаються всі записи з файлу
data = {
        'data': list()
    }

try:
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        """
        - model
        - category
        - brand
        - price"""
        lst_brand = list()  # список брендів
        for row in reader:
            # print(row['model'], row['category'], row['brand'], row['price'])

            lst_brand.append(row['brand'])

            data['data'].append(row)

        #  створює індекс унікальних айді для кожного запису, тобто словник,
        #  де ключі - це згенеровані унікальні айді, а значення - повна інформація про позицію товару
        unique_index = dict()
        for row in data['data']:
            # створює унікальний айді
            _uid = uuid4()
            # зберігаєм під уникальним айді повні данні про запис
            unique_index[_uid] = row['model'], row['category'], row['brand'], row['price']

        # print(unique_index)
        i = 1
        for key, value in unique_index.items():
            print(f'{i}. {key} : {value}')
            i += 1


        # print(data)

except FileNotFoundError:
    print('Файл не знайдено!')
except:
    print('Помилка обробки файлу!')


