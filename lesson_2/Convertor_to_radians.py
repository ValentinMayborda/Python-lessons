import math

print("Програма конвертує градуси в радіани")
degrees = int(input('Введіть кількість градусів:'))
radians = round(degrees * math.pi / 180, 5)
print(f'{degrees} градусів = {radians} радіанів')
