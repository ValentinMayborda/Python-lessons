import os

for filename in os.listdir("SKU"):
   with open(os.path.join("SKU", filename), 'r') as f:
       text = f.read()
       print(text)
   print('*' * 200)

fileDir = r"SKU"
fileExt = r".csv"
lst_csv = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]

print(lst_csv)

print('*' * 200)
fileDir = r"SKU"
fileExt = r".json"
lst_json = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]

print(lst_json)
