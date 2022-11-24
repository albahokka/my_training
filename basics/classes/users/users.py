"""Importing classes from the module"""
from classes_of_admin import *

def u(user):
    user.greet_user()
    user.describe_user()


user0 = User('Вася', 'Пупкин', 16, 'не женат', 'студент')
user0.greet_user()
user0.describe_user()

user0.increment_login_attempts()
user0.increment_login_attempts()
user0.reset_login_attempts()
print(f'{user0.login_attempts}')

user1 = User('Серега', 'Макаров', 28, 'женат', 'грузчик')
user1.greet_user()
user1.describe_user()

user2 = User('Лена', 'Мирова', 23, 'замужем', 'программист')
u(user2)

user_admin = Admin('Толя', 'Быков', 30, 'не женат', 'админ')
user_admin.greet_user()
user_admin.describe_user()
user_admin.privileges_admin.show_privileges()

