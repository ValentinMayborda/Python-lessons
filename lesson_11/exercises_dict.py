import csv
from uuid import uuid4


def create_index(dictionary: dict, index_key: str) -> dict:
    """
    Создаёт индекс по точному совпадению
    :param dictionary: индекс уникальных айдишников
    :param index_key: ключ по которому создавать индекс
    :return:
    """
    new_index = dict()
    for uid, value in dictionary.items():
        # если это значение уже есть в индексе, просто добавляем
        # например, представителей должности Инженер еще не было, а Директор - уже был
        if value[index_key] in new_index:
            new_index[value[index_key]].append(uid)
        # иначе, создаём список под это значение
        else:
            new_index[value[index_key]] = [uid]
    return new_index

# unique_index, brand_dct, gategory_name
def positions_in_view(
        unique_index_: dict, brand_dct_: dict,
        gategory_name_: str, debug: bool = False
) -> dict:
    """
    Функция считает сколько должностей работает в запрашиваемом отделе
    В возвращаемом словаре будут только те должности, которые есть в отделе, а не все допустимые
    :param unique_index_: индекс сотрудников
    :param brand_dct_: индекс отделов
    :param department_name: имя запрашиваемого отдела
    :param debug: флаг для проверки корректной работы
    :return: словарь, где ключи - представленные в отделе должности
                        значения - их популяция
    """
    positions_in = dict()
    for uid in brand_dct_[gategory_name_]:
        if debug:
            print(unique_index_[uid])
        brand = unique_index_[uid]['brand']
        if brand in positions_in:
            positions_in[brand] += 1
        else:
            positions_in[brand] = 1
    return positions_in


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

    # Виводить на екран статистику скільки товарів є від кожного бренда та від кожної категорії
    category_dct = create_index(unique_index, 'category')

    for key, value in category_dct.items():
        print(f'В категорії {key} є {len(value)} одиниць')
    print('*' * 200)

    brand_dct = create_index(unique_index, 'brand')
    for key, value in brand_dct.items():
        print(f'В бренді {key} є {len(value)} одиниць')


    # рахує розподіл товарів по брендам для кожної категорії та виводить це на екран.
    # Наприклад, в категорії Ноутбуки представлено 6 товарів від Lenovo, 8 від Mac, 10 від Dell, тощо.

    for gategory_name in brand_dct.keys():
        print(
            f'В категорії {gategory_name} ',
            positions_in_view(unique_index, brand_dct, gategory_name)
        )