print('Програма видаляє те що написано в перших дужках () тексту')
text = input('Введіть Ваш текст \n >> ')

# Перевірка чи є () в тексті
if '(' and ')' not in text:
    print(text)
else:
    before = text[:text.find('(')]  # Зріз до (
    after = text[text.find(')')+1:]  # Зріз після )
    out_text = before + after  # Склеювання  зрізів
    print(out_text)
