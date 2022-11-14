# Присваиваем переменной список
pizzas = ['pepperoni', 'cheese', 'mushroom']

# С помощью цикла for производим итерации с нашим списком
for pizza in pizzas:
    print('I like ' + pizza + 'pizza')
print('I really love pizza!')

# Копируем список в новую переменную
friend_pizzas = pizzas[:]

# Добавляем в каждый из списков по новому эелементу
pizzas.append('fruit')
friend_pizzas.append('meat')

# Выводим каждый список на экран для демонстрации индивидуальности
print('My favorite pizzas are:')
my_pizzas = [my_pizza for my_pizza in pizzas]
print(my_pizzas)

print('My friends favorite pizzas are:')
friends_pizzas = [friend_pizza for friend_pizza in friend_pizzas]
print(friends_pizzas)
