import json
from lesson_14.DataEntry import DataEntry
from lesson_14.FileProcessor import FileProcessor


class JSONFileProcessor(FileProcessor):
    def __init__(self, path):
        super().__init__(path)

    def process(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            for item in data:
                entry = DataEntry(item['name'], item['value'])
                self.entries.append(entry)
