"""Import class in modul for our work"""
from class_restaurant import Restaurant

"""Creating an instance and passing attribute values to the class"""
restaurant = Restaurant('Moscow', 'russia')

"""We output independent messages with access to attributes"""
print(f'Go to the restaurant under the name "{restaurant.restaurant_name}"?')
print(f'I heard there {restaurant.cuisine_type} cuisine.')
# print(f'{restaurant.number_served} - quantity served clients.')

"""Calling class methods for our instance"""
restaurant.describe_restaurant()
restaurant.open_restaurant()
# restaurant.number_served = 4

"""Calling the method to change the default value with setting the value"""
restaurant.update_served(5)
restaurant.served_quantity()

"""Calling the method to change the value by default increment
with setting the value to be added"""
restaurant.increment_served(10)
restaurant.served_quantity()

"""Create two more instances with their values, and call methods for them
class"""
restaurant1 = Restaurant('XYZ', 'georgian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Big Food', 'english')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

"""Creating a descendant class inheriting the methods and attributes of 
the class above (parent)"""
class IceCreamStand (Restaurant):

    """Initializing the attributes of the parent class"""
    def __init__(self, restaurant_name, cuisine_type):
        """Calling the __init__ method of the parent class with the super
        function"""
        super().__init__(restaurant_name, cuisine_type)
        """Assign a new attribute (list) to the descendant"""
        self.flavors = ['chocolate', 'strawberry', 'dairy']

    """Creating a new method-function for displaying the assigned attribute 
    on the screen"""
    def read_flavors(self):
        print(f'In this restaurant sell following ice cream: {self.flavors}')

"""Creating an instance of a descendant class with values that will be assigned
to attributes taken from the parent class. Next, we call two methods"""
ice_cream = IceCreamStand('Funned milker', 'Ice Cream')
ice_cream.describe_restaurant()
ice_cream.read_flavors()