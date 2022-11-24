"""Creating a class, adding two attributes to the __init__ method"""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        """Setting the default value"""
        self.number_served = 0

    """Creating a method that outputs two attributes"""
    def describe_restaurant(self):
        print(f'\nIn "{self.restaurant_name.title()}" served {self.cuisine_type} '
              f'cuisine!')

    """Creating a method that outputs the specified message"""
    def open_restaurant(self):
        print(f'Restaurant "{self.restaurant_name}" is open.')

    """Creating a method for displaying sms with a default value"""
    def served_quantity(self):
        print(f'{self.number_served} - quantity served clients.')

    """Creating a method to change the default value with verification"""
    def update_served(self, s):
        if s >= self.number_served:
            self.number_served = s
        else:
            print(f"Its a lie :(")

    """Creating a method to change the default value incrementally"""
    def increment_served(self, increment_s):
        self.number_served += increment_s
