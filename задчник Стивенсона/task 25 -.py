# s = int(input("Введи общее количество секунд: \n"))
# s_in_day = 86400
# s_in_hour = 3600
# s_in_minute = 60
#
# d = s / s_in_day
# s = s % s_in_day
# h = s / s_in_hour
# s = s % s_in_hour
# m = s / s_in_minute
# s = s % s_in_minute
#
# print("Длительность:", \
#       "%d:%02d:%02d:%02d." % (d, h, m, s))

# import time
# tym = time.localtime()
# #здесь считывается время с начала эпохи в секундах
# opt = time.asctime(tym)
# #здесь оно преобразуется и возвращается к нам обратно в виде времени OS
# print(opt)
# #выводим данное значение на экран

# import math
# print("Давай вычислим в выбранном тобой году, когда в нем наступает Пасха.")
# year = int(input("Введи год: \n"))
# a = year % 19
# b = math.floor(year / 100)
# c = year % 100
# d = math.floor(b / 4)
# e = b % 4
# f = math.floor((b + 8) / 25)
# g = math.floor((b - f + 1) / 3)
# h = (19 * a + b - d - g + 15) % 30
# i = math.floor(c / 4)
# k = c % 4
# l = (32 + 2 * e + 2 * i - h - k) % 7
# m = math.floor((a + 11 * h + 22 * l) / 451)
# month = math.floor((h + l + 7 * m + 114) / 31)
# day = 1 + (h + 1 - 7 * m + 114) % 31
# print("В указанном тобою году Пасха наступает", \
#       "%d.%d.%d." % (day, month, year))

# print("Давай посчитаем индекс массы твоего тела.")
# h = int(input("Введи свой рост в см: \n"))
# w = int(input("Введи свой вес в кг: \n"))
# bmi = w / (h ** 2)
# print("Индекс массы твоего тела равен", "%.6f" % bmi)

# print("Давай посчитаем коэффициент охлаждения ветром при введенных тобой данных.")
# T = float(input("Введи температуру воздуха в градусах Цельсия: \n"))
# V = float(input("Введи скорость ветра в километрах в час: \n"))
# WCI = 13.12 + 0.6215 * T + 11.37 * (V ** 0.16) + 0.3965 * T * (V ** 0.16)
# print("Коэффициент охлаждения ветром равен: " + str(round(WCI)) + ".")

# print("Привет! Давай переведем температуру из Цельсия в Кельвин и Фаренгейт!")
# C = float(input("Введи температуру в градусах Цельсия: \n"))
# F = C * 1.8 +32
# K = C + 273.15
# print("Температура в градусах Цельсия равна: "
#       + str("%.2f" % (C)) + ", в Кельвинах - " + str("%.2f" % (K)) + ", в Фаренгейт - "
#       + str("%.2f" % (F)) + ".")

# print("Привет! Давай переведем давление в различные единицы измерения!")
# kPa = float(input("Введи давление в килопаскалях: \n"))
# PSI = kPa * 6.894759
# mm_rt_st = kPa * 7.500616827041698
# atm = kPa * 101.325011
# print("Давление в килопаскалях равно " + str(kPa) + ", в фунтах на квадратный дюйм - " + str(PSI)
# + ", в милимметрах ртутного столба - " + str(mm_rt_st) + ", в атмосферах - " + str(atm) + ".")

# n = input("Введи целое четырехзначное число: \n")
# n1 = int(n[0])
# n2 = int(n[1])
# n3 = int(n[2])
# n4 = int(n[3])
# #введенное число разбили по частям и преобразовали их как целочисленные
# sm = n1 + n2 + n3 + n4
# #далее преобразованное сложили между собой
# print(sm)

# a = int(input("Введи первое целое число: \n"))
# b = int(input("Введи второе целое число: \n"))
# c = int(input("Введи третье целое число: \n"))
# mn = min(a, b, c)
# mx = max(a, b, c)
# av = a + b + c - mn - mx
# print("Выведем числа в порядке возрастания: " + str(mn) + ", " + str(av) + ", "+ str(mx))

# price = 3.49
# sale = 0.4
# price_with_sale = 3.49 * 0.4
# quantity = int(input("Введи количество купленного вчерашнего хлеба: \n"))
# all_price = price_with_sale * quantity
# print(str("%5.2f" % price) + " - обычная цена за буханку хлеба")
# print(str("%5.2f" % price_with_sale) + " - цена за буханку хлеба со скидкой")
# print(str("%5.2f" % all_price) + " - цена за всю покупку вчерашего хлеба со скидкой")