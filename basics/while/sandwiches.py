# Создаем два списка: с элементами, и пустой
sandwich_orders = ['whopper', 'big mag', 'pastrami', 'gamburger', 'pastrami']
finished_sandwiches = []

# Удаляем значение из списка безвозвратно с помощью цикла while
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Перебираем циклом while все элементы из первого списка: удаляем их с
# возможностью использования после удаления. Потом выводим на экран сообщение
# с удаленными элементами, которые уже принадлежат другой переменной
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made your sandwich - {made_sandwich.title()}")

# После, удаленные элементы добавляем в пустой список и подвергаем циклу for
# с выводом на экран
    finished_sandwiches.append(made_sandwich)
print("\nAll finished sandwich its: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# Проверяем, пуст ли изначально наполненный список
print(sandwich_orders)

