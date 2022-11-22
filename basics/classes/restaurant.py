# Создаем класа, добавляем в метод __init__ два атрибута
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Задаем значение по умолчанию
        self.number_served = 0

# Создаем метод, который выводит два атрибута
    def describe_restaurant(self):
        print(f'\nIn "{self.restaurant_name.title()}" served {self.cuisine_type} '
              f'cuisine!')

# Создаем метод, который выводит заданное сообщение
    def open_restaurant(self):
        print(f'Restaurant "{self.restaurant_name}" is open.')

# Создаем метод для отображения смс со значением по умолчанию
    def served_quantity(self):
        print(f'{self.number_served} - quantity served clients.')

# Создаем метод для изменения значения по умолчанию с проверкой
    def update_served(self, s):
        if s >= self.number_served:
            self.number_served = s
        else:
            print(f"Its a lie :(")

# Создаем метод дял изменения значения по умолчанию с приращиванием
    def increment_served(self, increment_s):
        self.number_served += increment_s

# Создаем экземпляр и передаем классу значения атрибутов
restaurant = Restaurant('Moscow', 'russia')

# Выводим независимые сообщения с обращением к атрибутам
print(f'Go to the restaurant under the name "{restaurant.restaurant_name}"?')
print(f'I heard there {restaurant.cuisine_type} cuisine.')
# print(f'{restaurant.number_served} - quantity served clients.')

# Вызываем методы класса для нашего экземпляра
restaurant.describe_restaurant()
restaurant.open_restaurant()
# restaurant.number_served = 4

# Вызываем метод для изменения значения по умолчанию с заданием значения
restaurant.update_served(5)
restaurant.served_quantity()

# Вызываем метод для изменения значения приращиванием по умолчанию
# с заданием значения, которое необходимо добавить
restaurant.increment_served(10)
restaurant.served_quantity()

# Создаем еще два экземпляра с их значениями, и вызываем для них методы класса
restaurant1 = Restaurant('XYZ', 'georgian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Big Food', 'english')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

# Создаем класс потомок, наследующий методы и атрибуты класса выше (родителя)
class IceCreamStand (Restaurant):
# Инициализируем атрибуты класса-родителя
    def __init__(self, restaurant_name, cuisine_type):
# Вызываем метод __init__ класса-родителя функцией super
        super().__init__(restaurant_name, cuisine_type)
# Присваиваем потомку новый атрибут (список)
        self.flavors = ['chocolate', 'strawberry', 'dairy']

# Создаем новый метод-функцию для вывода на экран назначенного атрибута
    def read_flavors(self):
        print(f'In this restaurant sell following ice cream: {self.flavors}')

# Создаем экземпляр класса-потомка со знаечениями, которые будут присвоены
# атрибутам, взятым из класса-родителя. Далее вызываем два метода
ice_cream = IceCreamStand('Funned milker', 'Ice Cream')
ice_cream.describe_restaurant()
ice_cream.read_flavors()