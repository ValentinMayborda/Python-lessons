# Програма приймає строку й повідомляє які там є голосні літери
print('Програма приймає строку й повідомляє які там є голосні літери.')

text = input('Введіть строку: ').lower()
# А, Е, Є, И, І, Ї, О, У, Ю, Я - голосні
if 'а' in text:
    print('Є голосна "a"')
if 'е' in text:
    print('Є голосна "e"')
if 'є' in text:
    print('Є голосна "є"')
if 'и' in text:
    print('Є голосна "и"')
if 'і' in text:
    print('Є голосна "і"')
if 'ї' in text:
    print('Є голосна "ї"')
if 'о' in text:
    print('Є голосна "о"')
if 'у' in text:
    print('Є голосна "у"')
if 'ю' in text:
    print('Є голосна "ю"')
if 'я' in text:
    print('Є голосна "я"')
else:
    print('Голосні відсутні!')
