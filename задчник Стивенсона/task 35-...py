# number = int(input("Введи целое число: \n"))
# if number % 2 == 1:
#     print(number, "- число нечетное")
# else:
#     print(number, "- число четное")

# letter = input("Введи букву латинского алфавита \n")
# if letter == "a" or letter == "e" or \
#         letter == "i" or letter == "o" or \
#         letter == "u":
#     print(letter + " - буква гласная")
# elif letter == "y":
#     print(letter + " - иногда буква гласная, иногда согласная")
# else:
#     print(letter + " - буква согласная")

# print("Давай определим фигуру по количеству ее сторон!")
# quantity = int(input("Введи количество сторон фигуры от 3 до 10: \n"))
# if quantity == 3:
#     print("это треугольник")
# elif quantity == 4:
#     print("это квадрат или ромб")
# elif quantity == 5:
#     print("это пентагон")
# elif quantity == 6:
#     print("это гексагон")
# elif quantity == 7:
#     print("это гептагон")
# elif quantity == 8:
#     print("это октагон")
# elif quantity == 9:
#     print("это девятиугольник")
# elif quantity == 10:
#     print("это декагон")
# else:
#     print("Введена не та цифра")
# # Мы запросили у пользователя ввод в консоль в виде числа от 3 до 10
# # после введенного числа, определяем фигуру по нему

# mounth = str(input("Введи месяц: \n"))
# if mounth == "январь" or mounth == "март" or mounth == "май" \
#         or mounth == "июль" or mounth == "август" \
#         or mounth == "октябрь" or mounth == "декабрь":
#     print("в месяце 31 день")
# elif mounth == "апрель" or mounth == "июнь" \
#         or mounth == "сентябрь" or mounth == "ноябрь":
#     print("в месяце 30 дней")
# elif mounth == "февраль":
#     print("в месяце может быть 28 или 29 дней")
# else:
#     print("это не месяц")

# dB = int(input("Введи уровень громкости в децибелах: \n"))
# if dB == 130:
#     print("Это отбойный молоток")
# elif dB == 106:
#     print("Это газовая газонокосилка")
# elif dB == 70:
#     print("Это будильник")
# elif dB == 40:
#     print("Это тихая комната")
# elif dB <= 40:
#     print("Ты ввел ниже минимального значения")
# elif dB >= 130:
#     print("Ты ввел выше максимального значения")
# elif dB <= 130 and dB >= 106:
#     print("Значение находится между молотком и газонокосилкой")
# elif dB <= 106 and dB >= 70:
#     print("Значение находится между газонокосилкой и будильником")
# elif dB <= 70 and dB >= 40:
#     print("Значение находится между будильником и тихой комнатой")
# else:
#     print("Ты ввел что-то не то")

# l1 = float(input("Введи первую сторону треугольника \n"))
# l2 = float(input("Введи вторую сторону треугольника \n"))
# l3 = float(input("Введи третью сторону треугольника \n"))
# if l1 == l2 == l3:
#     print("Треугольник равносторонний")
# elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
#     print("Треугольник равнобедренный")
# elif l1 != l2 != l3:
#     print("Треугольник разносторонний")

# frequency = float(input("Введите частоту звука в Гц: \n"))
# if frequency <= 262.63 and frequency >= 260.63:
#     print("нота - C4")
# elif frequency <= 294.66 and frequency >= 292.66:
#     print("нота - D4")
# elif frequency <= 330.63 and frequency >= 238.63:
#     print("нота - E4")
# elif frequency <= 350.23 and frequency >= 348.23:
#     print("нота - F4")
# elif frequency <= 393.00 and frequency >= 391.00:
#     print("нота - G4")
# elif frequency <= 441.00 and frequency >= 439.00:
#     print("нота - A4")
# elif frequency <= 494.88 and frequency >= 492.88:
#     print("нота - B4")
# else:
#     print("Такой ноты не существует")

# money = int(input("Введи номинал долларовой банкноты: \n"))
# if money == 1:
#     print("на ней изображен Джордж Вашингтон")
# elif money == 2:
#     print("на ней изображен Томас Джефферсон")
# elif money == 5:
#     print("на ней изображен Авраам Линкольн")
# elif money == 10:
#     print("на ней изображен Александр Гамильтон")
# elif money == 20:
#     print("на ней изображен Эндрю Джексон")
# elif money == 50:
#     print("на ней изображен Улисс Грант")
# elif money == 100:
#     print("на ней изображен Бенджамин Франклин")
# else:
#     print("Банкноты таким номиналом не существует")

# holidayday = int(input("Введи день \n"))
# holidaymounth = int(input("Введи месяц \n"))
# # Пользователь вводит день и месяц
# if holidayday == 1 and holidaymounth == 1:
#     print("%02d.%02d" % (holidayday, holidaymounth) + " - на эту дату приходится Новый "
#                                                       "год")
# elif holidayday == 1 and holidaymounth == 7:
#     print("%02d.%02d" % (holidayday, holidaymounth) + " - на эту дату приходится день "
#                                                       "Канады")
# elif holidayday == 25 and holidaymounth == 12:
#     print("%02d.%02d" % (holidayday, holidaymounth) + " - на этот день "
#                                                      "приходится Рождество")
# # Если данные совпадают с обозначенными то выводится сообщение о празднике
# # "%02d.%02d" % - дает два знакоместа на каждое из перечисленного в списке
# else:
#     print("Эта дата не является праздником")
# # Если введены данные, не совпадающие с необходимыми, то это обозначается в консоли

# mounth = str(input("Введи месяц в виде текста: \n"))
# day = int(input("Введи день в виде цифры: \n"))
# if mounth == "март" and day >= 20:
#     print("Сейчас весна")
# elif mounth == "апрель" or mounth == "май":
#     print("Сейчас весна")
# elif mounth == "июнь" and day <=20:
#     print("Сейчас весна")
# elif mounth == "июнь" and day >= 21:
#     print("Сейчас лето")
# elif mounth == "июль" or mounth == "август":
#     print("Сейчас лето")
# elif mounth == "сентябрь" and day <=21:
#     print("Сейчас лето")
# elif mounth == "сентябрь" and day >= 22:
#     print("Сейчас осень")
# elif mounth == "октябрь" or mounth == "ноябрь":
#     print("Сейчас осень")
# elif mounth == "декабрь" and day <=20:
#     print("Сейчас осень")
# else:
#     print("Сейчас зима")