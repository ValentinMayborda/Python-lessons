import csv

try:
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        """
        - model
        - category
        - brand
        - price"""
        lst_brand = list()
        for row in reader:
            print(row['model'], row['category'], row['brand'], row['price'])
            lst_brand.append(row['brand'])

        set_brand = set(lst_brand)
        print(set_brand)

except FileNotFoundError:
    print('Файл не знайдено!')
except:
    print('Помилка обробки файлу!')


