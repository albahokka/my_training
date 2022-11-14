# Создание числового списка от 1 до 10; возведение каждого элемента списка в куб
# с выводом на экран при помощи цикла for
numbers = list(range(1, 11))
for number in numbers:
    number = number**3
    print(number)

# Выводим на экран части списка (подсписки)
print('The irst three items in yhe list are:' + str(numbers[:3]))
print('The items from the middle of list are:' + str(numbers[3:6]))
print('The last three items in the list are:' + str(numbers[7:]))
