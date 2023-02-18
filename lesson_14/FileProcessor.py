import os
# from lesson_14.CSVFileProcessor import CSVFileProcessor
# from lesson_14.JSONFileProcessor import JSONFileProcessor


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
