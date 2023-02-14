import os


fileDir = r"SKU"
fileExt = r".json"
lst_json = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]

for filename in os.listdir("SKU"):
    if filename.endswith(fileExt):
        with open(os.path.join("SKU", filename), 'r') as f:
            text = f.read()
            print(text)

i = 1
for file in lst_json:
    print(f'{i}.{file}')
    i += 1
