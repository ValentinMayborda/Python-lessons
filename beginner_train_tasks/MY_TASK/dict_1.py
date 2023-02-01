#В переменной s хранится строка пар число:слово. Дополните приведенный код,
# используя генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.
#Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).
#Примечание 2. Выводить содержимое словаря result не нужно.

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
lst = [elem for elem in s.split()]
result = {int(i[:i.find(':')]): i[i.find(':')+1:] for i in lst}

print(lst)
for elem, value in result.items():
    print(type(elem), elem, type(value), value)

print(result)
