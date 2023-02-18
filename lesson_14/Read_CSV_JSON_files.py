import os
import csv
import json


class FileProcessor:
    def __init__(self, path):
        """Ініціалізує шлях до папки з файлами та список елементів."""
        self.path = path
        self.entries = []  # список для збереження об'єктів DataEntry

    def process(self):
        """Обробляє файли з папки та додає результат в список entries."""
        for filename in os.listdir(self.path):  # перебираємо файли у папці
            if filename.endswith('.csv'):  # якщо це CSV-файл
                csv_file = CSVFileProcessor(os.path.join(self.path, filename))
                self.entries += csv_file.process()  # додаємо результат обробки до загального списку
            elif filename.endswith('.json'):  # якщо це JSON-файл
                json_file = JSONFileProcessor(os.path.join(self.path, filename))
                self.entries += json_file.process()  # додаємо результат обробки до загального списку


class CSVFileProcessor(FileProcessor):
    def __init__(self, path):
        """Ініціалізує шлях до CSV-файлу та список елементів."""
        super().__init__(path)
        self.entries = []  # список для збереження об'єктів DataEntry

    def process(self):
        """Обробляє CSV-файл та повертає список елементів DataEntry."""
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # пропускаємо перший рядок (заголовки стовпців)
            for row in reader:
                entry = DataEntry(row[0], row[1])
                self.entries.append(entry)
        return self.entries  # повертаємо список з об'єктами DataEntry


class JSONFileProcessor(FileProcessor):
    def __init__(self, path):
        """Ініціалізує шлях до JSON-файлу та список елементів."""
        super().__init__(path)
        self.entries = []

    def process(self):
        """Обробляє JSON-файл та повертає список елементів DataEntry."""
        with open(self.path, 'r') as f:
            data = json.load(f)
            for item in data:
                # щоб переконатися, що item є словником, перш ніж спробувати отримати значення name та value.
                if isinstance(item, dict):
                    entry = DataEntry(item['name'], item['value'])
                    self.entries.append(entry)
        return self.entries  # повертаємо список з об'єктами DataEntry


class DataEntry:
    def __init__(self, name, value):
        """Ініціалізує об'єкт з іменем та значенням."""
        self.name = name
        self.value = value


if __name__ == '__main__':
    processor = FileProcessor('SKU')
    processor.process()

    # виводить елементи списку entries
    for entry in processor.entries:
        print(entry.name, entry.value)
