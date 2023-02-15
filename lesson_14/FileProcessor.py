import os
import json
import csv


class FileProcessor:
    pass


def show_files(lst: list):
    for elem in lst:
        print(elem)



fileDir = r"SKU"
fileExt_json = r".json"
fileExt_csv = r".csv"
lst_json = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt_json)]
lst_csv = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt_csv)]

# Список для спільного зберігання данних
data_csv_lst = list()
data_json_lst = list()

for filename in os.listdir("SKU"):

    if filename.endswith(fileExt_csv):
        with open(os.path.join("SKU", filename), 'r') as f:
            reader_csv = f.readlines()
            for row in reader_csv:
                data_csv_lst.append(row)
    elif filename.endswith(fileExt_json):
        with open(os.path.join("SKU", filename), 'r') as f:
            reader_json = f.readlines()
            for row in reader_json:
                data_json_lst.append(row)


# i = 0
# for elem in data_csv_lst:
#     print(elem)
    #i += 1


# i = 1
# for elem in data_json_lst:
#     print(i, elem)
#     i += 1
show_files(lst_csv)
show_files(lst_json)

