import os
import csv
import json


class FileProcessor:
    def __init__(self, path):
        self.path = path
        self.entries = []

    def process(self):
        for filename in os.listdir(self.path):
            if filename.endswith('.csv'):
                csv_file = CSVFileProcessor(os.path.join(self.path, filename))
                self.entries += csv_file.process()
            elif filename.endswith('.json'):
                json_file = JSONFileProcessor(os.path.join(self.path, filename))
                self.entries += json_file.process()


class CSVFileProcessor(FileProcessor):
    def __init__(self, path):
        super().__init__(path)

    def process(self):
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                entry = DataEntry(row[0], row[1])
                self.entries.append(entry)
        return self.entries


class JSONFileProcessor(FileProcessor):
    def __init__(self, path):
        super().__init__(path)

    def process(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            for item in data:
                if isinstance(item, dict):
                    entry = DataEntry(item['name'], item['value'])
                    self.entries.append(entry)
        return self.entries


class DataEntry:
    def __init__(self, name, value):
        self.name = name
        self.value = value


if __name__ == '__main__':
    processor = FileProcessor('SKU')
    processor.process()

    for entry in processor.entries:
        print(entry.name, entry.value)
