import os

fileDir = r"SKU"
fileExt = r".csv"
lst_csv = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]


i = 1
for file in lst_csv:
    print(f'{i}.{file}')
    i += 1
