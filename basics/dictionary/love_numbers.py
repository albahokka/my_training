# Создаем словарь и подвергаем его проверке для вывода сообщения на экран
love_numbers = {'ala':[8, 3, 6],
                'egor':[7, 8, 4],
                'artem':[3, 5, 2],
                'polina':[5, 2, 4],
                'tanya':[3, 8, 2],
                }

for name, love_number in love_numbers.items():
    print(f"\n{name.title()}'s lovely numbers its: ")
    for number in love_number:
        print(number)