import csv
from uuid import uuid4


def create_index(dictionary: dict, index_key: str) -> dict:
    """
    Створює індекс
    :param dictionary: індекс унікальних айді
    :param index_key: ключ по якому створює індекс
    :return:
    """
    new_index = dict()
    for uid, _value in dictionary.items():
        if _value[index_key] in new_index:
            new_index[_value[index_key]].append(uid)
        else:
            new_index[_value[index_key]] = [uid]
    return new_index


def calculate_brand(unique_index_: dict, brand_dct_: dict, сategory_name_: str, debug: bool = False) -> dict:
    """
    Створює словарь по розрахунку

    """
    ware_dct = dict()
    for uid in brand_dct_[сategory_name_]:
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
    print(f'********* Унікалний індекс *************, ************ Повна інформація про позицію товару **************')
    i = 1
    for key, value in unique_index.items():
        print(f'{i}. {key}, {value}')
        i += 1
    print('*' * 200)



    # Виводить на екран статистику скільки товарів є  від кожної категорії
    category_dct = create_index(unique_index, 'category')

    for key, value in category_dct.items():
        print(f'В категорії {key} є {len(value)} одиниць')
    print('*' * 200)

    # Виводить на екран статистику скільки товарів є від кожного бренда
    brand_dct = create_index(unique_index, 'brand')
    for key, value in brand_dct.items():
        print(f'В бренді {key} є {len(value)} одиниць')
    print('*' * 200)

    # Рахує розподіл товарів по брендам для кожної категорії та виводить це на екран.
    # Наприклад, в категорії Ноутбуки представлено 6 товарів від Lenovo, 8 від Mac, 10 від Dell, тощо.

    for сategory_name in category_dct.keys():
        print(f'В категорії {сategory_name}  представлено',
              calculate_brand(unique_index, category_dct, сategory_name))
    print('*' * 200)

    # виводить на екран перелік повної інформації про кожний товар одного обраного бренда та однієї обраної категорії

    # створює індекс по категоріям та брендам. Тобто словник,
    # де ключі - це назва категорії/бренду, а значення - це перелік унікальних айді товарів,
    # в яких є таке значення поля категорії/бренду