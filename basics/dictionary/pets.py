# Создаем словари и "кладем" их в список
Felix = {'cat':'Oleg'}
Guffi = {'dog':'kira'}
Mikki = {'mouse':'Mindi'}

pets = [Felix, Guffi, Mikki]

# Прогоняем словари из списка через проверку с выводом на экран
# Проверка состоит из цикла for, и такого же, вложенного в него
for pet in pets:
    for animal, owner in pet.items():
        print(f'Owner: {owner.title()}, pet - {animal}')