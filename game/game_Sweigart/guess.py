# # Это игра по угадыванию чисел
# import random
#
# guessesTaken = 0
#
# print("Привет! Как тебя зовут?")
# myName = input()
#
# number = random.randint(1, 100)
# print("Что ж, " + myName + ", я загадываю число от 1 до 100.")
#
# for guessesTaken in range (6):
#     print("Попробуй угадать.") # Четыре пробела перед именем функции print
#     guess = input()
#     guess = int(guess)
#
#     if guess < number:
#         print("Твое число слишком маленькое.") # Восемь пробелов перед именем функции print
#
#     if guess > number:
#         print("Твои число слишком большое")
#
#     if guess == number:
#         break
#
# if guess == number:
#     guessesTaken = str(guessesTaken + 1)
#     print("Отлично, " + myName + "! Ты справился за " + guessesTaken + " попытки!")
#
# if guess != number:
#     number = str(number)
#     print("Увы. Я загадала число " + number + ".")

# Ниже представлены примеры для наилучшего понимания
# import random
# number = random.randint(1000, 2000)
# print(number)
#
# for i in range(3):
#     print("Привет! Переменной i присвоено значение " + str(i))

