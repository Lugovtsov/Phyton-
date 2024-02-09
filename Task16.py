qvestion = input("Идет ли сейчас дождь: ")
qvestion = str.lower(qvestion)
if qvestion == "да":
    qvestion2 = str.lower(input("Ветренно ли сейчас на улице: "))
    if qvestion2 == "да":
        print("Слишком ветренно для зонтика")
    else:
        print("Возьми зонтик")
else:
    print("Приятного Вам дня!")