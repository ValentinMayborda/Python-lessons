import csv
from lesson_14.DataEntry import DataEntry
from lesson_14.FileProcessor import FileProcessor


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
