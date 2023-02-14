import os

for filename in os.listdir("SKU"):
   with open(os.path.join("SKU", filename), 'r') as f:
       text = f.read()
       print(text)

