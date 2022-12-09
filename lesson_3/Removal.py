print('Програма видаляє те що написано в перших дужках () тексту')
text = input('Введіть Ваш текст \n >> ')

before = text[:text.find('(')]
after = text[text.find(')')+1:]

out_text = before + after
print(out_text)
