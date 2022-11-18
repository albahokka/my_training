topping = "Какой топпинг ты хочешь? Напиши:\n"
topping += "Если не хочешь топпинг, нажми 'quit'\n"

while True:
    topping_change = input(str(topping))

    if topping_change == 'quit':
        break
    else:
        print(f"Ты выбрал " + topping_change + '?' + ' Это дополнение включено'
                                                     'в заказ')
        continue