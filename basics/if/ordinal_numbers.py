# Задаем переменной список  при помощи функций list и range
numbers = list(range(1, 10))
print(numbers)

# Перебираем значения списка, проимзводя проверки условий
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th", end='\n')