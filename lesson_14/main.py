from program import*


if __name__ == '__main__':

    processor = FileProcessor('SKU')
    #processor.process()

    for entry in processor.entries:
        print(entry.name, entry.value)
