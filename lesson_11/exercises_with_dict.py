import csv

try:
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        """
        - model
        - category
        - brand
        - price"""
        for row in reader:

            print(row['model'], row['category'], row['brand'], row['price'])
except FileNotFoundError:
    print('Файл не знайдено!')
except:
    print('Помилка обробки файлу!')


