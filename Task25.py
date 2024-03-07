name = input("Введите Ваше имя: ")
print (f" Длина Вашего имени {len(name)} символов")
if len(name) < 5:
    second_name = input("Введите Вашу фамилию: ")
    name = name + second_name
    print(name.upper())
else:
    print(name.lower())