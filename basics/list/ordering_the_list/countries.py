countries = ['Russia', 'USA', 'Great Britain', 'Chine', 'Japan']
print(countries)
# Вывели список на экран

print(sorted(countries))
# Вывели список на экран временно отсортировав в алфавитном порядке
print(countries)

print(sorted(countries, reverse=True))
# Временно отсортировали список в обратном алфавитном порядке
print(countries)

countries.reverse()
# Перевернули список
print(countries)

countries.reverse()
# Снова перевернули список
print(countries)

countries.sort()
# Отсортировали список в алфавитном порядке
print(countries)

countries.sort(reverse=True)
# Отсортировали список в обратном алфавитном порядке
print(countries)