# Создаем класа, добавляем в метод __init__ два атрибута
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

# Создаем метод, который выводит два атрибута
    def describe_restaurant(self):
        print(f'\nIn "{self.restaurant_name.title()}" served {self.cuisine_type} '
              f'cuisine!')

# Создаем метод, который выводит заданное сообщение
    def open_restaurant(self):
        print(f'Restaurant "{self.restaurant_name}" is open.')

# Создаем экземпляр и передаем классу значения атрибутов
restaurant = Restaurant('Moscow', 'russia')

# Выводим независимые сообщения с обращением к атрибутам
print(f'Go to the restaurant under the name "{restaurant.restaurant_name}"?')
print(f'I heard there {restaurant.cuisine_type} cuisine.')

# Вызываем методы класса для нашего экземпляра
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Создаем еще два экземпляра с их значениями, и вызываем для них методы класса
restaurant1 = Restaurant('XYZ', 'georgian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Big Food', 'english')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()