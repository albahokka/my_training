while True:
    age = int(input("Сколько тебе лет? \n"))
    if age < 3:
        print("Твой билет бесплатный")
    elif age >= 3 and age <= 12:
        print("Твой билет в кино стоит 10 долларов")
    elif age > 12:
        print("Твой билет в кино стоит 15 долларов")

    break