import csv
from uuid import uuid4


def create_index(dictionary: dict, index_key: str) -> dict:
    """
    Створює індекс по категоріям та брендам
    :param dictionary: індекс унікальних айді
    :param index_key: ключ по якому створює індекс
    :return: створений індекс
    """
    new_index = dict()
    for uid, _value in dictionary.items():
        if _value[index_key] in new_index:
            new_index[_value[index_key]].append(uid)
        else:
            new_index[_value[index_key]] = [uid]
    return new_index


def calculate_brand_in_category(unique_index_: dict, brand_dct_: dict,
                                category_name_: str, debug: bool = False) -> dict:
    """
    Рахує кількість брендів в категорії
    :param unique_index_: словник унікальних індексів
    :param brand_dct_: індекс категорії
    :param category_name_: назва категорії
    :param debug: перевірка коректної роботи
    :return: словник
    """

    ware_dct = dict()
    for uid in brand_dct_[category_name_]:
        if debug:
            print(unique_index_[uid])
        brand = unique_index_[uid]['brand']
        if brand in ware_dct:
            ware_dct[brand] += 1
        else:
            ware_dct[brand] = 1
    return ware_dct


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

    #  Створюємо індекс унікальних айді для кожного запису, тобто словник,
    #  де ключі - це згенеровані унікальні айді, а значення - повна інформація про позицію товару
    unique_index = dict()
    for row in data['data']:
        _id = uuid4()
        unique_index[_id] = row

    # Відображення словника
    print(f'********* Унікальний індекс *************, ************ Повна інформація про позицію товару **************')
    i = 1
    for key, value in unique_index.items():
        print(f'{i}. {key}, {value}')
        i += 1
    print('*' * 200)

    # Створення індексу по категорії та вивід кількості товарів в категорії
    category_dct = create_index(unique_index, 'category')
    for key, value in category_dct.items():
        print(f'В категорії {key} є {len(value)} одиниць')
    print('*' * 200)

    # Створення індексу по бренду та вивід кількості товарів бренду
    brand_dct = create_index(unique_index, 'brand')
    for key, value in brand_dct.items():
        print(f'В бренді {key} є {len(value)} одиниць')
    print('*' * 200)

    # виводить на екран перелік повної інформації про кожний товар одного обраного бренда та однієї обраної категорії
    print('Виводить перелік повної інформації по бренду "HP" \n')
    _brand = 'HP'
    i = 1
    for elem in brand_dct[_brand]:
        print(f'{i}. {unique_index[elem]}')
        i += 1
    print('*' * 200)

    print('Виводить перелік повної інформації по категорії "Laptop" \n')
    _category = 'Laptop'
    i = 1
    for elem in category_dct[_category]:
        print(f'{i}. {unique_index[elem]}')
        i += 1
    print('*' * 200)

    # Рахує розподіл товарів по брендам для кожної категорії та виводить це на екран.
    # Наприклад, в категорії Ноутбуки представлено 6 товарів від Lenovo, 8 від Mac, 10 від Dell, тощо.
    for category_name in category_dct.keys():
        print(f'В категорії {category_name}  представлено :',
              calculate_brand_in_category(unique_index, category_dct, category_name))
