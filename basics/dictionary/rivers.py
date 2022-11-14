# Задаем словарь переменной
rivers = {"ob'":'russia',
          'nile':'egypt',
          'drin':'albania',
          }

# Проводим проверку с выводом на экран сначала пар
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

# Проводим проверку с выводом на экран ключей и значений по отдельности
print('\nRivers: ')
for river in rivers.keys():
    print(f'{river.title()}')

print('\nCountry: ')
for country in rivers.values():
    print(country.title())