# Создаем словари и добавляем их в список people
my_friend0 = {'first_name':'Artur',
             'last_name':'Markovic',
             'age':24,
             'city':'Chelyaba',
             }

my_friend1 = {'first_name':'Egor',
             'last_name':'Egorov',
             'age':22,
             'city':'Great Novgorod',
             }

my_friend2 = {'first_name':'Olga',
             'last_name':'Olegova',
             'age':23,
             'city':'New York',
             }

people = [my_friend0, my_friend1, my_friend2]

# Проводим проверку словарей из списка с выводом на экран
for my_friend in people:
    print(f'\nFull name: {my_friend["first_name"]} {my_friend["last_name"]}')
    print(f'Age: {my_friend["age"]}')
    print(f'City: {my_friend["city"]}')