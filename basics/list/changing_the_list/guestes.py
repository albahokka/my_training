guestes = ['egor', 'irina', 'nastya']
# Обозначаем список

print(f'Hello, go to me, {guestes[0].title()}')
guest1 = f'Hello, go to me, {guestes[2].title()}'
print(guest1)
print(f'Hello, go to me, {guestes[1].title()}')
# Выводим на экран терминала сообщения с определенным элементом списка, указанного выше
# Метод title() позволяет выводит значение с прописной буквы

popped_guestes = guestes.pop(1)
# print(guestes)
# При помощи метода выше, удаляем значение списка индекса 1 и можем его использовать дальше

guestes.insert(1, 'Olga')
# print(guestes)
# При помощи метода выше, вставляем новый элемент на указанный в списке индекс 1

print('Sadly, ' + popped_guestes + ' wont be able to come ')

print(f'Hello, go to me, {guestes[0].title()}')
guest1 = f'Hello, go to me, {guestes[2].title()}'
print(guest1)
print(f'Hello, go to me, {guestes[1].title()}')

print('I have new table and want many guestes now!')

guestes.insert(0, 'Kate')
guestes.insert(2, 'Tanya')
guestes.append('Igor')
# append() позволяет добавить новое значение в конец списка
print(guestes)

print(f'Hello, go to me, {guestes[0].title()}')
guest1 = f'Hello, go to me, {guestes[2].title()}'
print(guest1)
print(f'Hello, go to me, {guestes[1].title()}')
print(f'Hello, go to me, {guestes[3].title()}')
print(f'Hello, go to me, {guestes[4].title()}')
print(f'Hello, go to me, {guestes[5].title()}')

print('Sadly, table is late. Therefore today my guestes is two man.')

popped_guest1 = guestes.pop(0)
popped_guest2 = guestes.pop(0)
popped_guest3 = guestes.pop(0)
popped_guest4 = guestes.pop(0)
print(guestes)
# Удаляем из списка все элементы, кроме двух. Выводим их на экран

for i in guestes:
    print('My first proposal is valid, ' + i + '.')
# Запускаем цикл для вывода сообщения на экран терминала при присутствии значения в указанном списке

popped_Guestes = []
popped_Guestes.append(popped_guest1)
popped_Guestes.append(popped_guest2)
popped_Guestes.append(popped_guest3)
popped_Guestes.append(popped_guest4)
# print(popped_Guestes)
# Добавили удаленные значения в новый список "удаленных значений"

for i in popped_Guestes:
    print('Sorry, dont visiting me, ' + i.title() + ', table is late.')
# Запускаем цикл для вывода сообщения на экран терминала при присутствии значения в указанном списке

del guestes[0]
del guestes[0]
# Удаляем последние значения из списка

print(guestes)
# Убеждаемся, что список пуст

print(len(guestes))
# Посчитали при помощи функции len() количество элементов в списке